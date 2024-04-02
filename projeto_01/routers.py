from fastapi import APIRouter
from converter import sync_converter
import requests

router = APIRouter()
url = "https://economia.awesomeapi.com.br/"


@router.get("/converter/{currency_pairs}")
def converter(currency_pairs: str):
    response = requests.get(url=f"{url}json/last/{currency_pairs}")

    return response.json()
