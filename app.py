import pandas as pd 
import numpy as np
import questionary
import fire 

import utils.ARKFconnect as ARKFconnect
tickers = ARKFconnect.relevantdf['ticker'].to_list()


analysis_ticker = questionary.select("Which ticker from ARKF would you like to analyze?", tickers).ask()