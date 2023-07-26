from sqlalchemy_serializer import SerializerMixin

from models import db


class Episode(db.Model, SerializerMixin):
    __tablename__ = 'episodes'

    serialize_rules = ('-rating.episode', '-tv_series.episodes')

    id = db.Column(db.Integer, primary_key=True)
    imdb_id = db.Column(db.String, db.ForeignKey('titles.imdb_id'), nullable=False, index=True, unique=True)
    parent_imdb_id = db.Column(db.String, db.ForeignKey('titles.imdb_id'), nullable=False)
    season_number = db.Column(db.Integer)
    episode_number = db.Column(db.Integer)

    tv_series = db.relationship('Title', foreign_keys=[parent_imdb_id], back_populates='episodes', uselist=False)
    title = db.relationship('Title', foreign_keys=[imdb_id], uselist=False)
    rating = db.relationship('Rating', uselist=False, backref='episode')

    def __repr__(self):
        return f"<Episode {self.imdb_id} {self.parent_imdb_id} {self.season_number} {self.episode_number}>"
