# import libraries
import cx_Oracle
import os
import pandas as pd

# import classes
from get_connection_params import Params
from process_sql_query import SqlQuery

def create_dataframe(json_file:str,query:str,schema:str):
    # Getting connection parameters
    config = Params(json_file).read_connection_params()
    user = config.get("user")
    passw = config.get("password")
    connection_chain = config.get("connection")

    
    # Establishing connection to Oracle
    try:
        connection = cx_Oracle.connect(user,passw,connection_chain)
        print("Database connection successfully established")
        # Creating cursor
        cursor = connection.cursor()
        print("Cursor successfully created")
    except cx_Oracle.Error as e:
        print(f"Oracle's error connection: {e}")

    # Connect to a PDB
    try:
        if schema == None:
            print("Welcome to Oracle")
        else:
            cursor.execute(f"ALTER SESSION SET CURRENT_SCHEMA = {schema}")
            print(f"Welcome to '{schema}' session")

    except Exception as e:
        print(f"Failure to connect to schema '{schema}': {e}")

    # Reads SQL script
    get_query = SqlQuery(query).gets_sql()

    # Create Dataframe
    try:
        df_pre = pd.read_sql_query(get_query,connection)
        df = df_pre.copy(deep=True)
        print("Dataframe successfully created.")
        # return df
    except Exception as e:
        print(f"Failure to create the Dataframe: {e}")
    
    # close connection
    finally:
        try:
            connection.close()
            print("Oracle database closed successfully.")
        except Exception as e:
            print(f"Failure to close connection: {e}")
            
    return df