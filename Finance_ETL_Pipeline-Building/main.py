from concurrent.futures import ThreadPoolExecutor
from etl.extract import fetch_finance_data
from etl.transform import transform_data
from etl.load import load_data_to_db
from config.settings import logger,engine
from database.models import Base

Base.metadata.create_all(engine)


def run_etl_pipeline():
    raw=fetch_finance_data()
    if raw:
        df=transform_data(raw)
        if not df.empty:
            load_data_to_db(df)
    else:
        logger.error("No data fetched from API, ETL pipeline aborted.")
def perform_queries():
    queries=[
        "SELECT * FROM finance_data",
        "SELECT COUNT(*) FROM finance_data",
        "SELECT AVG(average_price) FROM finance_data",
        "SELECT MAX(high_price) FROM finance_data",
        "SELECT MIN(low_price) FROM finance_data"]
    def run_query(query):
        with engine.connect() as connection:
            result = connection.execute(query)
            result.fetchall()
            logger.info(f"Executed query: {query}")
    with ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(run_query, queries)
    
if __name__ == "__main__":
    run_etl_pipeline()
    perform_queries()
    logger.info("ETL pipeline and queries executed successfully.")