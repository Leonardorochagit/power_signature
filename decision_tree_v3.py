# Load libraries
import pandas as pd
from sklearn.tree import DecisionTreeClassifier # Import Decision Tree Classifier
from sklearn.model_selection import train_test_split # Import train_test_split function
from sklearn import metrics #Import scikit-learn metrics module for accuracy calculation

col_names = ["Eletro", "phAngle_mean", "Freq_mean", "ReactPower_mean", "Power_mean", "Volts_mean", "Cur_mean"]
# load dataset
pima = pd.read_csv("db_eletr.csv", header=0, names=col_names)
pima.head()

#split dataset in features and target variable
feature_cols = ["phAngle_mean", "Freq_mean", "ReactPower_mean", "Power_mean", "Volts_mean", "Cur_mean"]
X = pima[feature_cols] # Features
y = pima.label # Target variable

# Split dataset into training set and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=1) # 70% training and 30% tests

# Create Decision Tree classifer object
clf = DecisionTreeClassifier()

# Train Decision Tree Classifer
clf = clf.fit(X_train,y_train)

# Predict the response for test dataset
y_pred = clf.predict(X_test)

# Model Accuracy, how often is the classifier correct?
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))

