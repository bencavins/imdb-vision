from flask import Flask
from flask_migrate import Migrate

from models import db
from models.tv_series import TVSeries
from models.episode import Episode
from models.rating import Rating


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

db.init_app(app)
migrate = Migrate(app, db)


@app.get('/')
def get_root():
    return '<h1>HELLO</h1>'

@app.get('/tv_series/<int:id>')
def get_tv_series_by_id(id):
    tv = TVSeries.query.filter(
        TVSeries.id == id
    ).first()

    if not tv:
        return {'error': 'Invalid ID'}, 404
    
    return tv.to_dict(), 200
