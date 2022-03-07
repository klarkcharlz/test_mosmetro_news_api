from .models import News
from src import ma


class NewsSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = News
        load_instance = True

    title = ma.String(required=True)
    img_url = ma.String(required=True)
    posted_at = ma.Date(required=True, format='%Y-%m-%d')
