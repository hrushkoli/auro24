# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.16.4
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# # 1. Importing Libraries

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import preprocessing

# # 2. Reading Data

podcastData = pd.read_csv("podcast_dataset.csv")
podcastData.head()

# # 3. Encoding Values

# +
label_encoder = preprocessing.LabelEncoder()
encodedPodcastData = podcastData.copy()
encodedPodcastData['Podcast_Name'] = label_encoder.fit_transform(podcastData['Podcast_Name'])
encodedPodcastData['Episode_Title'] = label_encoder.fit_transform(podcastData['Podcast_Name'])
encodedPodcastData['Genre'] = label_encoder.fit_transform(podcastData['Podcast_Name'])
encodedPodcastData['Publication_Day'] = label_encoder.fit_transform(podcastData['Podcast_Name'])
encodedPodcastData['Publication_Time'] = label_encoder.fit_transform(podcastData['Podcast_Name'])
encodedPodcastData['Episode_Sentiment'] = label_encoder.fit_transform(podcastData['Podcast_Name'])

encodedPodcastData
# -

# # 4. Creating a heatmap of the correlation matrix
#

plt.figure(figsize=(16,10))
ax = sns.heatmap(encodedPodcastData.corr(),annot=True)
plt.show()

# # 5. Creating a regression plot of Thalassemia to know the link between Thalassemia and Heart Disease

# +
# sns.regplot(data=heartDiseaseData, x=heartDiseaseData['Thalassemia '], y=Y)
# plt.show()
# -

# # 6. Splitting Data and Preprocessing

# +
encodedPodcastData = encodedPodcastData.dropna()
X=(encodedPodcastData.copy()).drop(['Listening_Time_minutes','Podcast_Name','Episode_Title','Genre','Publication_Time'm],axis=1)
Y=encodedPodcastData[['Listening_Time_minutes']]
print(X.shape)
print(Y.shape)

x_train, x_test, y_train , y_test = train_test_split(X,Y,test_size=0.5)

# -

# # 7. Creating Logistic Regression Model

clf = LinearRegression()

# # 8. Training the model on the training data created previously

clf.fit(x_train,y_train)

# # 9. Predicting the values of heart disease using the test data

# +
clf.score(x_train,y_train)

predict = clf.predict(x_test)
predict
# -

# # 10. Finding the mean error between the test values and the test values

# +
from sklearn.metrics import mean_squared_error,mean_absolute_error

mean_squared_error(predict,y_test)
# -

# # 11. Finding the mean error between the test values and the predicted values

mean_squared_error(predict,y_test)


