<!-- #region -->
# Price Momentum/Volume Adjusted Calculation Guide

This document is paired with **price_momentum.py**, **volume_adjusted_momentum.py**. It explains accessing, interpreting, and issues that arose from implementing these files. 

### Accessing the Data

The price momentum and volume adjusted momentum calculations are based on the historical stock data derived from the `tickers.txt` file in the `Task 1` directory.

**Data Source**: This script reads from tickers.txt. `tickers.txt` contains a new line of a unique stock ticker. 

**Data Processing**: For each ticker, the script accesses its corresponding CSV file from the task_1/data folder.

### Interpreting the Data

`price_momentum.csv` contains columns for the 'Date' and its calculated price momentum for each ticker over a two year period. Each ticker's momentum is given by its column name in its abbreviation.

`volume_momentum.csv` contains columns for the 'Date' and its calculated volume adjusted momentum for each ticker over a two year period. Each ticker's momentum is given by its column name in its abbreviation.


### Calculating Price Momentum

**Calculation and Data Storage**: This script calculates the price momentum/volume adjusted momentum as the percent change in the current closing price over a 5 day period. The method adds a new column to the data named after the ticker symbol. Then the calculated price momentum/volume_adjusted_momentum for all the tickers is compiled into a single DataFrame which is exported to price_momentum.csv/volume_momentum.csv.


### Issues Encountered & Solutions

**Reading Tickers from File**: I had trouble accessing the tickers.txt from the Task 1 directory but I learned to use os.path.join to find the relative path and to also ensure that it works over different operating systems.

**Lambda Functions and Stock Splits**: It was not directly related to the main functionality of calculating the price momentum, but going over lambda function again because I had to account for there being no value for the 5 day period.

**Merging DataFrames**: The biggest challenge in this file was to make sure that all of the tickers got appened to the dataframe without overwriting the existing data. I decided to use a flag to add the first company's data directly into the DataFrame and then merge the next company's data on the 'Date' column. 
<!-- #endregion -->

<!-- #region -->
# Dividend Yield Guide

This document is paired with **Dividend_Yield.py**. It explains accessing, interpreting, and issues that arose from implementing these files. 

### Accessing the Data

The price momentum and volume adjusted momentum calculations are based on the historical stock data derived from the `tickers.txt` file in the `Task 1` directory.

**Data Source**: This script reads from tickers.txt. `tickers.txt` contains a new line of a unique stock ticker. 

**Data Processing**: For each ticker, the script accesses its corresponding CSV file from the task_1/data folder.

### Interpreting the Data

`divided_yield.csv` contains columns for the 'Date' and its calculated dividend yield for each ticker over a two year period. Each ticker's momentum is given by its column name in its abbreviation.


### Calculating Dividend Yield

**Calculation and Data Storage**: This script calculates the dividend yield adjusted momentum as the percent change in the current closing price over a 1 day period. The method adds a new column to the data named after the ticker symbol.

### Why Dividend Yield
I chose to do Dividend Yield because it measures the dividend income compared to its current stock price. This could be useful for determining the value of the dividends that are being payed out by the company to compare to its earnings. However, one of the limitations with this model is that it does not take in a

Limitation: Ignores the company's future dividend growth potential.


### Issues Encountered & Solutions

**Reading Tickers from File**: I had trouble accessing the tickers.txt from the Task 1 directory but I learned to use os.path.join to find the relative path and to also ensure that it works over different operating systems.

**Lambda Functions and Stock Splits**: It was not directly related to the main functionality of calculating the price momentum, but going over lambda function again because I had to account for there being no value for the 5 day period.

**Merging DataFrames**: The biggest challenge in this file was to make sure that all of the tickers got appened to the dataframe without overwriting the existing data. I decided to use a flag to add the first company's data directly into the DataFrame and then merge the next company's data on the 'Date' column. 
<!-- #endregion -->
