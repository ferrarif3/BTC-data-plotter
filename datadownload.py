import pandas as pd
import requests

r = requests.get('https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_DAILY&symbol=BTC&market=CNY&apikey=demo').json()

data = r['Time Series (Digital Currency Daily)'] #I just need the data from this dictionary

dictio = {} #Create a new dictionary so I can store the exact data I need instead of the whole set

#I'm looking for just the data from 2017-11-XX
#So I filter it using a string slice and saving the data in the dictionary I created before
#The resulting format should look something like:
#{2017-11-30:{key:value, key:value}, 2017-11-29{key:value, key:value}, ...}

for i in data:
    if i[0:7] == '2017-11':
        dictio[i] = {}
        for k,v in r['Time Series (Digital Currency Daily)'][i].items():
            dictio[i][k] = v


dfr = pd.DataFrame.from_dict(dictio) #Get the dictionary with the data into a pandas dataframe

dfr.to_csv('dataNov2017.csv') #And then into CSV