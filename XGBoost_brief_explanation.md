# Smart-grid-stability-prediction-with-classification-and-regression-models-from-XGBoost
"Smart Grid Stability Prediction with XGBoost Classification and Regression Models."

This code demonstrates the use of XGBoost for both classification and regression tasks in the context of smart grid stability prediction. Here's a brief explanation:

Data Loading: The code begins by importing the necessary libraries and loading the dataset from a CSV file using pd.read_csv(). The data.info() line 
provides information about the dataset, such as the number of rows, columns, and data types.



Preprocessing: The preprocess_inputs() function is defined to preprocess the dataset based on the specified task. 
If the task is classification, the 'stab' column is dropped, and the target variable 'stabf' is assigned to the variable y, 
while the remaining columns are assigned to X. For regression, the 'stabf' column is dropped, and 'stab' is assigned to y. 
The function also performs train-test splitting using train_test_split().



Classification Task (commented out): This section demonstrates the classification task. 
It preprocesses the data using preprocess_inputs() for classification, assigns the returned 
values to X_train, X_test, y_train, y_test, and creates an instance of XGBClassifier(). 
The classifier is then trained on the training data using clf.fit(). 
The test accuracy of the classifier is printed using clf.score().



Regression Task: This section demonstrates the regression task. 
It preprocesses the data using preprocess_inputs() for regression, 
assigns the returned values to X_train, X_test, y_train, y_test, and creates an instance of XGBRegressor().
The regressor is trained on the training data using reg.fit(). The R^2 score of the regressor is printed using reg.score().


In summary, the code showcases how to use XGBoost for both classification and regression 
tasks by preprocessing the data accordingly and training the respective models.

















credit goes to: https://www.kaggle.com/code/gcdatkin/smart-grid-stability-prediction
