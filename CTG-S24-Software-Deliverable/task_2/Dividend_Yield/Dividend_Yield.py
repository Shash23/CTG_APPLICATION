#!/usr/bin/env python
# coding: utf-8

# In[2]:


'''
Name: Shashwat Ghevde
'''


# In[ ]:


import pandas as pd
import os


# In[3]:


# accessing the tickers.txt in Task 1 folder

parent_dir = ".."
task_dir = "task_1"
filename = "tickers.txt"

data_directory = os.path.join(parent_dir, task_dir,filename)

tickers = []
with open(data_directory, 'r') as f:
    for line in f:
        tickers.append(line.strip())


# In[5]:



'''
Formula: Dividends / Current Stock Price
This measures the dividend income as a percentage of the stock price.
'''

'''
Parameters: df(Dataframe with the wanted columns), ticker(String with company ticker name)
Return: N/A

This method calculates the volume momentum
'''
def calculate_dividend_yield(df, ticker):
    df[f"{ticker}"] = (df["Dividends"] / df["Close"]) * 100
    return df


momentum_df = pd.DataFrame()

parent_dir = ".."
task_dir = "task_1"
data_dir = "data"
extension = ".csv"

first_ticker_flag = True

for ticker in tickers:
    
    ticker_extension = ticker + extension
    
    company_path = os.path.join(parent_dir, task_dir, data_dir, ticker_extension)
    df = pd.read_csv(company_path)
    df = calculate_dividend_yield(df, ticker)    
    df = df[['Date', f'{ticker}']]
    
    if first_ticker_flag:
        momentum_df = df
        first_ticker_flag = False
    else:
        momentum_df = pd.merge(momentum_df, df, on = "Date", how = "left")
        
        
    
momentum_df.fillna('', inplace = True)    

filename = "dividend_yield.csv"
momentum_df.to_csv(filename)

