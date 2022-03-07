from src import db


class News(db.Model):

    __tablename__ = "mosmetro_news"

    id = db.Column(db.BigInteger, primary_key=True, index=True)
    title = db.Column(db.String(125))
    img_url = db.Column(db.String(255))
    posted_at = db.Column(db.Date, index=True)

    __table_args__ = (db.UniqueConstraint('title', 'img_url', 'posted_at', name='_unique_news'), )
