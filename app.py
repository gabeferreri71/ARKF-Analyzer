from matplotlib.pyplot import spy
import pandas as pd 
import numpy as np
import questionary
import fire 

import utils.alpacaConnect as alpacaConnect
tickers = alpacaConnect.tickers
data = alpacaConnect.prices_df

analysis_ticker = questionary.select("Which ticker from ARKF would you like to analyze?", tickers).ask()

ticker_data = data[analysis_ticker].dropna()
# take the first and last date
print(ticker_data.head())
first_date = ticker_data.index[0]
last_date = ticker_data.index[-1]

# get SPY data
spy_data = alpacaConnect.alpaca.get_barset(
    "SPY",
    "1D",
    start= first_date,
    end= last_date,
    limit= 1000
).df

spy_data.drop(["open", "high", "low", "volume"], axis=1, level=1, inplace=True)
spy_data.dropna(axis=1, how="all", inplace=True)
spy_data= spy_data.fillna(spy_data.rolling(6,min_periods=1).mean())
total_data = pd.concat([ticker_data, spy_data], axis=1)
print(total_data.dropna().head())

