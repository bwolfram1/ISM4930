#https://archive.ics.uci.edu/ml/datasets/Occupancy+Detection+
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import AdaBoostClassifier
from sklearn import svm, tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix,f1_score
#import the data
df = pd.read_csv("occupancy_data/datatest.txt")
#seeing how much of each class of the target variable we have
dsp = sns.distplot(df["Occupancy"])
plt.figure()
#plotting correlations to get some more insights 
corr = df.corr()
crp = sns.heatmap(corr,square=True)
pap = sns.pairplot(df, hue="Occupancy")

#defining our predictors 
X = df.drop("Occupancy", axis=1)
X["date"] = pd.to_datetime(X["date"]).dt.dayofyear


#defining our target variable
y = df.iloc[:,-1]


x_train, x_test, y_train, y_test = train_test_split(X, y, random_state=42)

lr = LogisticRegression()
lr.fit(x_train, y_train)

y_pred = lr.predict(x_test)
print(confusion_matrix(y_test, y_pred))
print("Log Regression: " + str(f1_score(y_test, y_pred)))

clf = svm.SVC(gamma='scale')
clf.fit(x_train, y_train)
y_predsvc = clf.predict(x_test)
print(confusion_matrix(y_test, y_predsvc))
print("SVC: " + str(f1_score(y_test, y_predsvc)))

tlf = tree.DecisionTreeClassifier()
tlf = tlf.fit(x_train, y_train)
y_predtree = tlf.predict(x_test)
print(confusion_matrix(y_test, y_predtree))
print("Tree: " + str(f1_score(y_test, y_predtree)))

alf = AdaBoostClassifier(n_estimators=150)
alf = alf.fit(x_train, y_train)
y_predab = alf.predict(x_test)
print(confusion_matrix(y_test, y_predab))
print("AdaBoost: " + str(f1_score(y_test, y_predab)))
