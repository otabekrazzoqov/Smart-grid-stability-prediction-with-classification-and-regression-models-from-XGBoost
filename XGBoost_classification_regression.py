
import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split

from xgboost import XGBClassifier, XGBRegressor

data = pd.read_csv("/github repos/SMART GRID STABILITY/smart_grid_stability_augmented.csv")

data.info()





#  PREPROCESSING

def preprocess_inputs(df, task='classification'):
    df = df.copy()
    
    if task == 'classification':
        df = df.drop('stab', axis=1)
        
        y = df['stabf'].copy()
        X = df.drop('stabf', axis=1).copy()
        
    elif task == 'regression':
        df = df.drop('stabf', axis=1)
        
        y = df['stab'].copy()
        X = df.drop('stab', axis=1).copy()
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.7, shuffle=True, random_state=1)
    
    return X_train, X_test, y_train, y_test




#  CLASSIFICATION TASK

#X_train, X_test, y_train, y_test = preprocess_inputs(data, task='classification')

#X_train
#y_train



#clf = XGBClassifier()
#clf.fit(X_train, y_train)
#print("Classifier trained.")

#print("Classification Test Accuracy: {:.2f}%".format(clf.score(X_test, y_test) * 100))





#  REGRESSION TASK

X_train, X_test, y_train, y_test = preprocess_inputs(data, task='regression')

X_train

y_train



reg = XGBRegressor()
reg.fit(X_train, y_train)
print("Regressor trained.")


print("Regression Test R^2 Score: {:.5f}".format(reg.score(X_test, y_test)))








