"""

@author: Cody Smith | codysmith.contact@gmail.com
https://github.com/codysmith-tech
https://www.linkedin.com/in/codysmithprofile/

"""

import numpy as np
from sklearn import preprocessing

def preprocess(df, forecast_time):
    """
    This function preprocesses the data by creating features
    and labels and scaling the data

    Parameters
    ----------
    df : Pandas DataFrame
        DF to create features and labels from
    forecast_time : int
        Number of days to forecast out

    Returns
    -------
    X : np.array
        Array of data features
    y : np.array
        Array of data labels
    X_forecast : np.array
        Array of data to predict against

    """
    
    #Setting features
    X = np.array(df.drop(['label'], axis=1))
    
    #Scaling features for processing speed & accuracy
    X = preprocessing.scale(X)
    X = X[:-forecast_time]
    
    #Setting data to predict against
    X_forecast = X[-forecast_time:]
    
    #Setting labels
    df.dropna(inplace=True)
    y = np.array(df['label'])

    
    return X, y, X_forecast