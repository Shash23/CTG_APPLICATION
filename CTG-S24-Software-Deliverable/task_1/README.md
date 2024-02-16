# Data Access and Interpretation Guide
This document is paired with **data_collection.py**.This document explains accessing, interpreting and issues that arose from implementing this file

### Accessing the Data
The data came from the ticker list provided by the interviewer. Each line in the file represents a unique stock ticker. 

**Data Extraction**: This script uses the yfinance library to get historical financial data for each ticker. 

**Data Storage**: The extracted data is stored in an individual csv with the format {ticker}.csv. 

**Adjusted Close Calculation**: Since the adjusted close did not appear in the historical data, I had to find sources for the formula and calculate it using the method I wrote 'calculate_adjusted_close'.

The data is stored at task_1/data/{ticker.csv}

## Interpreting the Data
Each CSV file contains historicald data including Open, High, Low, Close, Volume, Dividends, Stock Splits, and the calculated Adjusted Close prices. The data is over 2 years. 

## Issues Encountered & Solutions
**Reading Tickers from File**: I ran into an issue where I could not properly strip newline characters because I thought it was trim() not strip(). 

**Calculating Adjusted Close**: The main challenge I ran into was calculating 'Adjusted Close'. I thought that it would come with the historical data but it did not. Another problem I ran into in relation to this one was calculating when the 'Stock Split' value was zero. I understood that if the 'Stock Split' value was 0, then it could result in a runtime error: ZeroDivisionError. 

I handled this by applying a lambda function to see if the Stock Splits value was zero. If it was, then it just added the dividends to the close price but if it was not, then it would carry out the calculation for the adjusted close.

```python

```
