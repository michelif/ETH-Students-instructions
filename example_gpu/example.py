# Check settings
import tensorflow as tf
from keras import backend as K
print("-------------------------------------------")
print("GPU available: ", tf.test.is_gpu_available())
print("Keras backend: ", K.backend())
print("-------------------------------------------")

import numpy as np

# Load layers from keras
from keras.layers import Dense
from keras.models import Sequential
from keras.losses import binary_crossentropy

# load and split dataset
data = np.loadtxt("data.csv", delimiter=",")
X = data[:, :-1]
y= data[:, -1]

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42)

# Setup network
model = Sequential()
model.add(Dense(1024, activation="relu", input_shape=(X.shape[1],)))
model.add(Dense(512, activation="relu"))
model.add(Dense(512, activation="relu"))
model.add(Dense(256, activation="relu"))
model.add(Dense(1))

# Compile model
model.compile(optimizer="adam", loss="mean_squared_error")

# Train model
model.fit(x=X_train, y=y_train, epochs=100, batch_size=10000)

# Evaluate model
results = model.predict(X_test, batch_size=10000)
from sklearn.metrics import roc_auc_score
auc = roc_auc_score(y_test, results)
print("area under ROC curve: ", auc)
