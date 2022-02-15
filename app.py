from matplotlib.pyplot import spy
import pandas as pd 
import numpy as np
import questionary
import fire 
from utils.MCForecastTools import MCSimulation as MCSimulation
import utils.alpacaConnect as alpacaConnect
tickers = alpacaConnect.tickers
data = alpacaConnect.prices_df

analysis_ticker = questionary.select("Which ticker from ARKF would you like to analyze?", tickers).ask()

ticker_data = data[analysis_ticker].dropna()
# take the first and last date
first_date = ticker_data.index[0]
last_date = ticker_data.index[-1]
print(ticker_data.head())
# get SPY data
ticker_data = alpacaConnect.alpaca.get_barset(
    analysis_ticker,
    "1D",
    start= first_date,
    end= last_date,
    limit= 1000
).df

spy_data = alpacaConnect.alpaca.get_barset(
    "SPY",
    "1D",
    start= first_date,
    end= last_date,
    limit= 1000
).df

# spy_data.drop(["open", "high", "low", "volume"], axis=1, level=1, inplace=True)
# spy_data.dropna(axis=1, how="all", inplace=True)
# spy_data= spy_data.fillna(spy_data.rolling(6,min_periods=1).mean())
# ticker_data.drop(["open", "high", "low", "volume"], axis=1, level=1, inplace=True)
# ticker_data.dropna(axis=1, how="all", inplace=True)
# ticker_data= spy_data.fillna(spy_data.rolling(6,min_periods=1).mean())
total_data = pd.concat([ticker_data, spy_data], axis=1)
total_data.dropna(inplace=True)
print(total_data.head())
simulation = MCSimulation(total_data, weights = [0.5, 0.5], num_simulation=1000, num_trading_days=total_data.shape[0])
simulation.plot_simulation()

