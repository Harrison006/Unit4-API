import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from datetime import datetime
import pandas as pd


djia_data = pd.read_csv('HistoricalPrices.csv')
djia_data = djia_data.rename(columns = {' Open': 'Open', ' High': 'High', ' Low': 'Low', ' Close': 'Close'})
djia_data.head()    
z = np.polyfit(djia_data['Open'], djia_data['Close'], 1)
p = np.poly1d(z)


plt.scatter(djia_data['Open'], djia_data['Close'], c=djia_data['Close'], cmap = plt.cm.plasma)
plt.plot(djia_data['Open'], p(djia_data['Open']))

plt.savefig('DJIA 2023 Scatterplot Open vs. Close.png')
plt.show()