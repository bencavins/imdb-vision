from sqlalchemy_serializer import SerializerMixin

from models import db


class Episode(db.Model, SerializerMixin):
    __tablename__ = 'episodes'

    serialize_rules = ('-rating.episode', '-tv_series.episodes')

    id = db.Column(db.Integer, primary_key=True)
    imdb_id = db.Column(db.String, nullable=False, index=True, unique=True)
    parent_imdb_id = db.Column(db.String, db.ForeignKey('titles.imdb_id'), nullable=False)
    season_number = db.Column(db.Integer)
    episode_number = db.Column(db.Integer)

    rating = db.relationship('Rating', uselist=False, backref='episode')

    def __repr__(self):
        return f"<Episode {self.imdb_id} {self.parent_imdb_id} {self.season_number} {self.episode_number}>"
