from books_recommender.exception import AppException
import sys
from books_recommender.logger.log import logging

try:
    a = 3/0
except Exception as e:
    logging.info(e)
    raise AppException(e, sys) from e