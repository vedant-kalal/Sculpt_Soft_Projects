from sqlalchemy.orm import sessionmaker
from config.settings import engine, logger
from database.models import FinanceData

Session = sessionmaker(bind=engine)

def load_data_to_db(df):
    logger.info("loading data to database...")
    session= Session()
    try:
        for _, row in df.iterrows():
            finance_data = FinanceData(
            timestamp=row['timestamp'],
            open_price=row['open'],
            high_price=row['high'],
            low_price=row['low'],
            close_price=row['close'],
            volume=row['volume'],
            average_price=row['average_price']
        )
            session.add(finance_data)
        session.commit()
        logger.info("Data loaded successfully to database")
    except Exception as e:
        session.rollback()
        logger.error(f"Failed to load data to database: {e}") 
    finally:
        session.close()
        logger.info("Database session closed")


