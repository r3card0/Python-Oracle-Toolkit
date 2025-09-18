from modify_file_path import ModifyFilePath
import json

class Params:
    def __init__(self,json_file:str):
        self.filepath = json_file
        self.connection_file = ModifyFilePath(self.filepath).convert_filepath()

    # Class Method: Reads json file and returns a dictionary with connection parameters
    def read_connection_params(self):
        try:
            with open(self.connection_file,'r') as config_file:
                config = json.load(config_file)
                return config.get('oracle',{})
        except FileNotFoundError as e:
            print(f"Error: File not found")
            return {e}
        
    # Establish connection
    def connect(self):
        # load connection params
        config = self.read_connection_params()
        user = config.get("user")
        passw = config.get("password")
        connection_chain = config.get("connection")
        params = (user,passw,connection_chain)
        return params