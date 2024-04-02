import requests
from os import getenv
from fastapi import HTTPException

ALPHAVANTAGE_APIKEY = getenv("ALPHAVANTAGE_APIKEY")


def sync_converter(from_currency: str, to_currency: str, price: float):
    url = f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={from_currency}&to_currency={to_currency}&apikey={ALPHAVANTAGE_APIKEY}"

    try:
        response = requests.get(url=url)

    except Exception as e:
        raise HTTPException(status_code=400, detail=e)

    data = response.json()

    print(data)
    
    if "Realtime Currency Exchange Rate" not in data:
        raise HTTPException(status_code=400, detail='Probably invalid currencies given')
    
    return float(data["Realtime Currency Exchange Rate"]["5. Exchange Rate"])