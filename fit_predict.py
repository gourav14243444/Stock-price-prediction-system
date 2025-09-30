

import datetime
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

def fit_predict(df, X, y, X_forecast):
    """
    Function to split into training and testing subset, loops until confidence
    is sufficient, fits a linear regression, and predicts future values.

    Parameters
    ----------
    df : Pandas DataFrame
        DF to add predicted values into
    X : np.array
        Array of data features
    y : np.array
        Array of data labels
    X_forecast : np.array
        Array of data to predict against

    Returns
    -------
    df : Pandas DataFrame
        DF with predicted values for plotting
    confidence : int
        An integer from 0.0-1.0 to determine confidence score of regression
        fit.

    """
    
    while True:
        #Splitting arrays into random training and testing subsets (80/20 split)
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    
        #Instatiating classifier
        clf = LinearRegression(n_jobs=-1)
        
        #Fitting linear model to trained data
        clf.fit(X_train, y_train)
        
        #Scoring (Max value 1.0)
        confidence = clf.score(X_test, y_test)

        #Looping until suffiecient confidence
        if confidence > 0.85:
            break
    
    #Predicting future values
    forecast_set = clf.predict(X_forecast)
    
    #Adding predicted values to DataFrame
    df['ForecastPrice'] = np.nan
    
    #Finding last date and adding a day to it for prediction starting point
    last_date = df.iloc[-1].name
    last_unix = last_date.timestamp()
    one_day = 86400
    next_unix = last_unix + one_day
    
    #Adding dates for all predictions
    for i in forecast_set:
        next_date = datetime.datetime.fromtimestamp(next_unix)
        next_unix += one_day
        df.loc[next_date] = [np.nan for _ in range(len(df.columns)-1)] + [i]
        
    return df, confidence
