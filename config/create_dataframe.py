# import libraries
import cx_Oracle
import os
import pandas as pd

# import classes
from get_connection_params import Params

def create_dataframe(json_file:str,query:str,schema:str):
    params = Params(json_file).connect()
    
    # Establishing connection to Oracle
    try:
        connection = cx_Oracle.connect(params)
        print("Database connection successfully established")
    except cx_Oracle.Error as e:
        print(f"Oracle's error connection: {e}")

    # Create cursor
    try:
        cursor = connection.cursor()
        print("Cursor successfully created")
    except Exception as e:
        print(f"Failure to create cursor: {e}")

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
    # Evaluates if query is comming from a file

    # Create Dataframe
    # Close connection