import csv

from app import app
from models import db
from models.title import Title
from models.episode import Episode
from models.rating import Rating


tv_series_tsv_path = 'datasets/title.basics.tsv'
episode_tsv_path = 'datasets/title.episode.tsv'
ratings_tsv_path = 'datasets/title.ratings.tsv'

chunk_size = 10000  # for batch inserts

reader_kwargs = {
    'delimiter': '\t',
    'quotechar': None,
}

# short
# titleType
# tvMiniSeries
# tvSpecial
# tvEpisode
# video
# tvMovie
# tvSeries
# videoGame
# tvShort
# tvPilot
# movie


def main():
    with app.app_context():
        print('Dropping data')
        Rating.query.delete()
        Episode.query.delete()
        Title.query.delete()

        print("Loading Titles")
        load_tv_series()
        print()

        print("Loading Episodes")
        load_episodes()
        print()

        print('Loading Ratings')
        load_ratings()
        print()


def load_tv_series():
    """
    Loop through the TSV file with TV Series data and save in DB.
    """
    with open(tv_series_tsv_path, 'r') as f:
        reader = csv.reader(f, **reader_kwargs)  # using a ~ for the quote char cuz the default (") was causing problems
        next(reader) # skip header

        batch = []
        for row in reader:
            # Header should look like this:
            # tconst, titleType, primaryTitle, originalTitle, isAdult, startYear, endYear, runtimeMinutes, genres
            if row[1] not in ['tvMiniSeries', 'tvSpecial', 'tvEpisode', 'tvSeries', 'tvShort', 'tvPilot', 'tvMovie']:
                continue

            tv_series = Title(
                imdb_id=row[0],
                type=row[1], 
                primary_title=row[2],
                original_title=row[3],
                is_adult=True if row[4] == '1' else False,
                start_year=row[5],
                end_year=row[6] if row[6] != '\\N' else None,
                runtime=row[7] if row[7] != '\\N' else None,
                genres=row[8] if row[8] != '\\N' else None,
            )
            batch.append(tv_series)

            if len(batch) >= chunk_size:
                print('.', end='', flush=True)
                db.session.bulk_save_objects(batch)
                batch = []
        db.session.bulk_save_objects(batch)

    db.session.commit()

def load_episodes():
    with open(episode_tsv_path, 'r') as f:
        reader = csv.reader(f, **reader_kwargs)
        # skip header
        next(reader)

        batch = []
        for row in reader:
            # row[0] == tconst
            # row[1] == parentTconst
            # row[2] == seasonNumber
            # row[3] == episodeNumber
            episode = Episode(
                imdb_id=row[0],
                parent_imdb_id=row[1],
                season_number=row[2] if row[2] != '\\N' else None,
                episode_number=row[3] if row[3] != '\\N' else None,
            )
            batch.append(episode)

            # bulk updates to save memory
            # can switch to bulk_insert_mappings if need better performance
            if len(batch) >= chunk_size:
                print('.', end='', flush=True)
                db.session.bulk_save_objects(batch)
                batch = []
        db.session.bulk_save_objects(batch)
    db.session.commit()


def load_ratings():
    # all_ep_ids = Episode.query.with_entities(Episode.imdb_id).all()

    with open(ratings_tsv_path, 'r') as f:
        reader = csv.reader(f, **reader_kwargs)
        next(reader)  # skip header 

        batch = []
        for row in reader:
            # row[0] == tconst
            # row[1] == averageRating
            # row[2] == numVotes
            ep = Episode.query.filter(Episode.imdb_id == row[0]).first()
            if not ep:
                continue

            rating = Rating(
                imdb_id=row[0],
                average_rating=row[1],
                num_votes=row[2],
            )
            batch.append(rating)

            if len(batch) >= chunk_size:
                print('.', end='', flush=True)
                db.session.bulk_save_objects(batch)
                batch = []
        db.session.bulk_save_objects(batch)
    db.session.commit()


if __name__ == '__main__':
    main()
