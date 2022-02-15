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

path = Path("../utils/MCForecastTools.py")
json_entry = {
    "Ticker" : ticker,
    "Date" : time,
    "Beta" : beta,
    "Sharpe" : sharpe
}
def pushJson(path, json_entry):
    with open(path, 'w') as outfile:
       response = json.load(json_entry, outfile)


def pullJson(path):
    json.dump(response)
  
        
