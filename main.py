import requests
import polars as pl
from sqlalchemy.engine.url import URL


def req_cyrpto_market_data(api_url: str, token: str):
    """Send API request to coinmarketcap to get market data"""
    response = requests.api.get(
        url=api_url,
        headers={
            'X-CMC_PRO_API_KEY': token
        }
    )

    return pl.DataFrame(response.json()["data"])


def read_time_checkpoint(timeframe: str, db_url: URL):
    """Read the historic prices
    
    param timeframe: str
    param options: 
        <2,4>HR, <(1-7)>DAY 
    """
    table = ""
    timeframe_column = ""
    sql_query = f"SELECT * FROM {table} WHERE {timeframe_column} = {timeframe};"

    return pl.read_database(
        query=sql_query,
        connection=db_url
    )


if __name__ == "__main__":
    response = req_cyrpto_market_data(
        api_url="https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/listings/latest",
        token="b54bcf4d-1bca-4e8e-9a24-22ff2c3d462c"
    )
    breakpoint()