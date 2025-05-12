import pandas as pd
import pickle
import json
from data_preprocessing import load_and_preprocess
from model_training import train_and_select_best_model
from model_training import get_linear_regression_model
from prediction import predict_price

pd.set_option('display.max_colwidth',500)

def main():
        print()
        print("Calculating linear regression model...start")
        print()
        X, y, data_columns = load_and_preprocess('../data/cleaned_data.csv')
        lr_score, lr_cross_val_score, lr_cross_val_avg_score = get_linear_regression_model(X,y)
        print("Linear regression score:", lr_score)
        print("Linear regression cross val score:", lr_cross_val_score)
        print("Linear regression cross val average score:", lr_cross_val_avg_score)
        print()
        print("Calculating linear regression model...done")
        print()
        
        print("Calculating hyper-parameter tuning and best model selection...start")
        print()
        best_model, df_models = train_and_select_best_model(X,y)
        print("Models and best parameters",df_models)
        print("Best model selected",best_model)
        print()
        print("Calculating hyper-parameter tuning and best model selection...done ")
        print()
        
        with open('../models/house_prices_model.pickle', 'wb') as f:
                pickle.dump(best_model,f)
                
        columns = {
                'data_columns': [x.lower() for x in data_columns]
                }
        with open("../models/columns.json","w") as f:
                json.dump(columns,f)
        
        location = 'Indira Nagar'
        sqft = 1000
        bath = 2
        bedroom = 2
        predicted_price = predict_price(best_model, location, sqft, bath, bedroom)
        print(f"Predicted price for: {location} is {predicted_price:.2f}")
        
if __name__ == "__main__":
        main()