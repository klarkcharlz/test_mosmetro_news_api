from datetime import datetime, timedelta

from flask_restful import Resource
from flask import request, make_response
import json

from src.databases import MosmetroNews
from src.logger import logger


class Mosmetro(Resource):

    def get(self):
        day = request.args.get('day')

        if day:
            date_time = datetime.now() - timedelta(days=int(day))
            news = MosmetroNews.query.filter(MosmetroNews.posted_at >= date_time).all()
        else:
            news = MosmetroNews.query.all()

        news = [{'title': row.title,
                 'img_url': row.img_url,
                 'posted_at': row.posted_at.strftime("%Y-%m-%d")} for row in news]

        logger.info(news)

        # так сделано потому что иначе вместо русских букв возвращает юникод символы
        response = make_response(str({"news": news}).replace("'", '"'))
        response.headers['charset'] = 'utf-8'
        return response
