import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

# 1️⃣ Generate sequential data
t = np.linspace(0, 50, 500)
data = np.sin(t)

# 2️⃣ Prepare dataset for LSTM
def create_dataset(data, time_steps=10):
    X, y = [], []
    for i in range(len(data)-time_steps):
        X.append(data[i:i+time_steps])
        y.append(data[i+time_steps])
    X, y = np.array(X), np.array(y)
    X = X.reshape((X.shape[0], X.shape[1], 1))  # (samples, timesteps, features)
    return X, y

time_steps = 20
X, y = create_dataset(data, time_steps)

# 3️⃣ Build LSTM model
model = Sequential([
    LSTM(50, activation='tanh', input_shape=(time_steps, 1)),
    Dense(1)
])

# 4️⃣ Compile model
model.compile(optimizer='adam', loss='mse')

# 5️⃣ Train model
history = model.fit(X, y, epochs=50, batch_size=16, validation_split=0.1, verbose=1)

# 6️⃣ Evaluate & Predict
y_pred = model.predict(X)

# Plot results
plt.figure(figsize=(12,6))
plt.plot(data[time_steps:], y, label='Original')
plt.plot(data[time_steps:], y_pred, label='Predicted')
plt.legend()
plt.title("LSTM Time Series Prediction")
plt.show()
