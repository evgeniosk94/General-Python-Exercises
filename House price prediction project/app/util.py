import json
import pickle
import pandas as pd
import numpy as np

__locations = None
__model = None


def get_estimated_price(location,sqft,bedroom,bath):
        if location not in __locations:
                return "Invalid Location"
        
        X = pd.DataFrame({
        'location': [location],  
        'total_sqft': [sqft],
        'bath': [bath],
        'bedroom': [bedroom]
    })
        return np.round(__model.predict(X),2)

def get_location_names():
        return __locations

def load_saved_artifacts():                     # This function will load the saved columns and the pickle model                   
        print("loading saved artifacts...start")                 
        global __locations                      # Global variables, will store the artifacts in these global variables
        
        with open("./artifacts/columns.json", 'r') as f:
                __locations = json.load(f)['locations']       # From the columns json file we get the data_columns key which will return all the data columns 
        
        global __model
        with open("./artifacts/house_prices_model.pickle", "rb") as f:  # Binary model so rb
                __model = pickle.load(f)
        print("loading saved artifacts...done")
        

if __name__ == '__main__':
        load_saved_artifacts()
        print(get_location_names())
        print(get_estimated_price('Indira Nagar',1000,3,3))
        print(get_estimated_price('Indira Nagar',1000,2,2))
        print(get_estimated_price('other',1000,2,2)) # other location
        print(get_estimated_price('other',1000,2,2)) # other location