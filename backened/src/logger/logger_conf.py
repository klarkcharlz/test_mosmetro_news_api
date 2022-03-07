import logging
import sys


FORMAT = logging.Formatter('%(asctime)-25s  %(levelname)-10s  %(name)-10s  %(message)s')

# обработчик который выводит сообщение в консоль
terminal_log = logging.StreamHandler(sys.stderr)
terminal_log.setFormatter(FORMAT)

# Создать регистратор
logger = logging.getLogger('api_news')
logger.setLevel(logging.INFO)
logger.addHandler(terminal_log)
