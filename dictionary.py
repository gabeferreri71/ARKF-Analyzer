json_entry = {
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

def pushJson(path, json):
    with open(path, 'w') as outfile:
        json.dump(json, outfile)


def pullJson(path):
    pass
    # return json
        
