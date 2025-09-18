# Esta clase evalua el origen del SQL
# Este puede ser un archivo o estar definido en una variable
# Dependiendo del origen, es el proceso que entra en accion para que lo retorne de forma que pueda ser usado por la funcion 

from modify_file_path import ModifyFilePath
import os

class SqlQuery:
    def __init__(self,query:str):
        self.query = query
        self.sql = []

    def evaluates_query_origin(self):
        if os.path.isfile(self.query):
            return True
        else:
            return False
        
    def reads_sql_file(self):
        convert_sql_filepath = ModifyFilePath(self.query).convert_filepath()

        # open the file and append the sql statements as a list
        with open(convert_sql_filepath,"r",encoding="utf-8") as file:
            for line in file:
                self.sql.append[line]

        # convert the list to a string format
        sql_query = """""".join(self.sql)

        # returns string format
        return sql_query
    
    def gets_sql(self):
        try:
            # if self.query is a file, then read it and extracts the sql script
            if self.evaluates_query_origin() == True:
                get_query = self.reads_sql_file()
                return get_query
            else:
                # if self.query is a variable, then pass it
                return  self.query
        except Exception as e:
            print(f"Failure to load SQL: {e}")