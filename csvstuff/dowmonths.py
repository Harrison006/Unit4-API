# Import the calendar package 
from datetime import datetime as dt
from calendar import month_name
import pandas as pd


# Order by months by chronological order
djia_data = pd.read_csv('HistoricalPricesMonth.csv')
djia_data['Month'] = pd.Categorical(djia_data['Date'].dt.month_name(), month_name[1:])
djia_data.head()  
# Group metrics by monthly averages
djia_monthly_mean = djia_data \
    .groupby('Month') \
    .mean() \
    .reset_index()

djia_monthly_mean.head(6)