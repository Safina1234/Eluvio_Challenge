''' Safina Nganga
Eluvio Chllenge 
This project is in regards to predictive modelling on the following data
 file (Eluvio_DS_Challenge) this is used to predict number of up_votes
 can increase'''

import pandas as pd
import matplotlib.pyplot as plot

''' This is piece of code filters out data that belongs to the
author polar to compare the number of up_votes from 2008-2016'''
 

data = pd.read_csv("Eluvio_DS_Challenge.csv", 
                   index_col="author")
rows=data.loc[["polar"]]
print((rows))



''' This piece of code is used to get the mean
of up_votes from every author''' 

data = pd.read_csv("Eluvio_DS_Challenge.csv")
mean_Average=data['up_votes'].mean()
print((mean_Average))

''' this piece of code is used to compare the number of up_votes
at the month of January in 2008 and the month of January in 2016
as per the data the total number of up_votes is higher in January
2016 as compared to January 2008 as the time created is increased'''

data = pd.read_csv("Eluvio_DS_Challenge.csv", 
                   index_col="date_created")
rows=data.loc[["2008-01-28","2016-01-30"]]
print(rows)

''' this piece of code is used to graph the up_votes against
the time_created. As per the graph the more time_created, the 
number of up_votes increases. This graph predicts that the more
time a person takes to create news content, the more up_votes
that person will get.'''


data = pd.read_csv("Eluvio_DS_Challenge.csv")
data.plot.scatter(x='time_created', y='up_votes', 
                  title='Up_Votes vs Time_Created')
plot.show(block=True)





