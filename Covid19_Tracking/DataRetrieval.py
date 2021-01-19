
def LoadCTPData(update_first=False):
    """Return the most recent copy of our CTP data as a DataFrame and apply
        necessary preprocessing
    
        If update_first = True, then call UpdateCovidTracking() first..."""
    
    import pandas as pd
    from datetime import datetime as dt
    import requests
    import io

    file_name = "./data/RecentData.csv"

    if update_first:
        #UpdateCovidTracking()
        # Url for data
        url = "https://api.covidtracking.com/v1/states/daily.csv"

        # get new data
        urlData = requests.get(url).content
        df = pd.read_csv(io.StringIO(urlData.decode('utf-8')))

        with open(file_name, "wb") as f:
            f.write(urlData)
        
        # Tell user new data retrieved
        print("New Data Retrieved")
    
    else:
        # Load the most recent data saved on the computer
        df = pd.read_csv(file_name)

        # Inform user the data has been loaded
        print("Data Loaded")
        
    # Extract Columns we want
    cols = ['date', 'state', 'positive', 'death']
    df_filtered = df[cols].copy()
    
    # Fix Dates and set them as the index
    date_format = '%Y%m%d'
    df_filtered.date = df_filtered.date.apply(lambda d: dt.strptime(str(d), date_format))
    df_filtered.index = df_filtered.date
    df_filtered = df_filtered.drop(columns=['date'])
    
    # Return the filtered data
    return df_filtered


def ShowCovidTracking(state, metric, update_first=False):
    """ Call LoadCTPData to load the data and then plot the results for the
        state and metric ("death" or "positive") of deaths or positive cases
        since data started being collected

        Also prints out the number of total deaths/positive cases and the amount
        of new deaths/positive cases for the day
    """

    import matplotlib.pyplot as plt
    
    # Load the data
    df = LoadCTPData(update_first)
    
    # get state data
    idx_state = df.state == state
    df_current_state = df[idx_state].copy()

    
    # Print the total number of cases
    new_cases = df_current_state[metric][0] - df_current_state[metric][1]
    
    if metric == "death":
        print("\nTotal COVID-19 deaths in " + state + ": " + str(int(df_current_state[metric][0])))
        print("New COVID-19 deaths in " + state + " in the past day: " + str(int(new_cases)))
    else:
        print("\nTotal COVID-19 positive cases in " + state + ": " + str(int(df_current_state[metric][0])))
        print("New COVID-19 positive cases in " + state + " today: " + str(int(new_cases)))

    # Make the plot!
    plt.figure(figsize=(12,6))
    plt.plot(df_current_state[metric], color='blue')
    plt.xticks(rotation=45)
    if metric == "death":
        plt.ylabel("Deaths")
        plt.title("Covid-19 related deaths in " + state)
    else:
        plt.ylabel("Positive Cases")
        plt.title("Covid-19 positive cases in " + state)
    plt.show()
    
      


