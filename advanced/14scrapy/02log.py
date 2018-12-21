import logging
logging.basicConfig(level=logging.INFO,
format='%(levelname)s [%(filename)s:%(lineno)d]'
      ': %(message)s'
      '- %(asctime)s', datefmt='[%d/%b/%y %H:%M:%S]'

)
logger = logging.getLogger(__name__)

if __name__ == "__main__":
    logger.warning('this is log!')