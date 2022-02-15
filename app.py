from matplotlib.pyplot import spy
import pandas as pd 
import numpy as np
import questionary
import matplotlib.pyplot as plt
import fire 
from utils.MCForecastTools import MCSimulation as MCSimulation
import utils.alpacaConnect as alpacaConnect
tickers = alpacaConnect.tickers
data = alpacaConnect.prices_df

fund_ticker = questionary.text("What is the ticker of the fund you want to simulate?").ask()
while True:
    analysis_ticker = questionary.select(f'Which ticker from {fund_ticker} would you like to analyze?', tickers).ask()

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
    print("LOADING DATA")
    if spy_data is None:
        spy_data = alpacaConnect.alpaca.get_barset(
            "SPY",
            "1D",
            start= first_date,
            end= last_date,
            limit= 1000
        ).df
        fund_data = alpacaConnect.alpaca.get_barset(
            fund_ticker,
            "1D",
            start= first_date,
            end= last_date,
            limit= 1000
        )
        comparison = pd.concat([spy_data, fund_data], axis=1)
        spyMC = MCSimulation(total_data, weights = [1, 0], num_simulation=300, num_trading_days=comparison.shape[0])
        fundMC = MCSimulation(total_data, weights = [0, 1], num_simulation=300, num_trading_days=comparison.shape[0])
        print("Loading data completed")
    total_data = pd.concat([ticker_data, comparison], axis=1)
    total_data.dropna(inplace=True)
    print(total_data.head())
    simulationTicker = MCSimulation(total_data, weights = [1, 0], num_simulation=300, num_trading_days=total_data.shape[0])
    print("Loading data completed")
    # simulation.plot_simulation()
    # plt.plot(simulation.simulated_return)
    # plt.show()
    # plot_title = f"Distribution of Final Cumuluative Returns Across All {simulation.nSim} Simulations"
    # simulation.simulated_return.iloc[-1, :].plot(kind='hist', bins=10,density=True,title=plot_title)
    # plt.axvline(simulation.confidence_interval.iloc[0], color='r')
    # plt.axvline(simulation.confidence_interval.iloc[1], color='r')
    # plt.show()

    stats_ticker = simulation.summarize_cumulative_return()
    stats_SPY = spy_data.summarize_cumulative_return()
    stats_fund = fund_data.summarize_cumulative_return()
    print("Here are the results:")
    result = 0
    if stats_ticker.mean > stats_fund:
        result+=1
        print(f"{analysis_ticker} is predicted to do better than {fund_ticker}")
    if stats_ticker.mean < stats_fund:
        result-=1
        print(f"{analysis_ticker} is underperforming compared to {fund_ticker}")
    if stats_ticker.mean > stats_SPY:
        result+=1
        print(f"{analysis_ticker} is predicted to do better than S&P500")
    if stats_ticker.mean < stats_SPY:
        result-=1
        print(f"{analysis_ticker} is underperforming compared to S&P500")
    # for beta and sharpe similar thing
    # except for both beta and sharpe we only compare to the spy
    #next line is temporary before we have the beta and sharpe
    beta = 1
    sharpe = 2
    stats_ticker.beta = beta
    stats_ticker.sharpe = sharpe
    data_for_json = {
        "analysis_ticker": analysis_ticker,
        "fund_ticker": fund_ticker,
        "stats_ticker": stats_ticker,
        "stats_SPY": stats_SPY,
        "stats_fund": stats_fund,
        "result": result,
        "date of analysis": first_date
    }

