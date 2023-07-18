from models import db


class Rating(db.Model):
    __tablename__ = 'ratings'

    id = db.Column(db.Integer, primary_key=True)
    imdb_id = db.Column(db.String, db.ForeignKey('episodes.imdb_id'), nullable=False)
    average_rating = db.Column(db.Float)
    num_votes = db.Column(db.Integer)

    def __repr__(self):
        return f"<Rating {self.average_rating}>"
