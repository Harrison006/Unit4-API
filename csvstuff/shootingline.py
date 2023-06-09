import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from datetime import datetime


djia_data = pd.read_csv('export-9e612197-df7b-4af1-9df9-fed0998c64d2.csv')
djia_data = djia_data.rename(columns = {"State": "State","City Or County": "City", "# Victims Injured": "# Victims Injured", "# Victims Killed": "# Victims Killed"})
djia_data.head()    
z = np.polyfit(djia_data['# Victims Killed'], djia_data['# Victims Killed'], 1)
p = np.poly1d(z)


vitims["shootings"] = djia_data['# Victims Injured'].astype(str) +"-"+ djia_data["# Victims Killed"]
plt.scatter(djia_data[victims], djia_data["State"], cmap = plt.cm.plasma)
plt.plot(djia_data["# Victims Killed"], p(djia_data["# Victims Killed"]))

plt.savefig('DJIA 2023 Scatterplot Open vs. Close.png')
plt.show()