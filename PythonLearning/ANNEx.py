# ----------------------------
# Artificial Neural Network (ANN) Training Example
# Dataset: Iris Flower Classification
# ----------------------------

import tensorflow as tf
from tensorflow.keras import layers, models
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.utils import to_categorical

# 1️⃣ Load the dataset
iris = load_iris()
X = iris.data          # Features: sepal & petal length/width
y = iris.target        # Labels: 0,1,2 (setosa, versicolor, virginica)

# 2️⃣ Preprocess the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)             # normalize
y_categorical = to_categorical(y, 3)           # one-hot encode labels

# Split into train and test
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y_categorical, test_size=0.2, random_state=42)

# 3️⃣ Build the ANN model
model = models.Sequential([
    layers.Dense(10, activation='relu', input_shape=(4,)),  # hidden layer 1
    layers.Dense(8, activation='relu'),                     # hidden layer 2
    layers.Dense(3, activation='softmax')                   # output layer (3 classes)
])

# 4️⃣ Compile the model
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# 5️⃣ Train the model
print("\nTraining ANN...")
history = model.fit(X_train, y_train, epochs=50, batch_size=8,
                    validation_split=0.2, verbose=1)

# 6️⃣ Evaluate
loss, acc = model.evaluate(X_test, y_test)
print(f"\n✅ Test Accuracy: {acc*100:.2f}%")

# 7️⃣ Predict
sample = [[5.1, 3.5, 1.4, 0.2]]   # Example flower
sample_scaled = scaler.transform(sample)
prediction = model.predict(sample_scaled)
predicted_class = iris.target_names[prediction.argmax()]

print(f"🌸 Predicted Flower Type: {predicted_class}")
