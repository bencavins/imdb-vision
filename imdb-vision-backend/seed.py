from app import app
from models import db
from models.tv_series import TVSeries


with app.app_context():
    TVSeries.query.delete()

