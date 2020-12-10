import logging
import sys
from selenium.webdriver.remote.remote_connection import LOGGER

if len(sys.argv) >= 2 and sys.argv[1].lower() == "-debug":
    logging.basicConfig(level=logging.DEBUG)
    print("Logger limit to DEBUG")
else:
    logging.basicConfig(level=logging.WARNING)
    print("Logger limit to WARNING")
LOGGER.setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)


def debug(text):
    logging.debug(text)


def info(text):
    logging.info(text)


def warning(text):
    logging.warning(text)


def error(text):
    logging.error(text)


def crit(text):
    logging.critical(text)
