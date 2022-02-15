from pathlib import Path
import json

path = Path("./data/data.json")

# data_for_json = {
#         "analysis_ticker": analysis_ticker,
#         "fund_ticker": fund_ticker,
#         "ticker_stats": stats_ticker,
#         "SPY_stats": stats_SPY,
#         "fund_stats": stats_fund,
#         "result": result,
#         "date of analysis": first_date
#     }
     
def pushJson(path, data_for_json):
    with open(path, 'w') as outfile:
       response = json.load(data_for_json, outfile)


def pullJson(path, response):
    # load the json file
    return json.dump(response)

data = pullJson(path, response)
ticker_of_interest = "COIN"
just_ticker = {}
for item in data:
    # look for ticker
    # add item to just_ticker
    if analysis_ticker == ticker_of_interest:
        just_ticker.append(analysis_ticker)



  
        
