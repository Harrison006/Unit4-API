import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from datetime import datetime
import pandas as pd

djia_data = pd.read_csv('./HistoricalPrices.csv')
djia_data = djia_data.rename(columns = {' Open': 'Open', ' High': 'High', ' Low': 'Low', ' Close': 'Close'})
djia_data.head()    
plt.scatter(djia_data['Open'], djia_data['Close'])

plt.legend()
plt.show()