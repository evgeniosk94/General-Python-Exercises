# Import necessary packages
import pandas as pd 
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import ShuffleSplit
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV

from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.pipeline import Pipeline

from sklearn.linear_model import LinearRegression, Lasso, Ridge
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor

# Load the cleaned dataset
df = pd.read_csv('C:/Users/eugen/Desktop/Repo/General Python Exercises/House price prediction project/data/cleaned_data.csv')

# Transform location column into 0,1, drop the first to avoid dummy variable trap (perfect multicollinearity in linear models)
dummies = pd.get_dummies(df.location, drop_first=True)

# Add original df and dummies in the same dataframe 
df2 = pd.concat([df,dummies], axis=1)

# Drop the location column since location was previously dummied
df3 = df2.drop(["location"], axis=1)

# Create the X and Y variables 
X = df3.drop('price', axis=1)
y = df3.price

# Split the data into train and test 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=10)

# Create a liner regression model 
lr_clf = LinearRegression()
lr_clf.fit(X_train,y_train)
print("Linear regresion model score:",round(lr_clf.score(X_test,y_test),3))

cv = ShuffleSplit(n_splits=5, test_size=0.2, random_state=10)

scores = cross_val_score(LinearRegression(), X, y, cv=cv)
print(f"Linear regression scores with cross validation: {np.round(scores,3)}")
print(f"Linear regression cross validation average score: {round(scores.mean(),3)}")

# Grid search CV and hyperparameter tuning for best model selection
model_params = {
    'linear_regression': {
        'model': Pipeline([
            ('scaler', StandardScaler()),
            ('model', LinearRegression())
        ]),
        'params': {
            'model__fit_intercept': [True,False],
            'scaler': [StandardScaler(), MinMaxScaler()]
        }
    },
    'lasso': {
        'model': Pipeline([
            ('scaler', StandardScaler()),
            ('model', Lasso())
        ]),
        'params' : {
            'model__alpha': [0.1,1,2],
            'model__selection': ['random', 'cyclic'],
            'scaler': [StandardScaler(), MinMaxScaler()]
        }
    },
    'ridge': {
        'model': Pipeline([
            ('scaler', StandardScaler()),
            ('model', Ridge()),
        ]),
        'params' : {
            'model__alpha': [0.1,1,2],
            'scaler': [StandardScaler(), MinMaxScaler()]
        }
    },
    # 'random_forest': {
    #     'model': RandomForestRegressor(random_state=0),
    #     'params' : {
    #         'n_estimators': [50,100],
    #         'criterion': ["squared_error"]
    #     }
    # },
    "decision_trees": {
        "model": DecisionTreeRegressor(random_state=0),
        "params": {
             "criterion": ['squared_error', 'friedman_mse'],
             "splitter": ["best", "random"],
             "max_depth": [None,5,10,20]    
        }
    }
}

scores = []
best_models = {}
cv = ShuffleSplit(n_splits=5, test_size=0.2, random_state=0)

for model_name, model_parameters in model_params.items():
    clf =  GridSearchCV(model_parameters['model'], model_parameters['params'], cv=cv, return_train_score=False)
    clf.fit(X,y)
    best_models[model_name] = clf.best_estimator_
    scores.append({
        'model': model_name,
        'best_score': clf.best_score_,
        'best_params': clf.best_params_
    })
    
df_models = pd.DataFrame(scores,columns=['model','best_score','best_params'])
pd.set_option('display.max_colwidth',500)
print("Models and best parameters",df_models)

best_model_name = df_models.sort_values('best_score', ascending=False).iloc[0]['model']
best_model = best_models[best_model_name]
print("Best model selection:",best_model)

# Define models
linear_model = best_models['linear_regression']
lasso_model = best_models['lasso']
ridge_mdoel = best_models['ridge']
decision_tree_model = best_models['decision_trees']
#random_forest_model = best_models['random_forest']

# Model predictions
def predict_price(location,sqft,bath,bedroom):
        loc_index = np.where(X.columns==location)[0][0]
        
        x = np.zeros(len(X.columns))
        x[0] = sqft
        x[1] = bath
        x[2] = bedroom
        if loc_index >=0:
                x[loc_index] = 1
                
        # Create DataFrame with same columns
        x_df = pd.DataFrame([x], columns=X.columns)
        
        return linear_model.predict(x_df)[0]   # Replace best_model with any other model i.e., linear_model or lr_clf

print("Price for 1st Phase JP Nagar and 1000 sqft, 2 bath and 2 bedroom is:",float(predict_price('1st Phase JP Nagar', 1000, 2, 2)))
print("Price for 1st Phase JP Nagar and 1000 sqft, 2 bath and 3 bedroom is:",float(predict_price('1st Phase JP Nagar', 1000, 2, 3)))
print("Price for Indira Nagar and 1000 sqft, 2 bath and 2 bedroom is:",float(predict_price('Indira Nagar', 1000, 2, 2)))
print("Price for Indira Nagar and 1000 sqft, 3 bath and 3 bedroom is:",float(predict_price('Indira Nagar', 1000, 3, 3)))
print("Price for other and 1000 sqft, 2 bath and 2 bedroom is:",float(predict_price('other', 1000, 2, 2)))