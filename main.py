import requests
import polars as pl


def get_cyrpto_market_data(api_url: str, token: str):
    """Send API request to coinmarketcap to get market data"""
    response = requests.api.get(
        url=api_url,
        headers={
            'X-CMC_PRO_API_KEY': token
        }
    )

    return response.json()


if __name__ == "__main__":
    resonse_data = get_cyrpto_market_data(
        api_url="https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/listings/latest",
        token="b54bcf4d-1bca-4e8e-9a24-22ff2c3d462c"
    )
    breakpoint()
    crypto_df = pl.DataFrame(resonse_data["data"])