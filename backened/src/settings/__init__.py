import configparser
import os


CONF_PATH = f'{os.path.dirname(__file__)}/config.ini'
assert os.path.exists(CONF_PATH), 'Не найден файл конфигурации'

CONFIG = configparser.ConfigParser()
CONFIG.read(CONF_PATH)

from .settings import DATABASE_URL, MOSMETRO_NEWS_URL
