import os

from flask import Flask
from flask_migrate import Migrate
from flask_cors import CORS

from models import db
from models.title import Title
from models.episode import Episode
from models.rating import Rating


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = ''
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

db.init_app(app)
migrate = Migrate(app, db)
CORS(app)


@app.get('/')
def get_root():
    return '<h1>HELLO</h1>'

@app.get('/tv_series/<int:id>')
def get_tv_series_by_id(id):
    tv = Title.query.filter(
        Title.id == id
    ).first()

    if not tv:
        return {'error': 'Invalid ID'}, 404
    
    return tv.to_dict(), 200
