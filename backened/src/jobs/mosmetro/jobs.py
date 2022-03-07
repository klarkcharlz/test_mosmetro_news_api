from multiprocessing import Process
from time import sleep

import schedule

from src.resources import parser_mosmetro_news


def job():
    sleep(10)
    parser_mosmetro_news()
    schedule.every(10).minutes.do(parser_mosmetro_news)
    while True:
        schedule.run_pending()
        sleep(10)


job = Process(target=job, daemon=True, )