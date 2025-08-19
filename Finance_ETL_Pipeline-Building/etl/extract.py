import requests
import logging
from config.settings import finance_api_url,logger
def fetch_finance_data():
    logger.info("fetching data from API...")
    try:
        response=requests.get(finance_api_url)
        response.raise_for_status()
        logger.info("Data fethched Successfully from API")
        return response.json()
    except Exception as e:
        logging.error(e)
        return None
