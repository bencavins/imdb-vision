import csv

from app import app
from models import db
from models.tv_series import TVSeries


tv_series_tsv_path = 'datasets/title.basics.tsv'


with app.app_context():
    TVSeries.query.delete()

    # Loop through the TSV file with TV Series data
    count = 0
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
