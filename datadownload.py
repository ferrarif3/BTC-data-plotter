import pandas as pd
import requests

r = requests.get('https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_DAILY&symbol=BTC&market=CNY&apikey=demo').json()

data = r['Time Series (Digital Currency Daily)'] #I just need the data from this dictionary

dictio = {} #Create a new dictionary so I can store the exact data I need instead of the whole set

#Ask for year and month. If user inputs a month/year where there was no data, the resulting CSV won't have anything
year = int(input('Input the year you want to pull the data from, in YYYY format: '))
month = int(input('Input the month you want to pull the data from, in MM format: '))

#Filter it using a string slice for the year and month and saving the data in the dictionary I created before
#The resulting format should look something like:
#{2017-11-30:{key:value, key:value}, 2017-11-29{key:value, key:value}, ...}

for i in data:
    if i[0:7] == '{}-{num:02d}'.format(year, num=month): #Adds leading 0 in case of single digit month
        dictio[i] = {}
        for k,v in r['Time Series (Digital Currency Daily)'][i].items():
            dictio[i][k] = v


dfr = pd.DataFrame.from_dict(dictio) #Get the dictionary with the data into a pandas dataframe

dfr.to_csv('data{num:02d}{}.csv'.format(year, num=month)) #And then into CSV