import numpy as np
import pandas as pd
from config.settings import logger
from database.models import FinanceData
import os

def transform_data(raw_data):
    logger.info("Transforming data....")
    time_series = raw_data.get("Time Series (5min)", {})

    if not time_series:
        logger.warning("No time series found in API response")
        return pd.DataFrame()
    
    df = pd.DataFrame.from_dict(time_series, orient="index")
    df.reset_index(inplace=True)
    df.rename(columns={
        "index": "timestamp",
        "1. open": "open",
        "2. high": "high",
        "3. low": "low",
        "4. close": "close",
        "5. volume": "volume"
    }, inplace=True)

    df = df.astype({
        "open": float,
        "high": float,
        "low": float,
        "close": float,
        "volume": int 
    })
    df["average_price"] = np.mean(df[["open", "close"]], axis=1)
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    os.makedirs("data", exist_ok=True)
    df.to_csv("data/transformed_data.csv", index=False)
    logger.info("Data transformation complete")
    logger.info("Data fetched successfully from API")
    return df
