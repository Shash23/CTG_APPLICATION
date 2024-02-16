#!/usr/bin/env python
# coding: utf-8

# In[44]:


'''
Name: Shashwat Ghevde
'''


# In[45]:


import pandas as pd
import os


# In[46]:


# accessing the tickers.txt in Task 1 folder

parent_dir = ".."
task_dir = "task_1"
filename = "tickers.txt"

data_directory = os.path.join(parent_dir, task_dir,filename)

tickers = []
with open(data_directory, 'r') as f:
    for line in f:
        tickers.append(line.strip())


# In[48]:


'''
Parameters: df(Dataframe with the wanted columns), ticker(String with company ticker name)
Return: N/A

This method calculates the price momentum

issue: had to re-learn lambda functions to account for Stock Splits = 0(ZeroDivisionError)
'''

def calculate_price_momentum(df, ticker):
    df[f"{ticker}"] = ((df["Close"] - df["Close"].shift(5)) / df["Close"].shift(5)) * 100
    return df

# Initializing DataFrame for putting information into csv
momentum_df = pd.DataFrame()

parent_dir = ".."
task_dir = "task_1"
data_dir = "data"
extension = ".csv"

first_ticker_flag = True

# Used to append Momentum to the Dataframe
for ticker in tickers:
    
    ticker_extension = ticker + extension
    
    # reading the data into the CSV
    company_path = os.path.join(parent_dir, task_dir, data_dir, ticker_extension)
    df = pd.read_csv(company_path)
    
    
    df = calculate_momentum(df, ticker)    
    df = df[['Date', f'{ticker}']]
    
    # issue: adding the price momentum because it kept getting reassigned
    
    # if there is only one company, add the dataframe, and turn off the flag
    if first_ticker_flag:
        momentum_df = df
        first_ticker_flag = False
    else:
        #else, merge on the new company to the dataframe
        momentum_df = pd.merge(momentum_df, df, on = "Date", how = "left")
        
# replacing NaN with Spaces
momentum_df.fillna('', inplace = True)



# adding to price_momentum.csv
filename = "price_momentum.csv"
momentum_df.to_csv(filename)


momentum_df

