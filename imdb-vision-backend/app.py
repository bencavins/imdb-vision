import os

from flask import Flask
from flask_migrate import Migrate
from flask_cors import CORS
from dotenv import dotenv_values
from fuzzywuzzy import fuzz

from models import db
from models.title import Title
from models.episode import Episode
from models.rating import Rating


env_values = dotenv_values()

app = Flask(
    __name__, 
    static_folder='../imdb-vision-frontend/dist',
    static_url_path='/'
)
app.config['SQLALCHEMY_DATABASE_URI'] = env_values.get('TEST_DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = True

db.init_app(app)
migrate = Migrate(app, db)
CORS(app)


@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.errorhandler(404)
def not_found(e):
    return app.send_static_file('index.html')

@app.get('/tv_series')
def get_all_tv_series():
    series = Title.query.filter(
        Title.type == 'tvSeries'
    ).all()

    data = [s.to_dict(rules=('-episodes',)) for s in series]

    return data, 200

@app.get('/tv_series/<string:title>')
def get_tv_series_by_title(title):
    series = Title.query.filter(
        Title.type == 'tvSeries'
    ).filter(
        Title.primary_title.ilike(f"%{title}%")
    ).all()

    data = [s.to_dict(rules=('-episodes',)) for s in series]

    # use Levenstein matching to score each title
    for series in data:
        series['score'] = fuzz.WRatio(series['primary_title'], title)

    # sort data based on the score
    return sorted(data, key=lambda series: series['score'], reverse=True), 200

@app.get('/tv_series/<int:id>')
def get_tv_series_by_id(id):
    tv = Title.query.filter(
        Title.id == id
    ).first()

    if not tv:
        return {'error': 'Invalid ID'}, 404
    
    return tv.to_dict(), 200
