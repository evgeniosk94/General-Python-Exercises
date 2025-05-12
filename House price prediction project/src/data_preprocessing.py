import pandas as pd

def load_and_preprocess(filepath):
        # Load the cleaned dataset
        df = pd.read_csv(filepath)
        
        # Get unique locations
        unique_locations = df['location'].unique().tolist()
        
        # Transform location column into 0,1, drop the first to avoid dummy variable trap (perfect multicollinearity in linear models)
        # dummies = pd.get_dummies(df.location, drop_first=True)
        
        # Add original df and dummies in the same dataframe and Drop the location column since location was previously dummied
        # df = pd.concat([df,dummies], axis=1).drop(["location"], axis=1)
        
        # Create the X and Y variables 
        X = df.drop('price', axis=1)
        y = df.price
        
        return X,y, unique_locations