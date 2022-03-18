import requests
import datetime
from matplotlib import pyplot as plt

data = []
usd_to_brl = []
days = []

today = datetime.date.today()
today_date = today.strftime('%y-%m-%d')

date = [year, month, day] = today_date.split('-')

year = '20' + year

tag = int(day)

for i in range(20):
    
    url = f"https://freecurrencyapi.net/api/v2/historical?apikey=c7fa61b0-7b5c-11ec-b981-e732d3fb49be&base_currency=USD&date_from={year}-{month}-{day}&date_to={year}-{month}-{day}"