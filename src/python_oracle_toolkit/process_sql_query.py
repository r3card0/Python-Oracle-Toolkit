
# dependencies
from path_converter import PathConverter
from .get_connection_params import Params

# Libraries
import os
import cx_Oracle
import pandas as pd

class SqlQuery:
    def __init__(self,json_file:str,query:str,schema:str):
        # Getting connection parameters
        self.config = Params(json_file).read_connection_params()
        self.user = self.config.get("user")
        self.passw = self.config.get("password")
        self.connection_chain = self.config.get("connection")
        self.schema = schema
        self.query = PathConverter(query).to_wsl()
        self.sql = []


    def _evaluates_query_origin(self):
        if os.path.isfile(self.query):
            return True
        else:
            return False
        
    def reads_sql_file(self):
        convert_sql_filepath = self.query

        # open the file and append the sql statements as a list
        with open(convert_sql_filepath,"r",encoding="utf-8") as file:
            for line in file:
                self.sql.append(line)

        # convert the list to a string format
        sql_query = """""".join(self.sql)

        # returns string format
        return sql_query
    
    def _gets_sql(self):
        try:
            # if self.query is a file, then read it and extracts the sql script
            if self._evaluates_query_origin() == True:
                get_query = self.reads_sql_file()
                return get_query
            else:
                # if self.query is a variable, then pass it
                return  self.query
        except Exception as e:
            print(f"Failure to load SQL: {e}")

    def create_dataframe(self):
        # establishing connection to Oracle
        try:
            connection = cx_Oracle.connect(self.user,self.passw,self.connection_chain)
            print("Database connection successfully established")
            # creating cursor
            cursor = connection.cursor()
            print("Cursor successfully created")
        except cx_Oracle.Error as e:
            print(f"Oracle's error connection: {e}")

        # Connect to a Pluggable Database
        try:
            if self.schema == None:
                print("Welcome to Oracle")
            else:
                cursor.execute(f"ALTER SESSION SET CURRENT_SCHEMA = {self.schema}")
                print(f"Welcome to '{self.schema}' session")
        except Exception as e:
            print(f"Failure to connect to schema '{self.schema}: {e}'")

        # Reads SQL script
        get_query = self._gets_sql()

        # Creates Dataframe
        try:
            print("Starting create dataframe . . .")
            df_pre = pd.read_sql_query(get_query,connection)
            df = df_pre.copy(deep=True)
            print("Dataframe successfully created.")
            _records = df.shape[0]
            _columns = df.shape[1]
            print(f"Result: {_records} records extracted and {_columns} columns")
        except Exception as e:
            print(f"Failure to create the Dataframe: {e}")

        # Close Connection
        finally:
            try:
                connection.close()
                print("Oracle database closed successfully.")
            except Exception as e:
                print(f"Failure to close connection: {e}")

        return df