from sqlalchemy_serializer import SerializerMixin

from models import db


class TVSeries(db.Model, SerializerMixin):
    __tablename__ = 'tv_series'

    serialize_rules = ('-episodes.tv_series',)

    id = db.Column(db.Integer, primary_key=True)
    imdb_id = db.Column(db.String, unique=True, index=True)
    primary_title = db.Column(db.String, nullable=False)
    original_title = db.Column(db.String)
    is_adult = db.Column(db.Boolean, default=False)
    start_year = db.Column(db.String)
    end_year = db.Column(db.String)
    runtime = db.Column(db.Integer)
    genres = db.Column(db.String)

    episodes = db.relationship('Episode', backref='tv_series')

    def __repr__(self):
        return f"<Show {self.imdb_id} {self.primary_title}>"
