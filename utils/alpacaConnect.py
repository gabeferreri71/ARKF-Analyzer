#All neccesary imports
import os
import datetime
import pandas as pd
from datetime import date
from dotenv import load_dotenv
import alpaca_trade_api as tradeapi
from importlib_metadata import method_cache
import os
#get ticker list
# requesting manually is beyond my ability to do

#names = os.listdir("./data")
#read in data
df = pd.read_csv(r".\data\ARK_FINTECH_INNOVATION_ETF_ARKF_HOLDINGS.csv")
print(df.columns)
relevantdf = df[['ticker', 'weight (%)']]
relevantdf.ticker.apply(str)
relevantdf= relevantdf.loc[relevantdf["ticker"]!= "4689"]
relevantdf.dropna(inplace=True)
tickers = relevantdf['ticker'].to_list()

#connect to alpaca

load_dotenv()
alpaca_api_key= os.getenv("ALPACA_API_KEY")
alpaca_secret_key= os.getenv("ALPACA_SECRET_KEY")

alpaca = tradeapi.REST(
    alpaca_api_key,
    alpaca_secret_key,
    api_version="v2"
)
today= date.today().strftime("%Y-%m-%d")
year_3= date.today() - datetime.timedelta(days=3*365)

start_date = pd.Timestamp(year_3, tz= "America/New_York").isoformat()
end_date = pd.Timestamp(today, tz= "America/New_York").isoformat()
timeframe = "1D"
limit_rows = 1000

# loop through tickers and get data 
def get_data(ticker):
    data = alpaca.get_barset(
        ticker,
        timeframe,
        start= start_date,
        end= end_date,
        limit= limit_rows
    ).df
    return data
prices_df = alpaca.get_barset(
    tickers,
    timeframe,
    start= start_date,
    end= end_date,
    limit= limit_rows
).df

"""
# drop all unnecesarry info

prices_df.drop(["open", "high", "low", "volume"], axis=1, level=1, inplace=True)
prices_df.dropna(axis=1, how="all", inplace=True)

# fill Nan values

prices_df= prices_df.fillna(prices_df.rolling(6,min_periods=1).mean())
# print(prices_df)

# save the data in the data folder in sqlite format 
# ALTHOUGH DO WE ACTUALLY NEED THIS CONSIDERING WE ARE UPDATING the data anyway?
# writing all the functions that will check for the presence of 
# relevant data in the database will make it 20 percent more efficient but will take 80% more time
"""