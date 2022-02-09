import ARKFconnect
import pandas as pd
import alpaca_trade_api as tradeapi
tickers = ARKFconnect.relevantdf['ticker'].to_list()
print(tickers)
#connect to alpaca





# loop through tickers and get data 





# clean the data





# combine the data into a nice dataframe





# save the data in the data folder in sqlite format 
# ALTHOUGH DO WE ACTUALLY NEED THIS CONSIDERING WE ARE UPDATING the data anyway?
# writing all the functions that will check for the presence of 
# relevant data in the database will make it 20 percent more efficient but will take 80% more time

import sqlConnect



