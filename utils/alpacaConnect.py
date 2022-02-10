import os
import ARKFconnect
import pandas as pd
import alpaca_trade_api as tradeapi
from dotenv import load_dotenv

tickers = ARKFconnect.relevantdf['ticker'].to_list()

#connect to alpaca

load_dotenv()
alpaca_api_key= os.getenv("ALPACA_API_KEY")
alpaca_secret_key= os.getenv("ALPACA_SECRET_KEY")


alpaca = tradeapi.REST(
    alpaca_api_key,
    alpaca_secret_key,
    api_version="v2"
)

start_date = pd.Timestamp("2019-02-09", tz= "America/New_York").isoformat()
end_date = pd.Timestamp("2022-02-09", tz= "America/New_York").isoformat()
timeframe = "1D"
limit_rows = 1000

# loop through tickers and get data 

prices_df = alpaca.get_barset(
    tickers,
    timeframe,
    start= start_date,
    end= end_date,
    limit= limit_rows
).df

# clean the data


#print(prices_df)


prices_df.drop(["open", "high", "low", "volume"], axis=1, level=1, inplace=True)

print(prices_df)


print(prices_df["4689"])


"""
for row in prices_df["4689"]["close"]:



# combine the data into a nice dataframe





# save the data in the data folder in sqlite format 
# ALTHOUGH DO WE ACTUALLY NEED THIS CONSIDERING WE ARE UPDATING the data anyway?
# writing all the functions that will check for the presence of 
# relevant data in the database will make it 20 percent more efficient but will take 80% more time

import sqlConnect
"""