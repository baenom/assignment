import pandas as pd
import numpy as np

data_url = "https://lib.stat.cmu.edu/datasets/boston"
raw_df = pd.read_csv(data_url,sep='\s+',skiprows=22,header=None)
data = np.hstack([raw_df.values[::2,:],raw_df.values[1::2,:2]])
target = raw_df.values[1::2,2]
dropnadf = raw_df.dropna(axis=0)
print(dropnadf)

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

df = pd.DataFrame(data)
df['MEDV'] = target

df = df.dropna(axis=0)

x = df.iloc[:,:13]
y = df['MEDV']


x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42)

linear_model = LinearRegression()
linear_model.fit(x_train,y_train)

y_pred = linear_model.predict(x_test)

residual = y_test - y_pred
print(y_pred)
print(residual)


plt.figure(figsize=(8,6))
plt.scatter(y_test,y_pred)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()])
plt.show

from sklearn.linear_model import LogisticRegression
median_value = df['MEDV'].median()
y = (df['MEDV'] >= median_value).astype(int)
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42)
logistic_model = LogisticRegression(max_iter=10000)
logistic_model.fit(x_train,y_train)

y_pred = logistic_model.predict(x_test)
print(y_pred)

from sklearn.neural_network import MLPRegressor
from sklearn.preprocessing import StandardScaler

y = df['MEDV']
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42)

scaler = StandardScaler()
x_train_scaler = scaler.fit_transform(x_train)
x_test_scaler = scaler.transform(x_test)

nn_model = MLPRegressor(hidden_layer_sizes=(64,32),max_iter=2000,random_state=42)

nn_model.fit(x_train_scaler,y_train)
y_pred = nn_model.predict(x_test_scaler)
print(y_pred)