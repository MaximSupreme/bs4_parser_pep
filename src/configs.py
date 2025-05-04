import logging
from logging.handlers import RotatingFileHandler
import argparse

from constants import (
    DT_FORMAT, LOG_FORMAT, LOG_DIR, LOG_FILE,
    MAXBYTES, BACKUPCOUNT
)


def configure_argument_parser(available_modes):
    parser = argparse.ArgumentParser(description='Парсер документации Python')
    parser.add_argument(
        'mode',
        choices=available_modes,
        help='Режимы работы парсера'
    )
    parser.add_argument(
        '-c',
        '--clear-cache',
        action='store_true',
        help='Очистка кеша'
    )
    parser.add_argument(
        '-o',
        '--output',
        choices=('pretty', 'file'),
        help='Дополнительные способы вывода данных'
    )
    return parser


def configure_logging():
    log_dir = LOG_DIR
    log_dir.mkdir(exist_ok=True)
    log_file = LOG_FILE
    rotating_handler = RotatingFileHandler(
        log_file, maxBytes=MAXBYTES, backupCount=BACKUPCOUNT
    )
    logging.basicConfig(
        datefmt=DT_FORMAT,
        format=LOG_FORMAT,
        level=logging.INFO,
        handlers=(rotating_handler, logging.StreamHandler())
    )
