import pandas as pd

file = input('Input the name of the file you want to see the data from: ')


def plot(dataframe):
    day = dataframe.keys()[0]  # Sets 'day' as the first column (last day) of the month
    day = int(day[8:10])  # Day counter, gets the last day of the month (31,30,28 or 29) as a string, converts it to int

    month = dataframe.keys()[0]
    month = month[5:7]  # Gets the month number as a string

    year = dataframe.keys()[0]
    year = year[0:4]  # Gets the year number as a string

    avg = 0  # Average counter, always starts at 0

    print('Values for {}-{}:\n'.format(month, year))
    # For every value in the row (1 for each day), get the open and close price in USD and print them.
    # '{num:02d}'.format(num=day)])' adds a leading 0 to single digit numbers for the days
    for i in dataframe.loc['1b. open (USD)']:
        print('Open price for {num:02d}-{}-{}: {}'.format(day, month, year,
                                                          dataframe.loc['1b. open (USD)', '{}-{}-{num:02d}'.format(
                                                              year, month, num=day)], num=day))

        print('Close price for {num:02d}-{}-{}: {}\n----'.format(day, month, year,
                                                                 dataframe.loc[
                                                                     '4b. close (USD)', '{}-{}-{num:02d}'.format(
                                                                         year, month, num=day)], num=day))

        avg += ((dataframe.loc['1b. open (USD)', '{}-{}-{num:02d}'.format(year, month, num=day)]) -
                (dataframe.loc['4b. close (USD)', '{}-{}-{num:02d}'.format(year, month, num=day)]))

        day -= 1

    avg = avg / 30  # Calculate the average
    print(
        'The average between the opening and closing price for {}-{} is: {}'.format(month, year,
                                                                                    avg))  # Print the average


try:
    dfr = pd.read_csv('{}'.format(file), index_col=0)  # Open the CSV as a dataframe and set the index column as 0
    plot(dfr)
except FileNotFoundError:
    print('File not found, exiting.')
