import requests
import pandas as pd
import matplotlib.pyplot as plt

url = 'https://api.coingecko.com/api/v3/coins/bitcoin/market_chart'

days = 120
params = {
    'vs_currency': 'usd',
    'days': '{days}',  # Número de dias para os dados históricos, por exemplo, 30 dias
    'interval': 'daily'
}

def cryptocurrency_price_analysis():
    # Code to analyze cryptocurrency prices
    print("Running Cryptocurrency Price Analysis...")
    # Add API calls, data processing, and visualization here
    pass