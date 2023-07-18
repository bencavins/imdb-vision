import csv

from app import app
from models import db
from models.tv_series import TVSeries
from models.episode import Episode
from models.rating import Rating


tv_series_tsv_path = 'datasets/title.basics.tsv'
episode_tsv_path = 'datasets/title.episode.tsv'
ratings_tsv_path = 'datasets/title.ratings.tsv'

chunk_size = 1000  # for batch inserts


def main():
    with app.app_context():
        print("Loading TV Series...")
        TVSeries.query.delete()
        load_tv_series()
        print("Loading Episodes...")
        Episode.query.delete()
        load_episodes()
        print('Loading Ratings...')
        Rating.query.delete()
        load_ratings()


def load_tv_series():
    """
    Loop through the TSV file with TV Series data and save in DB.
    """
    with open(tv_series_tsv_path, 'r') as f:
        reader = csv.reader(f, delimiter='\t')
        for row in reader:
            # Header should look like this:
            # tconst, titleType, primaryTitle, originalTitle, isAdult, startYear, endYear, runtimeMinutes, genres
            if row[1] == 'tvSeries':  # make sure this is a tv series (movies and shorts are in the dataset too)
                tv_series = TVSeries(
                    imdb_id=row[0],
                    primary_title=row[2],
                    original_title=row[3],
                    is_adult=True if row[4] == '1' else False,
                    start_year=row[5],
                    end_year=row[6] if row[6] != '\\N' else None,
                    runtime=row[7] if row[7] != '\\N' else None,
                    genres=row[8] if row[8] != '\\N' else None,
                )
                db.session.add(tv_series)
    db.session.commit()


def load_episodes():
    with open(episode_tsv_path, 'r') as f:
        reader = csv.reader(f, delimiter='\t')
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
                db.session.bulk_save_objects(batch)
                batch = []
    db.session.commit()


def load_ratings():
    with open(ratings_tsv_path, 'r') as f:
        reader = csv.reader(f, delimiter='\t')
        next(reader)  # skip header 

        batch = []
        for row in reader:
            # row[0] == tconst
            # row[1] == averageRating
            # row[2] == numVotes
            rating = Rating(
                imdb_id=row[0],
                average_rating=row[1],
                num_votes=row[2],
            )
            batch.append(rating)

            if len(batch) >= chunk_size:
                db.session.bulk_save_objects(batch)
                batch = []
    db.session.commit()


if __name__ == '__main__':
    main()
