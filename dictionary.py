"""
json_entry ={}

json_entry["ticker"] = {
    "ticker": "AAPL",
    "2/9/2022" : {
        "date": '5',
        "beta": "1",
        'sharpe': "1"
        },
    "2/10/2022" : {
        "date": '10',
        "beta": "2",
        'sharpe': "1"
        },
}
betas = []
dates =[]
for item in json_entry:
    if item != 'ticker':
        betas.append(json_entry[item]['beta'])
print(betas)

"""


from pathlib import Path
import json

path = Path("./data/data.json")
json_entry = {
    "Ticker" : ticker,
    "Date" : time,
    "Beta" : beta,
    "Sharpe" : sharpe
}
# data_for_json = {
#         "analysis_ticker": analysis_ticker,
#         "fund_ticker": fund_ticker,
#         "ticker_stats": stats_ticker,
#         "SPY_stats": stats_SPY,
#         "fund_stats": stats_fund,
#         "result": result,
#         "date of analysis": first_date
#     }
def pushJson(path, json_entry):
    with open(path, 'w') as outfile:
       response = json.load(json_entry, outfile)


def pullJson(path, response):
    # load the json file
    return json.dump(response)

data = pullJson(path, response)
ticker_of_interest = "COIN"
just_ticker = {}
for item in json:
    # look for ticker
    # add item to just_ticker



  
        
