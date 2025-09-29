# GME-stock-predictions

@author: Cody Smith | codysmith.contact@gmail.com

https://github.com/codysmith-tech

https://www.linkedin.com/in/codysmithprofile/

------------------------
***OVERVIEW***

A Python project using SQL and Machine Learning to predict future close prices of the infamous GameStop stock.

This uses an SQL database that I created and is included in the files for this project. A linear regression model is used to predict future closing prices.

------------------------
***GETTING STARTED***

This project was made in a Windows OS.
This project was made in Python 3.8.8.
This project was made in the Anaconda environment.
*Download Anaconda here*
https://www.anaconda.com/products/individual

Please use this setup for best results.

Modules needed for this project:

	sqlite3

	pandas

	matplotlib

	numpy

	math

	datetime

	sklearn
  
------------------------
**Files:**

main.py - master file for running all other files and basic data cleaning

sql.py - contains functions necessary for querying database

preprocess.py - preprocesses and gets data ready for applying the linear regression model

fit_predict.py - fits data to linear regression model and makes prediction based on that model

plot_prediction.py - plots data and predicted data

------------------------
**RESULTS DISCUSSION**

To run this project, open main.py and press run. The final graph will pop up after a moment of processing.

Taking a look at the console, we can see that the first thing printed is:
 
    SQL Table Column names:
    ['Date', 'OpenPrice', 'HighPrice', 'LowPrice', 'ClosePrice', 'AdjClosePrice', 'Volume']
    
This was done to take a look at what the data the SQL DB holds.
We don't need all of this data; we're mostly interested in the 'ClosePrice' and the associated 'Date'.

So, the DB was queried and the appropriate data was saved into a Pandas DataFrame.
We can see the head of the DataFrame as the next thing printed in the console:

    DataFrame head:
                ClosePrice
    Date                  
    2002-02-13      10.050
    2002-02-14      10.000
    2002-02-15       9.950
    2002-02-19       9.550
    2002-02-20       9.875
    
This is the data that is having a linear regression model applied to it. The model is set up to predict 1% of the length of the data out.
This is the next thing printed:

    Number of days to forecast out: 51
    
The data is split into testing and training subsets on loop until the confidence of the linear regression model fit is at least 85%.
This is now printed:

    Confidence score of linear regression: 0.8669978085311427
    
Only slightly above 85% confidence is about the best this model can do.
Here is the predicted data for this confidence:

![GME_stock_predictions](https://user-images.githubusercontent.com/58944210/147838872-3da09014-de7e-4b33-9588-6c5533ae4414.png)

So, predictions were successfully made, but 85% isn't a confidence I recommend making investments on. Perhaps a different model would have a higher confidence.
