"""Model.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gybSZ1kkOSSFXHOj_E2aX3lbaZ75eCZi

# **Iris Prediction using Decision Tree Algorithm**

## **Importing the libraries**
"""

import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

"""## **Importing the dataset**"""

dataset = pd.read_csv('Iris.csv')
X = dataset.iloc[:, :-1].values # Independent variables
y = dataset.iloc[:, -1].values  # Dependent or Target variable (Iris-Species)

"""## **Dataset information**"""

dataset

dataset.info()
# datatypes and null_value count

dataset.shape
# Rows & Columns

"""## **Exploratory Data Analysis (EDA)**"""

plt.title('Species vs SepalLengthCm')
sns.barplot(data= dataset, x = 'SepalLengthCm', y= 'Species', hue = 'Species')

plt.title('Species vs SepalWidthCm')
sns.barplot(data= dataset, x = 'SepalWidthCm', y= 'Species', hue = 'Species')

plt.title('Species vs PetalLengthCm')
sns.barplot(data= dataset, x = 'PetalLengthCm', y= 'Species', hue = 'Species')

plt.title('Species vs PetalWidthCm')
sns.barplot(data= dataset, x = 'PetalWidthCm', y= 'Species', hue = 'Species')

"""## **Splitting the dataset into the Training set and Test set**"""

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)

"""## **Feature Scaling**"""

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

"""## **Training the Decision Tree Classification model on the Training set**"""

from sklearn.tree import DecisionTreeClassifier
classifier = DecisionTreeClassifier(criterion = 'entropy', random_state = 0)
classifier.fit(X_train, y_train)

"""## **Predicting Prediction class**"""

y_pred = classifier.predict(X_test)

"""## **Predicting result individually**

"""

print(classifier.predict(sc.transform([[1, 5.1, 3.5, 1.4, 0.2]])))

"""## **Making the Confusion Matrix "Accuracy"**


"""

from sklearn.metrics import confusion_matrix, accuracy_score
cm = confusion_matrix(y_test, y_pred)
print("Accuracy: {:.2f}%".format(accuracy_score(y_test, y_pred)*100))

"""## **Visualising the Real class and Predicted class**"""

sns.countplot(y_pred, data=dataset)
plt.title('Predicted class')
plt.xlabel('Iris-Species')
plt.show()
sns.countplot(y_test,  data=dataset)
plt.title('Real class')
plt.xlabel('Iris-Species')
plt.show()
