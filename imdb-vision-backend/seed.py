import csv

from app import app
from models import db
from models.tv_series import TVSeries
from models.episode import Episode


tv_series_tsv_path = 'datasets/title.basics.tsv'
episode_tsv_path = 'datasets/title.episode.tsv'


def main():
    with app.app_context():
        TVSeries.query.delete()
        Episode.query.delete()

        print("Loading TV Series...")
        load_tv_series()
        print("Loading Episodes...")
        load_episodes()


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
            db.session.add(episode)
    db.session.commit()


if __name__ == '__main__':
    main()
