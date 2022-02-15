import pandas as pd
import sqlalchemy
from alpacaConnect import prices_df 

database_connection_string = 'sqlite:///ticker.db'

engine = sqlalchemy.create_engine(database_connection_string)
engine

prices_df.to_sql('ticker', engine)

engine.table_names() 