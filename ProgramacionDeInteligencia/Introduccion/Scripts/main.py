import numpy as np
import pandas as pd
import tensorflow as tf
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import Dense
from sklearn.datasets import load_iris
from matplotlib.colors import LightSource
import random

iris = load_iris()

sepal_length = iris.data[0:99, 0]
petal_length = iris.data[0:99, 2]
flower_type = iris.target[0:99]

x = np.column_stack((sepal_length, petal_length))
y = flower_type

np.random.seed(5)
tf.random.set_seed(5)
random.seed(5)

model = Sequential()
model.add(Dense(6, activation='relu', input_dim=2))
model.add(Dense(12, activation='relu'))
model.add(Dense(6, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
model.compile(loss='mean_squared_error')

model.fit(x, y, epochs=40)

print(model.predict([[4.9, 1.4]]))
print(model.predict([[6.3, 4.9]]))
