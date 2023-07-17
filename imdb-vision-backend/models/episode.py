from models import db


class Episode(db.Model):
    __tablename__ = 'episodes'

    id = db.Column(db.Integer, primary_key=True)
    imdb_id = db.Column(db.String, nullable=False, index=True)
    parent_imdb_id = db.Column(db.String, db.ForeignKey('tv_series.imdb_id'), nullable=False)
    season_number = db.Column(db.Integer)
    episode_number = db.Column(db.Integer)

    def __repr__(self):
        return f"<Episode {self.imdb_id} {self.parent_imdb_id} {self.season_number} {self.episode_number}>"
