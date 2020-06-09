import numpy as np
from sklearn.svm import SVR 
import matplotlib.pyplot as plt 
import pandas as pd 

df = df[['totalconfirmed']] 
print(df.head())
#Taking out the column which is of our interest.

forecast_out = 30 
#Create another column (the target ) shifted 'n' units up
df['Prediction'] = df[['totalconfirmed']].shift(-forecast_out)
print(df.tail())
#This adds NaN values in prediction Columns which will be updated after prediction.

X = np.array(df.drop(['Prediction'],1))
X = X[:-forecast_out]

y = np.array(df['Prediction'])
# Get all of the y values except the last '30' rows
y = y[:-forecast_out]

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

x_forecast = np.array(df.drop(['Prediction'],1))[-forecast_out:]

lr = LinearRegression()
# Train the model
lr.fit(x_train, y_train)

lr_confidence = lr.score(x_test, y_test)
print("lr confidence: ", lr_confidence)
#lr confidence:  0.8711626422970308 in this case

lr_prediction = lr.predict(x_forecast)
print(lr_prediction)
