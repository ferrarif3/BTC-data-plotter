import pandas as pd

dfr = pd.read_csv('dataNov2017.csv', index_col=0) #Open the CSV as a dataframe and set the index column as 0

day = 30 #Day counter
avg = 0 #Average counter

#For every value in the row (1 for each day), get the open and close price in USD and print them.
#'2017-11-{num:02d}'.format(num=day)]) adds a leading 0 to single digit numbers for the days
for i in dfr.loc['1b. open (USD)']:
    print('Open price for Nov. {}, 2017: {}'.format(day, dfr.loc['1b. open (USD)','2017-11-{num:02d}'.format(num=day)]))
    print('Close price for Nov. {}, 2017: {}'.format(day, dfr.loc['4b. close (USD)','2017-11-{num:02d}'.format(num=day)]))
    avg += ((dfr.loc['1b. open (USD)','2017-11-{num:02d}'.format(num=day)]) -
            (dfr.loc['4b. close (USD)','2017-11-{num:02d}'.format(num=day)]))
    day -= 1

avg = avg/30 #Calculate the average
print('The average between the opening and closing price for Nov. 2017 is: {}'.format(avg)) #Print the average


