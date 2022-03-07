import re
from datetime import date, datetime

import requests
from sqlalchemy.dialects.postgresql import insert
from lxml import html as hl

from src.settings import MOSMETRO_NEWS_URL
from src.databases import MosmetroNewsSchema, MosmetroNews
from src import db
from src.logger import logger
from .x_path import NEWS_BLOCK_PATH, BLOCK_PATH, TITLE_PATH, IMG_URL_PATH, DATE_PATH

DATE_MAP = {
    'января': '01',
    'февраля': '02',
    'марта': '03',
    'апреля': '04',
    'мая': '05',
    'июня': '06',
    'июля': '07',
    'августа': '08',
    'сентября': '09',
    'октября': '10',
    'ноября': '11',
    'декабря': '12',
}


def pars_date(date: str) -> list:
    date = date.split()
    return date


def get_mosmetro_news() -> str:
    logger.info("Получение данных с сайта")
    while True:
        try:
            response = requests.get(MOSMETRO_NEWS_URL, timeout=10)
        except Exception as err:
            logger.error("Ошибка при запросе к сайту.")
            logger.exception(err)
        else:
            if response.status_code == 200:
                logger.info("Данные получены успешно!")
                return response.text
            else:
                logger.warning(f"Данные не получены, статус код: {response.status_code}.")
                return ""


def parse_html(html: str, schema) -> dict:
    logger.info("Парсим данные...")
    html_xpath = hl.fromstring(html)
    news_block = html_xpath.xpath(NEWS_BLOCK_PATH)[0]
    news_blocks = news_block.xpath(BLOCK_PATH)
    for news in news_blocks:
        try:
            data = {'title': news.xpath(TITLE_PATH)[0],
                    'posted_at': news.xpath(DATE_PATH)[0],
                    'img_url': re.match(r'.*\((.+)\)', news.xpath(IMG_URL_PATH)[0])[1]}
            date_ = pars_date(data['posted_at'])
            data['posted_at'] = date(year=datetime.now().year,
                                     month=int(DATE_MAP[date_[1].replace(",", "")]),
                                     day=int(date_[0]))
        except Exception as err:
            logger.error("ошибка при парсинге.")
            logger.exception(err)
        else:
            news = MosmetroNews(**data)
            try:
                logger.info('Валидация данных...')
                schema.dump(news)
            except Exception as err:
                logger.error('Данные не валидны...')
                logger.exception(err)
            else:
                logger.info('Данные валидны...')
                db.session.execute(insert(MosmetroNews)
                                   .values(data)
                                   .on_conflict_do_nothing())
    logger.info('Запись в БД...')
    db.session.commit()


def main():
    logger.info("Старт скраппинга")
    news_schema = MosmetroNewsSchema()
    html = get_mosmetro_news()
    parse_html(html, news_schema)
