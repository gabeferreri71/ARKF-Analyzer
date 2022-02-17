from matplotlib.pyplot import spy
import pandas as pd 
import questionary
import matplotlib.pyplot as plt
import fire 
import utils.gauge as gauge
from utils.MCForecastTools import MCSimulation as MCSimulation
import utils.alpacaConnect as alpacaConnect
import utils.beta_sharpe_functions as stats 
    

def run():
   
    tickers = alpacaConnect.tickers
    # analysis_ticker = questionary.select("Which ticker from ARKF would you like to analyze?", tickers).ask()
    # take the first and last date
    # first_date = ticker_data.index[0]
    # last_date = ticker_data.index[-1]
    # print(ticker_data.head())
    # get SPY data
    # ticker_data = alpacaConnect.get_data(analysis_ticker)
    fund_ticker = questionary.text("What is the ticker of the fund you want to simulate (ARKF)?").ask()
    spy_data = None

    while True:
        analysis_ticker = questionary.select(f'Which ticker from {fund_ticker} would you like to analyze?', tickers).ask()

        # ticker_data = data[analysis_ticker].dropna()
        # # take the first and last date
        # first_date = ticker_data.index[0]
        # last_date = ticker_data.index[-1]
        # print(ticker_data.head())
        # get SPY data
        ticker_data = alpacaConnect.get_data(analysis_ticker)
        print("LOADING DATA")
        if spy_data is None:
            
            spy_data = alpacaConnect.get_data("SPY")
            fund_data = alpacaConnect.get_data(fund_ticker)
            # print(spy_data.head())
            comparison = pd.concat([spy_data, fund_data], axis=1)
            spyMC = MCSimulation(comparison, weights = [1, 0], num_simulation=200, num_trading_days=comparison.shape[0])
            fundMC = MCSimulation(comparison, weights = [0, 1], num_simulation=200, num_trading_days=comparison.shape[0])
        total_data = pd.concat([ticker_data, spy_data], axis=1)
        total_data.dropna(inplace=True)
        # print(total_data.head())
        simulationTicker = MCSimulation(total_data, weights = [1, 0], num_simulation=200, num_trading_days=total_data.shape[0])
        print("Loading data completed")
        # simulation.plot_simulation()
        # plt.plot(simulation.simulated_return)
        # plt.show()
        # plot_title = f"Distribution of Final Cumuluative Returns Across All {simulationTicker.nSim} Simulations"
        # simulationTicker.simulated_return.iloc[-1, :].plot(kind='hist', bins=10,density=True,title=plot_title)
        # plt.axvline(simulationTicker.confidence_interval.iloc[0], color='r')
        # plt.axvline(simulationTicker.confidence_interval.iloc[1], color='r')
        # plt.show()


        stats_ticker = simulationTicker.summarize_cumulative_return()
        stats_SPY = spyMC.summarize_cumulative_return()
        stats_fund = fundMC.summarize_cumulative_return()
        print("Here are the results:")
        result = 3
        if stats_ticker["mean"] > stats_fund["mean"]:
            result+=.5
            print(f"{analysis_ticker} is predicted to do better than {fund_ticker}")
        if stats_ticker["mean"] < stats_fund["mean"]:
            result-=.5
            print(f"{analysis_ticker} is underperforming compared to {fund_ticker}")
        if stats_ticker["mean"] > stats_SPY["mean"]:
            result+=.5
            print(f"{analysis_ticker} is predicted to do better than S&P500")
        if stats_ticker["mean"] < stats_SPY["mean"]:
            result-=.5
            print(f"{analysis_ticker} is underperforming compared to S&P500")
        # for beta and sharpe similar thing
        # except for both beta and sharpe we only compare to the spy
        #next line is temporary before we have the beta and sharpe
        beta = stats.beta(total_data)
        sharpe = stats.sharpe(total_data).ticker_data

        if beta > 1:
            result-=.5
            print(f"{analysis_ticker} is predicted to be more volatile than S&P500")
        if beta < 1:
            result+=.5
            print(f"{analysis_ticker} is predicted to be less volatile than S&P500")
        if sharpe > 1:
            result+=.5
            print(f"{analysis_ticker} has a good risk/return ratio")
        if sharpe < 1:
            result-=.5
            print(f"{analysis_ticker} has a poor risk/return ratio")
        stats_ticker.beta = beta
        stats_ticker.sharpe = sharpe
        data_for_json = {
            "analysis_ticker": analysis_ticker,
            "result": result,
            "date of analysis": total_data.index[-1],
        }


        # spy_data.drop(["open", "high", "low", "volume"], axis=1, level=1, inplace=True)
        # spy_data.dropna(axis=1, how="all", inplace=True)
        # spy_data= spy_data.fillna(spy_data.rolling(6,min_periods=1).mean())
        # ticker_data.drop(["open", "high", "low", "volume"], axis=1, level=1, inplace=True)
        # ticker_data.dropna(axis=1, how="all", inplace=True)
        # ticker_data= spy_data.fillna(spy_data.rolling(6,min_periods=1).mean())
        total_data = pd.concat([ticker_data, spy_data], axis=1)
        total_data.dropna(inplace=True)
        # print(total_data.head())
        # simulation = MCSimulation(total_data, weights = [0.5, 0.5], num_simulation=100, num_trading_days=total_data.shape[0])
        # simulation.plot_simulation()
        # plt.plot(simulation.simulated_return)
        # plot_title = f"Distribution of Final Cumuluative Returns Across All {simulation.nSim} Simulations"

        '''
        plt = simulation.simulated_return.iloc[-1, :].plot(kind='hist', bins=10,density=True,title=plot_title)
        plt.axvline(simulation.confidence_interval.iloc[0], color='r')
        plt.axvline(simulation.confidence_interval.iloc[1], color='r')
        '''
        # plt.show()

        gauge.gauge(labels=['Strong Sell','Sell','Hold','Buy', 'Strong Buy'], \
            colors=['darkred','red','gray','lightgreen','green'], arrow=int(result), title='Buy or Sell?')



        again = questionary.select("Would you like to analyze another ticker?", choices=["Yes", "No"]).ask()
        if again == "No":
            break


if __name__ == "__main__":
    fire.Fire(run)    