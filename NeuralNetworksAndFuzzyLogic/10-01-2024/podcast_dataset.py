# Loan Approval Data 

import tensorflow as tf
from tensorflow.keras import layers, models
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

import pandas as pd
import matplotlib.pyplot as plt

import seaborn as snb

df = pd.read_csv("./podcast_dataset.csv")
df.head()
df.drop(['Number_of_Ads'],axis=1,inplace=True)
df.drop(['Podcast_Name'],axis=1,inplace=True)
df.drop(['Episode_Title'],axis=1,inplace=True)
df.head()
from sklearn.preprocessing import LabelEncoder

le_publication_day= LabelEncoder()
le_publication_time= LabelEncoder()
le_episode_sentiment = LabelEncoder()
le_genre= LabelEncoder()
df['Publication_Day'] = le_publication_day.fit_transform(df['Publication_Time'])
df['Publication_Time'] = le_publication_time.fit_transform(df['Publication_Time'])
df['Episode_Sentiment'] = le_episode_sentiment.fit_transform(df['Episode_Sentiment'])
df['Genre'] = le_genre.fit_transform(df['Genre'])

df.head()

plt.figure(figsize=(12, 6))
snb.heatmap(df.corr(), annot=True, cmap='viridis')
plt.show()

## By Looking at the Correlation graph we can determine that the listening time is strongly related to the Episode Length


X = df.iloc[:, 1:]
X
y = df["Listening_Time_minutes"]
y

# %%
train_data, test_data, train_targets, test_targets = train_test_split(X, y, test_size=0.2, random_state=42)

# %%
# Normalize the data (this is important for neural networks)
scaler = StandardScaler()
train_data = scaler.fit_transform(train_data)
train_data
test_data = scaler.transform(test_data)
test_data

# %%
print("Train Data: ", len(train_data))
print("Test Data: ", len(test_data))

# %%

# %%
# Build the model
model = models.Sequential()
model.add(layers.Dense(64, activation='relu', input_shape=(train_data.shape[1],)))
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(1))  # Output layer for regression
model.summary()

# %%
# Compile the model
model.compile(optimizer='sgd', loss='mse', metrics=['accuracy'])

# %%
# Train the model
history = model.fit(train_data, train_targets,epochs=100,batch_size=32,validation_data=(test_data, test_targets))


# %%
# Evaluate the model
test_mse_score, test_mae_score = model.evaluate(test_data, test_targets)
test_mse_score
print(f"Test MSE: {test_mse_score}")
print(f"Test MAE: {test_mae_score}")



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
