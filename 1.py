import json
import pandas as pd
from datetime import datetime
from pandas.core.api import DataFrame as DataFrame
from baseloader import BaseDataLoader
from enum import Enum

class Granularity(Enum):
    ONE_MINUTE = 60
    FIVE_MINUTES = 300
    FIFTEEN_MINUTES = 900
    ONE_HOUR = 3600
    SIX_HOURS = 21600
    ONE_DAY = 86400

class CoinbaseLoader(BaseDataLoader):

    def __init__(self, endpoint="https://api.exchange.coinbase.com"):
        super().__init__(endpoint)

    def _get_data(self, url: str, params: dict = None) -> pd.DataFrame:
        try:
            data = self._get_req(url, params)
            df = pd.DataFrame(json