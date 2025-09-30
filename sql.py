
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt


def connect_db(path):
    """
    This function connects to the SQL database.

    Parameters
    ----------
    path : str
        A string of a path to the SQL DB.

    Returns
    -------
    connection : Connection object
        SQLite3 Connection
    cursor : Cursor object
        SQLite3 Cursor

    """

    #Connecting to DB
    connection = sqlite3.connect(path)
    cursor = connection.cursor()
    
    return connection, cursor

def disconnect_db(cursor, connection):
    """
    Disconnects from the SQL database.

    Parameters
    ----------
    cursor : Cursor object
        SQLite3 Cursor
    connection : Connection object
        SQLite3 Connection

    Returns
    -------
    None.

    """
    
    #Disconnecting from DB
    cursor.close()
    connection.close()



def check_db(cursor):
    """
    Reads the SQL database and prints column names.

    Parameters
    ----------
    cursor : Cursor object
        SQLite3 Cursor

    Returns
    -------
    None.

    """
    
    #SQL Query to check what data DB holds
    cursor.execute('SELECT * FROM GMEstock')
    
    #Getting the names of columns from DB
    names = [description[0] for description in cursor.description]
    
    #Printing names
    print("SQL Table Column names:")
    print(names)
    print("-----------------------------------------------------------------")
    

def read_from_db(query, connection):
    """
    Reads from the DB and saves as Pandas DataFrame

    Parameters
    ----------
    query : str
        A string of the desired SQL query.
    connection : Connection object
        SQLite3 Connection
    

    Returns
    -------
    df : Pandas DataFrame
        A Pandas DF created from the data in the SQL database.

    """
    
    #SQL Query to read data into DataFrame
    df = pd.read_sql_query(query, connection, index_col='Date')
    
    #Converting queried data into integers from strings
    df = df.apply(pd.to_numeric, errors='coerce')
    
    #Turning index into datetime objects
    df.index = pd.to_datetime(df.index)

    return df
