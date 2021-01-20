# CovidTracking

`Tracking.py` can be run from the command line. The user has the option to examine the number of positive tests that a certain state has had, or the number of Covid-19 related deaths that state has had. The program will then print out the total cases, the new cases for the day, and provide a graph showing the trend of the cases/deaths in that state since the data started being collected. The data was collected from "https://api.covidtracking.com/v1/states/daily.csv"

There are three command line arguments the user needs to know about:
1. State Abbreviation
2. Statistic of choice (either 'positive' or 'death')
3. Whether to update the data (True if you want the most up to date data, False if you want the most recently loaded dataset). False is the default option if nothing is input. 
       
 For example, if someone wanted to view the most up to date death totals in Washington D.C. they would type the following on the command line:
 *python Tracking.py DC death True*
 
 If the wanted to view the number of positive test cases in Massachusetts, they would type:
 *python Tracking.py MA positive*

`DataRetrieval.py` holds the functions used for updating, loading, and graphing the Covid-19 data
`Covid19_Tracking/data` holds a file called `RecentData.csv` which is where the most recent data is stored (overwritten when updated)

# Covid Notebook

The notebook `CovidTracking.ipynb`is there to walk you through some analysis I did with the data. There are 4 basic sections:
1. Basic understanding of what the data looks like, how to update and load the data, and how to visualize it
2. Some analysis of the data looking at how the number of positive cases and number of deaths in a state are correlated
3. I used a polynomial regression to model the number of deaths in MA and predict what death totals will be as cases increase
4. I used a LSTM algorithm to model the deaths in MA. This time I used a test set to look at accuracy, because this was my first analysis of time series data
    
`ctp.py` simply holds the functions to update, load, and graph Covid-19 data. They are slightly different for the notebook
