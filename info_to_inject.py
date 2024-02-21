import yfinance as yf
from models import Stocks
from tradelens import app, db
import warnings

warnings.filterwarnings("ignore", category=FutureWarning)


sofi = yf.Ticker('SOFI')
# print(sofi.major_holders)
# print(sofi.balance_sheet)

'''
print(sofi.get_calendar())

<class 'dict'> of length 7
{'Earnings Date': [datetime.date(2024, 4, 29), datetime.date(2024, 5, 3)], 
'Earnings High': 0.04, 
'Earnings Low': -0.02, 
'Earnings Average': 0.01,
'Revenue High': 662000000, 
'Revenue Low': 541900000, 
'Revenue Average': 568380000}
'''

hist_data = sofi.history(period="1d")

# Get the first row which corresponds to the last trading day
last_day = hist_data.iloc[0]

print(last_day['Open'])
print(last_day['High'])
print(last_day['Low'])
print(last_day['Close'])
print(last_day['Volume'])


print(sofi.get_fast_info()['lastPrice']) # this gets live volume??

