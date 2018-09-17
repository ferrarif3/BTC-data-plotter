# BTC-data-plotter
Scripts for downloading daily (historical) BTC prices and plotting the data using Pandas.

Datadownload.py downloads the data from the endpoint located at https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_DAILY&symbol=BTC&market=CNY&apikey=demo and puts that data into a CSV file. Asks the user for month and year they want to pull data for.

Dataplotter.py parses the data pulled with the datadownload.py script to give you the daily open and closing prices for each day of the month. Additionally, it prints the average difference between the open and closing price for all days. Asks the user for the file they want to parse, and if that file isn't found it exits instead.
