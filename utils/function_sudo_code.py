#read this sudo conceptual code, since did not obtain clean data yet.
#function 1 to create individual beta ticker 
#function 2 to sharp ration risk metric
#------------------------------------

#1. tickers beta(for individual one) & the ticker correlation with S&P 500(Section 1)

# create dataframe where the columns are the closing prices for each ticker
from random import betavariate

#total data is in app.py is the combined ticker data and s&p500
for (columnName, columnData) in total_data.iteritems():
    print('Stock Name:', columnName)
    print('Stock Value:', columnData.values)
    # Sort datetime index in ascending order (past to present)
    total_data.sort_index(inplace=True)
    # Set column names to 'tickers' and 'S&P 500'
    total_data.columns = ['ticker_data', 'comparison']
    total_data.head()
    # to calculate daily returns of closing prices for each column,Use the `pct_change` function 
    daily_returns = total_data.pct_change()
    daily_returns.head()

    # Calculate covariance of all daily returns of tickers vs. S&P 500
    covariance = daily_returns['ticker_data'].cov(daily_returns['comparison'])
    covariance

    # Calculate variance of all daily returns of tickers vs. S&P 500
    variance = daily_returns['comparison'].var()
    variance

    # Calculate beta of all daily returns of tickers
    tickers_beta = covariance / variance
    tickers_beta

    # Calculate the correlation for the daily_returns dataframe using the pearson method.
    #corr_tickers_sp500=daily_returns.corr(method="pearson")

    print('stock beta:', tickers_beta)



#---------------------------------------
#function 2 (section 2)
#total data is in app.py is the combined ticker data and s&p500
for (columnName, columnData) in total_data.iteritems():
    print('Stock Name:', columnName)
    print('Stock Value:', columnData.values)

    # Calculate the daily percent changes and drop n/a values
    total_data = total_data.pct_change().dropna()
    total_data.head()

    year_trading_days = len(total_data)
    # Calculate the annual average return
    average_annual_return = total_data.mean() * year_trading_days
    average_annual_return

    # Calculate the annualized standard deviation
    annualized_standard_deviation = total_data.std() * (year_trading_days) ** (1 / 2)
    annualized_standard_deviation

    # Calculate the sharpe ratios
    sharpe_ratios = average_annual_return / annualized_standard_deviation

    # Plot the sharpe ratios(optional)
    sharpe_ratios.plot.bar(title="Sharpe Ratios")

    print('Stock Sharpe_Ratios:', sharpe_ratios)

    plt.show()


