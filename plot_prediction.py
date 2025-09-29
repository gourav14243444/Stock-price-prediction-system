"""

@author: Cody Smith | codysmith.contact@gmail.com
https://github.com/codysmith-tech
https://www.linkedin.com/in/codysmithprofile/

"""

import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')

def plot(df):
    """
    Plots the data and predicted data.

    Parameters
    ----------
    df : Pandas DataFrame
        DF that is to be plotted

    Returns
    -------
    None.

    """
    
    #Plotting known data
    df['ClosePrice'].plot()
    
    #Plotting predicted data
    df['ForecastPrice'].plot()
    
    #Legend
    plt.legend(loc='best')
    
    #Labels
    plt.title('GME Stock Price Prediction')
    plt.xlabel('Date')
    plt.ylabel('Price')
    
    #Showing fig
    plt.show()