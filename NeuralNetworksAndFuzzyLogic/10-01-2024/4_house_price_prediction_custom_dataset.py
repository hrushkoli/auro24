# %%
import tensorflow as tf
from tensorflow.keras import layers, models
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

import pandas as pd
import matplotlib.pyplot as plt

import seaborn as snb

df = pd.read_csv("house_prediction.csv")
df.head()

# %%
df.info()

# %%
df.describe()

# %%
df.head()

# %%
df.isnull().sum()

# %%
df['country'].unique()

# %%
df.drop(['country'], axis=1, inplace = True)

# %%
df.columns

# %%
from sklearn.preprocessing import LabelEncoder

le_street = LabelEncoder()
le_city = LabelEncoder()
le_statezip = LabelEncoder()

# %%
df['street'] = le_street.fit_transform(df['street'])
df['city'] = le_city.fit_transform(df['city'])
df['statezip'] = le_statezip.fit_transform(df['statezip'])

# %%
df.info()

# %%
df.drop(['date'], axis=1, inplace = True)
df.head()

# %%
plt.figure(figsize=(12, 6))
snb.heatmap(df.corr(), annot=True, cmap='viridis')
plt.show()

# %%
df.drop(['sqft_above'],axis=1,inplace=True)

# %%
X = df.iloc[:, 1:]
y = df.price

# %%
train_data, test_data, train_targets, test_targets = train_test_split(X, y, test_size=0.3, random_state=42)

# %%
# Normalize the data (this is important for neural networks)
scaler = StandardScaler()
train_data = scaler.fit_transform(train_data)
test_data = scaler.transform(test_data)

# %%
print("Train Data: ", len(train_data))
print("Test Data: ", len(test_data))

# %%
train_data.shape[1]

# %%
# Build the model
model = models.Sequential()
model.add(layers.Dense(128, activation='relu', input_shape=(train_data.shape[1],)))
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(1))  # Output layer for regression
model.summary()

# %%
# Compile the model
model.compile(optimizer='rmsprop', loss='mse', metrics=['accuracy'])

# %%
# Train the model
history = model.fit(train_data, train_targets, epochs=100, batch_size=32, validation_data=(test_data, test_targets))


# %%
# Evaluate the model
test_mse_score, test_mae_score = model.evaluate(test_data, test_targets)
print(f"Test MSE: {test_mse_score}")
print(f"Test MAE: {test_mae_score}")

# %%
# Plotting the training and validation loss
plt.figure(figsize=(12, 5))

# Plot loss vs val_loss
plt.subplot(1, 2, 1)
plt.plot(history.history['loss'], label='Training Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.title('Training and Validation Loss')

# Plot mae vs val_mae
plt.subplot(1, 2, 2)
plt.plot(history.history['accuracy'], label='Training Aaccuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()
plt.title('Training and Validation Accuracy')

plt.tight_layout()
plt.show()

# %%


# %%
