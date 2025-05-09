import numpy as np
import pandas as pd

def predict_price(model, location, sqft, bath, bedroom):
    # Create a DataFrame for the new sample, with the same column names as the original dataset
    X_new = pd.DataFrame({
        'location': [location],  # Pass the location as a string
        'total_sqft': [sqft],
        'bath': [bath],
        'bedroom': [bedroom]
    })
    
    # Use the trained model to make the prediction (model handles preprocessing automatically)
    prediction = model.predict(X_new)
    
    
    return prediction[0] # Replace model with any other model i.e., linear_model or lr_clf