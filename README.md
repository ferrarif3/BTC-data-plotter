# BTC-data-plotter
Scripts for downloading daily (historical) BTC prices and plotting the data using Pandas.

For now, datadownload.py just downloads the data for Nov, 2017 from the endpoint located at https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_DAILY&symbol=BTC&market=CNY&apikey=demo and puts the data into a CSV file.

Dataplotter.py parses the data to give you the daily open and closing prices for each day of the month. Additionally, it prints the average difference between the open and closing price for all days.
