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
from sklearn.linear_model import LogisticRegression
from sklearn import preprocessing

# # 2. Reading Data

heartDiseaseData = pd.read_csv("heart_disease_classification.csv")
heartDiseaseData.head()

# # 3. Encoding Sex data from "male", "female" to 1 & 

label_encoder = preprocessing.LabelEncoder()
heartDiseaseData['Sex'] = label_encoder.fit_transform(heartDiseaseData['Sex'])
heartDiseaseData.head()

# # 4. Creating a heatmap of the correlation matrix
#

plt.figure(figsize=(16,10))
ax = sns.heatmap(heartDiseaseData.corr(),annot=True)
plt.show()

# # 5. Creating a regression plot of Thalassemia to know the link between Thalassemia and Heart Disease

sns.regplot(data=heartDiseaseData, x=heartDiseaseData['Thalassemia '], y=Y)
plt.show()

# # 6. Splitting Data

X=heartDiseaseData[['Age','Sex','ChestPainType','RestingBP','cholesterol ','FastingBS','Resting electrocardiographic','MaxHR','ExerciseAngina','Oldpeak','slope of the peak','MajorVessels','Thalassemia ']]
Y=heartDiseaseData['HeartDisease']
x_train, x_test, y_train , y_test = train_test_split(X,Y,test_size=0.2)

# # 7. Creating Logistic Regression Model

clf = LogisticRegression(solver='lbfgs', max_iter=1000)

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

# # 12. Creating Confusion Matrix

# +
from sklearn.metrics import confusion_matrix

cm = confusion_matrix(y_test, predict)
cm

# +
# now, visualize confusion metrix

ax = sns.heatmap(cm, annot=True, cmap='Blues')

ax.set_title('Confusion Matrix with labels\n\n');
ax.set_xlabel('\nPredicted Values')
ax.set_ylabel('Actual Values ');


## Display the visualization of the Confusion Matrix.
plt.show()

# +
ax = sns.heatmap(cm/np.sum(cm), annot=True,  fmt='.2%', cmap='Blues')

ax.set_title('Confusion Matrix with labels\n\n');
ax.set_xlabel('\nPredicted Values')
ax.set_ylabel('Actual Values ');


## Display the visualization of the Confusion Matrix.
plt.show()
