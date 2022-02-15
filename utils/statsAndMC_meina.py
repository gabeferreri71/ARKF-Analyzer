# Import module
import os
from matplotlib.pyplot import axis
import pandas as pd
import numpy.random as rnd
from MCForecastTools import MCSimulation

#Print the documentation of the MCSimulation module of the MCForecastTools library
#?MCSimulation

#Read in csv files
ARK_df = prices_df
print(ARK_df)
#ARK_df_index=ARK_df.droplevel(level=1)


# Create a simulation object
# This portfolio will have a 20/80 split between training dataset split from dataset obtained and validation dataset from dataset obtained in the weight parameter
# We set the number of simulations trials to be 10
# The period over which we will simulate is the number of trading days in a 3 year times the number of years.

three_year_simulation = MCSimulation(
    portfolio_data=ARK_df,
    weights=[0.20, 0.80],
    num_simulation=50,
    num_trading_days=252*3,
)
three_year_simulation.portfolio_data.head()
three_year_simulation.calc_cumulative_return()

# Run the Monte Carlo simulation to forecast the cumulative return
three_year_simulation.calc_cumulative_return()

# Visualize the simulation by creating an
# overlay line plot
three_year_simulation.plot_simulation()

# Visualize distribution
three_year_simulation.plot_distribution()

# Generate summary statistics from the simulation results
three_year_simulation.summarize_cumulative_return()