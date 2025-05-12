import pandas as pd
import numpy as np
from sklearn.model_selection import ShuffleSplit, GridSearchCV, train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler, MinMaxScaler, OneHotEncoder
from sklearn.linear_model import LinearRegression, Lasso, Ridge
from sklearn.tree import DecisionTreeRegressor
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer

def get_linear_regression_model(X,y):
        # List your categorical and numerical columns
        categorical_cols = ['location']
        numerical_cols = ['total_sqft','bath','bedroom']
        
        # Preprocessing for numerical and categorical data
        preprocessor = ColumnTransformer([
                ('num', StandardScaler(), numerical_cols),
                ('cat', OneHotEncoder(drop='first', handle_unknown='ignore'), categorical_cols)
        ])
        
        '''
            handle_unknown='ignore': ensures that if an unknown location is passed later (during prediction), 
            it wont crash — the unknown will just get zeros in the one-hot encoding step.
            
        '''
        
        # Create pipeline with preprocessing + LinearRegression
        lr_pipeline = Pipeline([
                ('preprocessor', preprocessor),
                ('model', LinearRegression())
        ])
        
        # Split the data into train and test 
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=10)
        
        # Fit the model
        lr_pipeline.fit(X_train,y_train)
        
        # Linear regression score
        score = round(lr_pipeline.score(X_test,y_test),3)
        
        cv = ShuffleSplit(n_splits=5, test_size=0.2, random_state=10)
        scores = np.round(cross_val_score(lr_pipeline, X, y, cv=cv),3)
        avg_score = round(scores.mean(),3)
        
        return score,scores,avg_score
        

def get_model_params():
    # List your categorical and numerical columns
    categorical_features = ['location']
    numerical_features = ['total_sqft','bath','bedroom']    
    
    # Define transformers
    categorical_transformer = OneHotEncoder(drop='first')
    numerical_transformers = StandardScaler()

    # Combine into preprocessor
    preprocessor = ColumnTransformer(
        transformers=[
                ('num', numerical_transformers, numerical_features),
                ('cat', categorical_transformer, categorical_features)
        ])
        
    return {
        'linear_regression': {
            'model': Pipeline([
                ('preprocessor', preprocessor),
                ('model', LinearRegression())
            ]),
            'params': {
                'model__fit_intercept': [True,False],
                'preprocessor__num': [StandardScaler(), MinMaxScaler()],
            }
        },
        'lasso': {
            'model': Pipeline([
                ('preprocessor', preprocessor),
                ('model', Lasso())
            ]),
            'params' : {
                'model__alpha': [0.1,1,2],
                'model__selection': ['random', 'cyclic'],
                'preprocessor__num': [StandardScaler(), MinMaxScaler()],
            }
        },
        'ridge': {
            'model': Pipeline([
                ('preprocessor', preprocessor),
                ('model', Ridge()),
            ]),
            'params' : {
                'model__alpha': [0.1,1,2],
                'preprocessor__num': [StandardScaler(), MinMaxScaler()],
            }
        },
        "decision_trees": {
            "model": Pipeline([
                ('preprocessor', preprocessor),
                ('model', DecisionTreeRegressor(random_state=0))
            ]),
            "params": {
                "model__criterion": ['squared_error', 'friedman_mse'],
                "model__splitter": ["best", "random"],
                "model__max_depth": [None, 5, 10, 20]
            }
        }
    }


def train_and_select_best_model(X, y):
    model_params = get_model_params()
    cv = ShuffleSplit(n_splits=5, test_size=0.2, random_state=0)

    scores = []
    best_models = {}

    for model_name, model_parameters in model_params.items():
        clf =  GridSearchCV(estimator=model_parameters['model'], param_grid=model_parameters['params'], cv=cv, return_train_score=False)
        clf.fit(X, y)
        best_models[model_name] = clf.best_estimator_
        scores.append({
            'model': model_name,
            'best_score': clf.best_score_,
            'best_params': clf.best_params_
        })

    df_models = pd.DataFrame(scores, columns=['model', 'best_score', 'best_params'])
    best_model_name = df_models.sort_values('best_score', ascending=False).iloc[0]['model']
    best_model = best_models[best_model_name]

    return best_model, df_models