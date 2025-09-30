


import math
import sql
from preprocess import preprocess
from fit_predict import fit_predict
from plot_prediction import plot

def main():
    """
    This is the main script for this project. This calls on all other scripts
    and handles some small cleaning tasks.

    Returns
    -------
    None.

    """
    #Connecting to DB
    conn, c = sql.connect_db('GMEstock.db')
    
    #Checking DB data
    sql.check_db(c)
    
    #Reading data from DB into DataFrame
    gme_stock = sql.read_from_db('SELECT Date, ClosePrice FROM GMEstock', conn)
    print("DataFrame head:")
    print(gme_stock.head())
    print("-----------------------------------------------------------------")
    
    #Disconnecting fom DB
    sql.disconnect_db(c, conn)
    
    #Replacing bad data
    gme_stock.fillna('-1000000', inplace=True)
    
    #Setting the amount of time to forecast out to be 1% of total data length
    forecast_out = int(math.ceil(0.01*len(gme_stock)))
    print("Number of days to forecast out:", forecast_out)
    print("-----------------------------------------------------------------")
    
    #Shifting column to see predicted close price
    gme_stock['label'] = gme_stock['ClosePrice'].shift(-forecast_out)
    
    #Preprocessing & splitting into training and testing data
    X, y, X_forecast = preprocess(gme_stock, forecast_out)
    
    #Fitting linear regression, predicting future values, and finding confidence
    gme_stock, confidence = fit_predict(gme_stock, X, y, X_forecast)
    print("Confidence score of linear regression:", confidence)
    print("-----------------------------------------------------------------")
    
    #Plotting
    plot(gme_stock)

if __name__ == "__main__":
    main()
