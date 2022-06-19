import traceback
import os, sys

class ConfigurationHandler():

    def __init__(self):
        # define variables that you want to fetch and set from configuration service. Only use A-Z and _ in names.

        self.API_BACKEND_URL = None
        self.DB_CONN_STRING = None
        self.INTERNAL_API_TOKEN = None 
        self.JWT_SECRET = None
        self.JWT_ALGORITHM = None
        self.set_configuration_values()
        
    def set_configuration_values(self):
        self.API_BACKEND_URL = self.load_env_value(key="API_BACKEND_URL")
        self.DB_CONN_STRING = self.load_env_value(key="DB_CONN_STRING")
        self.INTERNAL_API_TOKEN = self.load_env_value(key="INTERNAL_API_TOKEN")
        self.JWT_ALGORITHM = self.load_env_value(key="JWT_ALGORITHM")
        self.JWT_SECRET = self.load_env_value(key="JWT_SECRET")
    
    def load_env_value(self,key):
        try:
            return  os.environ[key]
        except Exception as e: 
            #print exception to screen 
            traceback.print_exc() 
            raise RuntimeError(f"Failed to load env variable:{key}")





        


