import sys

from loguru import logger

logger.add(sys.stderr, backtrace=True, diagnose=True)
logger.info('Initializing logger ...')
