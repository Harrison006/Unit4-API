import pandas as pd
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from datetime import datetime


# Import the calendar package

from calendar import month_name
djia_data = pd.read_csv('export-9e612197-df7b-4af1-9df9-fed0998c64d2.csv')
djia_data = djia_data.rename(columns = {"Incident Date": "Date", "State": "State","City Or County": "City", "# Victims Injured": "# Victims Injured", "# Victims Killed": "# Victims Killed"})
djia_data.head()  
#djia_data["Date"] = pd.to_datetime(djia_data["Date"])
#djia_data = djia_data.sort_values(by="Date")
# Order by months by chronological order
"""djia_data["Month"] = pd.Categorical(djia_data["Date"].dt.month_name(), month_name[1:])
# Group metrics by monthly averages
djia_monthly_mean = djia_data \
    .groupby('Month') \
    .mean() \
    .reset_index()
djia_monthly_mean = djia_data.groupby("Month").mean().reset_index()
djia_monthly_mean.head(6)
"""
"""
plt.bar(djia_monthly_mean['Month'], height = djia_monthly_mean['Close'])

plt.show()

"""

# reordering bar plots from largest to smallest
#djia_monthly_mean_srtd = djia_monthly_mean.sort_values(by="# Victims Injured", ascending=False)
plt.bar(["State"], height="# Victims Injured")
plt.bar(
    height=["# Victims Injured"],
    color=["blue", "gray", "red", "green", "green", "gray"],
)


plt.show()

