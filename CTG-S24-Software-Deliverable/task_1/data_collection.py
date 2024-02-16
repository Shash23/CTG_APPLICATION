#!/usr/bin/env python
# coding: utf-8

# In[5]:


import yfinance as yahooFinance
import csv
import os
import datetime
import pandas as pd


# In[6]:



filename = "tickers.txt"

tickers = []

# issue: getting the names from the file, not knowing strip()
with open(filename, 'r') as f:
    for line in f:
        tickers.append(line.strip())
        
# tickers


# In[7]:


if not os.path.exists("data"):
    os.makedirs("data")
    
startDate = datetime.datetime(2021, 1, 1)
endDate = datetime.datetime(2023, 12, 31)


def calculate_adjusted_close(df):
    
    df['Adjusted Close'] = df.apply(lambda row: row["Close"] + row["Dividends"] - (row["Close"] / row["Stock Splits"]),  axis=1)

for company in tickers:
    
    filename = company + ".csv"

    getCompanyInformation = yahooFinance.Ticker(company)
    company_history = getCompanyInformation.history(start = startDate, end = endDate)
    
    company_history['Adjusted Close'] = company_history.apply(lambda row: row["Close"] + row["Dividends"] if row["Stock Splits"] == 0 else row["Close"] + row["Dividends"] - (row["Close"] / row["Stock Splits"]), axis = 1)
    company_history.index = company_history.index.strftime('%m/%d/%Y')
    
    
    filename = os.path.join("data", f"{company}.csv")
    

    company_history.to_csv(filename)

