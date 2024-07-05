import pandas  as pd
import logging

# setupt the lgging

logging.basicConfig(level=logging.info)
logger = logging.getLogger(__name__)


def extract_data(file_path):
    try:
        df = pd.read_csv(file_path)
        logger.info()
        logger.info('DAta extracted succesful.')
        return df
    except Exception as e:
        logger.error(f'extracting data : {e}')
        raise

extract_data()
