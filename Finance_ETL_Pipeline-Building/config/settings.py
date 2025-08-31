import logging
from sqlalchemy import create_engine
import requests
demo="H3BLL91WVKQMAFQG"

company_name=input("Enter the company name: ")

finance_api_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={company_name}&interval=5min&apikey={demo}"
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
database_url="mysql+pymysql://root:vedank10@localhost:3306/finance_db"
engine=create_engine(database_url,echo=True)
r=requests.get(finance_api_url)
if r.status_code == 200:
    logger.info("API is reachable")