import pandas as pd
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from datetime import datetime


# Import the calendar package

from calendar import month_name
djia_data = pd.read_csv("HistoricalPrices.csv")
djia_data.head()
djia_data = djia_data.rename(
    columns={" Open": "Open", " High": "High", " Low": "Low", " Close": "Close"}
)
djia_data["Date"] = pd.to_datetime(djia_data["Date"])
djia_data = djia_data.sort_values(by="Date")
# Order by months by chronological order
djia_data["Month"] = pd.Categorical(djia_data["Date"].dt.month_name(), month_name[1:])
# Group metrics by monthly averages
djia_monthly_mean = djia_data \
    .groupby('Month') \
    .mean() \
    .reset_index()
djia_monthly_mean = djia_data.groupby("Month").mean().reset_index()
djia_monthly_mean.head(6)
"""

plt.bar(djia_monthly_mean['Month'], height = djia_monthly_mean['Close'])

plt.show()

"""

# reordering bar plots from largest to smallest
djia_monthly_mean_srtd = djia_monthly_mean.sort_values(by="Close", ascending=False)
plt.bar(djia_monthly_mean_srtd["Month"], height=djia_monthly_mean_srtd["Close"])
plt.bar(
    djia_monthly_mean_srtd["Month"],
    height=djia_monthly_mean_srtd["Close"],
    color=["blue", "gray", "red", "green", "green", "gray"],
)


plt.show()

