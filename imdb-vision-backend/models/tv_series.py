from models import db


class TVSeries(db.Model):
    __tablename__ = 'tv_series'

    id = db.Column(db.Integer, primary_key=True)
    imdb_id = db.Column(db.String, unique=True, index=True)
    primary_title = db.Column(db.String, nullable=False)
    original_title = db.Column(db.String)
    is_adult = db.Column(db.Boolean, default=False)
    start_year = db.Column(db.String)
    end_year = db.Column(db.String)
    runtime = db.Column(db.Integer)
    genres = db.Column(db.String)

    def to_dict(self):
        return {
            'id': self.id,
            'imdb_id': self.imdb_id,
        }

    def __repr__(self):
        return f"<Show {self.imdb_id} {self.primary_title}>"
