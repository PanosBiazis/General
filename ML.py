#Python using Machine learning
#The Regression/Estimaton technique is used for predicting a continuous value.
#A Classification technique is used for predicting the class or category of a case.
#Association technique is used for finding items or events that often co-occur,
#For example grocery items that are usually bought together by a particular customer.
#Anomaly detection is used to discover abnormal and unusual cases,
#For example it is used for credit card fraud detection.
#Sequence mining is used for predicting the next event,for instance, the click-stream in websites.
#Dimension  reduction is used to reduce the size of data.
#Recommendation systems,the associates people's preferences with others who have similar tastes, and recommends new items to them, such as books or movies.
#The first package is NumPy which is a math library to work with N-dimensional arrays in Python.
#It enables you to do computation efficiently and effectively.
#SciPy is a collection of numerical algorithms and domain specific toolboxes,including signal processing , optimization , statistics and much more.
#SciPy is a good library for scientific and high performance computation.
#Matplotlib is a very popular plotting package that provides 2D plotting, as well as 3D plotting.
#Pandas library is a very high-level Python library that provides high performance easy to use data structures.
#It has many functions for data importing manipulation and analysis.
#In particular,it offers data structures and operations for manipuating numerical tables and timeseries.
#SciKit Learn is a collection of algorithms and tools for  machine learning which is our focus here and which you"ll learn to use within this course.
#Supervised vs  Unsupervised algorithms.
#There are two types of supervised learning techniques.They are classification, and regression.
#Classification is a process of predicting a discrete class label, or category.
#Regression is the process of predicting a continuous value as opposed to predicting a categorical value in classification.
#Unsupervised algorithm is when we let model work on its own to discover information that may not be visible to the human eye.
#It means, it trains on the dataset, and draws conclusions on unlabeled data.
#There are two types of regression models. Simple and Multiple.
#Simple  regression model involves only one independent variable is used to estimate a dependent variable
# multiple regression model involves more than one independent variables is used to  estimate mutiple dependent variable.
#It can be linear or nonlinear.
#Linearity of regression, is based on the nature of relationship between independent and dependent variables.
#Essentially, we use regression when we want to estimate a continuous value.
#Linear regression estimates the coefficients of the line.
#This error is also called the residual error.Also, the error is the distance from the data point to the fitted regression line.
#Furthermore, The mean of all residual errors shows how poorly the line fits with the whole data set.
#Our objective is to find a line where the mean of all these errors is minimised.
#In other words, the mean error of the prediction using the fit line should be minimized.
#The goal of regression is to build a model to accurately predict an unknown case.
#We use the entire dataset for training and we build a model using this training set.
#Now, we select a small portion of the dataset,such as row number six to nine, but without the labels.
#This set is called a test set, which has the labels, but the labels are not used for prediction and is used only as ground truth.
#The labels are called actual values of the test set.
#Now we pass the feauture set of the testing portion to our built mdel and predict the target values.
#Finally, we compare the predicted values by our model with actual values in the test set.
#Training accuracy is the percentage of correct predictions that the model makes when using the test dataset.
#However, a high training accuracy isn't necessarily a good thing.
#For instance,having a high training accuracy may result in an over-fit the data.
#This means that the model is overly trained to the dataset, which may capture noise and poduce a non-generalized model.
#Out-of-sample accuracy is the  percentage of correct predictions made after the model has not been trained on.
#The second evaluation approach is called train/test split.
#Here,we divide the dataset into two parts:a training set and a test set.
#Then,we train our model on the training set and make predictions on the test set.
#Afterwards,we calculate the accuracy of our model on the test set.
#Evaluation metrics are used to explain the performance of a model.
#Evaluation metrics, provide a key role in the development of a model, as it provides insight to areas that require improvement.
#In the context of regression, the error of the model is the difference between the data points and the trend line generated by the algorithm.
#Since there are multiple data points, an error can be determined in multiple ways.
import matplotlib.pyplot as plt#Importing matplotlib module
import pandas as pd#Importing pandas module
import pylab as pl#Importing pylab module
import numpy as np#Importing numpy module
import seaborn as sns#Importing seaborn module
import itertools#Importing itertools module
import matplotlib.ticker as ticker#Importing ticker module from matplotlib
from sklearn import preprocessing#Importing preprocessing module from scikit learn
from sklearn import datasets, linear_model, metrics#Importing sklearn module
from sklearn.linear_model import LinearRegression#Importing LinearRegression module from sklearn
from sklearn.datasets import fetch_california_housing#Importing fetch_california_housing module from sklearn
from sklearn.model_selection import train_test_split#Importing train_test_split module from sklearn
from sklearn.metrics import r2_score#Importing r2_score module from sklearn
from sklearn.metrics import mean_squared_error#Importing mean_squared_error module from sklearn
from sklearn.metrics import mean_absolute_error#Importing mean_absolute_error module from sklearn
from sklearn.metrics import explained_variance_score#Importing explained_variance_score module from sklearn
from sklearn.model_selection import cross_val_score#Importing cross_val_score module from sklearn
from sklearn.model_selection import GridSearchCV#Importing GridSearchCV module from sklearn
from sklearn.metrics import classification_report#Importing classification_report module from sklearn
from sklearn.metrics import confusion_matrix#Importing confusion_matrix module from sklearn
from sklearn.metrics import accuracy_score#Importing accuracy_score module from sklearn
from sklearn.metrics import precision_score#Importing precision_score module from sklearn
from sklearn.metrics import recall_score#Importing recall_score module from sklearn
from sklearn.metrics import f1_score#Importing f1_score module from sklearn
from sklearn.metrics import roc_curve#Importing roc_curve module from sklearn
from sklearn.metrics import roc_auc_score#Importing roc_auc_score module from sklearn
from sklearn.metrics import log_loss#Importing log_loss module from sklearn
from sklearn.metrics import mean_poisson_deviance#Importing mean_poisson_deviance module from sklearn
from sklearn.metrics import mean_gamma_deviance#Importing mean_gamma_deviance module from sklearn
from sklearn.metrics import mean_tweedie_deviance#Importing mean_tweedie_deviance module from sklearn
from sklearn.metrics import mean_absolute_percentage_error#Importing mean_absolute_percentage_error module from sklearn
from sklearn.metrics import jaccard_score
from sklearn.model_selection import train_test_split#Importing train_test_split module from sklearn
from sklearn.neighbors import KNeighborsClassifier#Importing KNeighborsClassifier module from sklearn
from sklearn.preprocessing import StandardScaler#Importing StandardScaler module from sklearn
from sklearn.tree import DecisionTreeRegressor#Importing DecisionTreeRegressor module from sklearn
from sklearn.tree import DecisionTreeClassifier#Importing DecisionTreeClassifier module from sklearn
#from sklearn.externals.six import StringIO##For Python 3 compatibility
import six #For Python 3 compatibility
from six import StringIO#For Python 3 compatibility
import pydotplus#For visualization of decision tree
import matplotlib.image as mpimg#For visualization of decision tree
from sklearn import tree#For visualization of decision tree
from sklearn.ensemble import RandomForestClassifier#Importing RandomForestClassifier module from sklearn
from sklearn.ensemble import RandomForestRegressor#Importing RandomForestRegressor module from sklearn
from sklearn.ensemble import GradientBoostingClassifier#Importing GradientBoostingClassifier module from sklearn
from sklearn.ensemble import GradientBoostingRegressor#Importing GradientBoostingRegressor module from sklearn
from sklearn.preprocessing import LabelEncoder#Importing LabelEncoder module from sklearn
from sklearn.preprocessing import OneHotEncoder#Importing OneHotEncoder module from sklearn
from sklearn.tree import plot_tree#Importing plot_tree module from sklearn
import pydot#For visualization of decision tree
from sklearn.tree import export_graphviz#Importing export_graphviz module from sklearn
from IPython.display import Image#Importing Image module from IPython.display for displaying images in Jupyter notebooks
from PIL import Image#Importing Image module from PIL for displaying images in Jupyter notebooks
from mpl_toolkits.mplot3d import Axes3D#Importing Axes3D module from mpl_toolkits.mplot3d
from tensorflow import keras#Importing keras module from tensorflow
from keras import layers#Importing layers module from tensorflow.keras
import time#Importing time module to record the execution time
from matplotlib.widgets import Button#Importing Button module from matplotlib.widgets
import scipy.optimize as opt #Importing  scipy
from scipy.optimize import minimize #Importing minimize module from scipy
from sklearn.metrics import confusion_matrix
import itertools
from sklearn.linear_model import LogisticRegression  # Importing a model, e.g., Logistic Regression
from sklearn import svm #
import random
import xgboost as xgb
import warnings
from sklearn.cluster import KMeans
from sklearn.metrics import davies_bouldin_score
from sklearn.metrics import silhouette_score
from sklearn.datasets._samples_generator import make_blobs


# # data_url = "http://lib.stat.cmu.edu/datasets/boston"#URL of the dataset
# data_url = "F:\panag\Documents\ΕΡΓΑΣΤΗΡΙΑΚΕΣ ΑΣΚΗΣΕΙΣ\Python tries\\boston.csv"#URL of the dataset
# raw_df = pd.read_csv(data_url, sep="\s+", skiprows=22, header=None)#Reading the dataset
# data = np.hstack([raw_df.values[::2, :], raw_df.values[1::2, :2]])#Storing the dataset in a numpy array
# target = raw_df.values[1::2, 2]#Storing the target variable in a numpy array

# housing = fetch_california_housing()#Loading the California housing dataset from scikit learn library

# The dataset contains the following attributes:
# housing.data: array of shape (20640, 8)
# housing.target: array of shape (20640,)
# housing.DESCR: description of the dataset
#Loading the Boston housing dataset from scikit learn library
#boston = datasets.load_boston()
df = pd.read_csv(r'/run/media/panos/SAMSUNG T7/panag/Documents/ΕΡΓΑΣΤΗΡΙΑΚΕΣ ΑΣΚΗΣΕΙΣ/Python tries/FuelConsumptionCo2.csv')#('F:\panag\Documents\ΕΡΓΑΣΤΗΡΙΑΚΕΣ ΑΣΚΗΣΕΙΣ\Python tries\FuelConsumptionCo2.csv')#Reading csv file
#take a look at the dataset
df.head()#showing first five rows of the dataframe
print(df.head(10)['ENGINESIZE'])#Showing first 10 rows of ENGINESIZE column
#Visualizing the distribution of ENGINESIZE
plt.figure(figsize=(6,6))#Setting figure size
plt.hist(df['ENGINESIZE'],bins=20)#Histogram of ENGINESIZE column
plt.xlabel('ENGINESIZE')#x-axis label
plt.ylabel('Frequency')#y-axis label
plt.title('Distribution of ENGINESIZE')#title of the plot
plt.grid(True)#Adding grid lines
plt.show()#Displaying the plot
#Statistics about the dataset
print("Data Set Information")
print(df.info())
#There are missing values in the dataset.
#To handle them, we need to prepare our dataset before applying any machine learning algorithm.
#First step is to check if there are any null values in the dataset.
print("\nChecking For Null Values")
print(df.isnull().sum())#Sum of each column having null values
#As seen above,there are no null values in the dataset.
#Next,let us understand the correlation between the features of the dataset.
# Remove the 'MODEL' column from the dataset
cdf = df.drop('MODEL', axis=1)
# Replace string values with NaN
cdf['CO2EMISSIONS_num'] = cdf['CO2EMISSIONS;;;;;;;;;;;;;;;;;;;'].replace('ACURA', np.nan)
# Replace non-numeric values with the mean
cdf['CO2EMISSIONS_num'] = cdf['CO2EMISSIONS_num'].apply(lambda x: np.nan if type(x) != float else x)
cdf['CO2EMISSIONS_num'] = cdf['CO2EMISSIONS_num'].fillna(cdf['CO2EMISSIONS_num'].mean())
# Drop rows with non-numeric values
cdf = cdf.dropna(subset=['CO2EMISSIONS_num'])
# Fill NaN values with the mean of the column
cdf['CO2EMISSIONS_num'] = cdf['CO2EMISSIONS_num'].fillna(cdf['CO2EMISSIONS_num'].mean())

# Convert the NaN values to float
cdf['CO2EMISSIONS_num'] = cdf['CO2EMISSIONS_num'].astype(float)
# Calculate the correlation matrix
corr_matrix = cdf.corr()#Correlation matrix
f, axarr = plt.subplots(1,1,figsize=(10,10))#Setting figure size for subplots
#Plotting heatmap of the correlation matrix
sns.heatmap(corr_matrix,vmin=-1,vmax=1,annot=True,linewidths=0.5,cmap="YlGnBu")
plt.xticks(rotation=90)#Rotating x-axis labels so they fit better
plt.yticks(rotation=0)#Rotating y-axis labels so they fit better
plt.show()#Displaying the plot
# Converting the CO2EMISSIONS;;;;;;;;;;;;;;;;;;; column to float
cdf['CO2EMISSIONS_num'] = cdf['CO2EMISSIONS;;;;;;;;;;;;;;;;;;;'].str.split(';').str[0].astype(float)
#From the correlation matrix,it seems that the features have a strong correlation with CO2 emissions.
#We will remove this feature from our dataset and see if there is any improvement in our model.
#summarize the data
cdf.describe()
#print(df.columns)
viz=cdf[['ENGINESIZE','CYLINDERS','FUELCONSUMPTION_COMB','CO2EMISSIONS;;;;;;;;;;;;;;;;;;;']]#selecting only the features we need
cdf.head(9)#showing first 9 rows of the dataframe
viz=cdf[['CYLINDERS','ENGINESIZE','CO2EMISSIONS;;;;;;;;;;;;;;;;;;;','FUELCONSUMPTION_COMB']]#selecting only the features we need
viz.hist()#Histogram of all features
plt.show()#Displaying the plot
cdf['CO2EMISSIONS_num'] = cdf['CO2EMISSIONS;;;;;;;;;;;;;;;;;;;'].str.split(';').str[0].astype(int)#Converting the CO2EMISSIONS;;;;;;;;;;;;;;;;;;; column to int
plt.scatter(cdf.ENGINESIZE, cdf.FUELCONSUMPTION_COMB, c=cdf['CO2EMISSIONS_num'], cmap='viridis')#Scatter plot of Engine Size vs. CO2 Emissions
plt.xlabel('Engine Size')#x-axis label
plt.ylabel('Emissions')#y-axis label
plt.show()#Displaying the plot
msk=np.random.rand(len(cdf))<0.7#Splitting the dataset into 80% training and 20% testing
train=cdf[msk]#Training set
test=cdf[~msk]#Test set
train_index = np.where(msk)[0]
test_index = np.where(~msk)[0]
plt.scatter(cdf.ENGINESIZE, cdf.CO2EMISSIONS_num, c=cdf['CO2EMISSIONS_num'], cmap='viridis')#Scatter plot of Engine Size vs. CO2 Emissions
plt.xlabel('Engine Size')#x-axis label
plt.ylabel('Emissions')#y-axis label
plt.show()#Displaying the plot
regr=linear_model.LinearRegression()#Linear regression model
train_x=np.asanyarray(train[['ENGINESIZE']])#Training features
train_y=np.asanyarray(train[['CO2EMISSIONS_num']])#Training target variable
# Convert the CO2EMISSIONS;;;;;;;;;;;;;;;;;;; column to int for the training data
train['CO2EMISSIONS_num'] = train['CO2EMISSIONS;;;;;;;;;;;;;;;;;;;'].str.split(';').str[0].astype(int)
if len (train_index) == 0:
    print("Warning: the training dataset is empty. Please adjust the split ratio.")
# Split the dataset into training and testing sets using the `train_test_split` function
#train_features, test_features, train_labels, test_labels = train_test_split(cdf[['ENGINESIZE']], cdf[['CO2EMISSIONS_num']], test_size=0.2, random_state=42)
# Create training and testing features and labels
else:
    train_features = np.asanyarray(train[['ENGINESIZE']])
    train_labels = np.asanyarray(train[['CO2EMISSIONS_num']])
    test_features = np.asanyarray(test[['ENGINESIZE']])
    test_labels = np.asanyarray(test[['CO2EMISSIONS_num']])
    # Train the linear regression model
    regr.fit(train_features, train_labels)
#regr.fit(train_x,train_y)#Training the model on the training set (invalid)
#The coefficients
    print("Coefficient:",regr.coef_)#The coefficients of the linear regression model
    print("Intercept:",regr.intercept_)#The intercept of the linear regression model
#D>Coefficients: [[39.1737071]]#The coefficients of the linear regression model
#Intercept: [125.41316608]#The intercept of the linear regression model
# Assuming you have a training dataframe `train` and a feature column name `'ENGINESIZE'`
#train_x = np.asanyarray(train[['ENGINESIZE']])
#train_y = np.asanyarray(train[['CO2EMISSIONS_num']])
#print(train_x.shape)
#print(train_y.shape)
# Fit the model using the training data
#regr.fit(train_x, train_y)
#test_x = np.asanyarray(test[['ENGINESIZE']])#Test features
#test_y=np.asanyarray(test[['CO2EMISSIONS_num']])#Test target variable
#test_y = regr.predict(test_x)#Predicting the CO2 emissions for the test set
#print("Mean absolute error: %.2f" % np.mean(np.absolute(test_y-test_y)))#Mean absolute error
#print("Residual sum of squares (MSE): %.2f" % np.mean((test_y-test_y)**2))#Residual sum of squares (MSE)
#print("R2-score: %.2f" % r2_score(test_y , test_y) )#R2-score
#Multiple linear regression model
#When multiple independent variables are used, the linear regression model is called multiple linear regression model.
#For example, if we have 2 variables, we can use 2 independent variables to predict the CO2 emissions.
#We can also use multiple independent variables to predict the CO2 emissions.
#In this case, the linear regression model is called multiple linear regression model.
#To implement it, we need to add the code below in the program.
#Additional independent variables
#Let's say we have another variable, say, 'CYLINDERS', which is a categorical variable with 3 levels. 
# We convert it to dummy variables before feeding them to the linear regression model. 
# are added by appending them to the 'ENGINESIZE' column.
#Multiple linear regression model used to idetify the strength of the effect that the independent variables have on the dependent variable.
#Second, it can be used to predict the impact of changes,that is, to understand how the dependent variable changes when we change the independent variables.
#Theta is also called the perameters or weight vector of the regression equation.
#The first element of the feature set would be set to one,because it turns that theta zero into the intercept or
#biased parameter when the vector is multiplied by the parameter vector.
#Please notce that theta transpose x in a one-dimensional space is the equation of a line,
#it is what we use in simple linear regression.
#In higher dimensions when we have more than one input or x the line is called a plane or a hyperplane, 
# and this is what we use for multiple linear regression.So the whole idea is to find the best fit hyperplane for our data.
#In linear regression,we should estimate the values for theta vector that best predict the value of the target field in each row.
#To achieve this goal,we have to minimize the error of the prediction.
#To find the optimized parameters for our model,we should first understand what the optimized parameters are,
# then we will find a way to optimize the parameters.
#In short,optimized parameters are the ones which lead to a model with fewest  errors.
df=pd.read_csv(r'/run/media/panos/SAMSUNG T7/panag/Documents/ΕΡΓΑΣΤΗΡΙΑΚΕΣ ΑΣΚΗΣΕΙΣ/Python tries/FuelConsumptionCo2.csv', usecols=['ENGINESIZE', 'CYLINDERS', 'FUELCONSUMPTION_COMB', 'CO2EMISSIONS;;;;;;;;;;;;;;;;;;;'])#Reading csv file
df.head()#showing first five rows of the dataframe
cdf=df[['ENGINESIZE','CYLINDERS','FUELCONSUMPTION_COMB','CO2EMISSIONS;;;;;;;;;;;;;;;;;;;']]#selecting only the features we need
cdf.head(9)#showing first 9 rows of the dataframe
cdf['CO2EMISSIONS_num'] = cdf['CO2EMISSIONS;;;;;;;;;;;;;;;;;;;'].str.split(';').str[0].astype(int)#Converting the CO2EMISSIONS;;;;;;;;;;;;;;;;;;; column to int
plt.scatter(cdf.ENGINESIZE, cdf.CO2EMISSIONS_num, c=cdf['CO2EMISSIONS_num'], cmap='viridis')#Scatter plot of Engine Size vs. CO2 Emissions
plt.xlabel('Engine Size')#x-axis label
plt.ylabel('Emissions')#y-axis label
plt.show()#Displaying the plot
msk=np.random.rand(len(cdf))<0.8#Splitting the dataset into 80% training and 20% testing
train=cdf[msk]#Training set
test=cdf[~msk]#Testing set
plt.scatter(cdf.ENGINESIZE, cdf.CO2EMISSIONS_num, c=cdf['CO2EMISSIONS_num'], cmap='viridis')#Scatter plot of Engine Size vs. CO2 Emissions
plt.xlabel('Engine Size')#x-axis label
plt.ylabel('Emissions')#y-axis label
plt.show()#Displaying the plot
#Multiple Regression Model
#The good thing here is that Multiple linear regression model is the extension of a single linear regression model.
regr=linear_model.LinearRegression()#Linear regression model
x=np.asanyarray(train[['ENGINESIZE','CYLINDERS','FUELCONSUMPTION_COMB']])#Training features
y=np.asanyarray(train[['CO2EMISSIONS_num']])#Training features and target variable
regr.fit(x,y)#Training the model on the training set
print("Coefficient: ",regr.coef_)#The coefficients of the linear regression model
#Sckit-learn uses the plain Ordinary Least Squares to solve the linear regression problem.
#Ordinary Least Squares is an optimization method that is used to find the optimal parameters for a linear regression model.
#It does not provide an option to select the parameters.
#OLS chooses the parameters for the linear regression model that minimizes the sum of squared errors.
#In other words,it tries to minimizes the sumof squared errors (SSE)
# or mean squared error (MSE) between the target variable (y) and our predicted output (y_hat) over all samples in the dataset.
y_hat=regr.predict(test[['ENGINESIZE','CYLINDERS','FUELCONSUMPTION_COMB']])#Predicting the CO2 emissions for the test set
x=np.asanyarray(test[['ENGINESIZE','CYLINDERS','FUELCONSUMPTION_COMB']])#Test features
y=np.asanyarray(test[['CO2EMISSIONS_num']])#Test target variable
#df=pd.read_csv('D:/panag/Documents/ΕΡΓΑΣΤΗΡΙΑΚΕΣ ΑΣΚΗΣΕΙΣ/Python tries/teleCust1000t.csv')#Reading csv file
#if 'custcat' in df.columns:
#    x = df.drop('custcat', axis=1).values
#else:
#    print("The 'custcat' column does not exist in the DataFrame.")
#print(type(x))  # <class 'numpy.ndarray'>

# Convert the NumPy array to a DataFrame
#x = pd.DataFrame(x)

#print(x.dtypes)
# or
#scaler=StandardScaler()
#x = scaler.fit_transform(x)

# Get the feature names
#feature_names = scaler.get_feature_names_out()

#print(feature_names)
# Assuming 'x' is your input data
#x = pd.DataFrame(x)

#model = LinearRegression().set_params(feature_names_in=x.dtypes.index)
# Fit the LinearRegression model
#model = LinearRegression()
#print(model)

#model.fit(x, y)
#x = pd.DataFrame(x)
#y = np.squeeze(pd.DataFrame(y))
#if y.ndim!= 1:
    #raise ValueError("'y' must be 1-dimensional.")


# Check if the number of samples in 'x' and 'y' is the same
#if len(x) != len(y):
    #raise ValueError("The input variables 'x' and 'y' have inconsistent numbers of samples.")

# Fit the LinearRegression model
#model = LinearRegression()
#model.fit(x, y)

#print(model)

print("Residual sum of squares: %.2f"%np.mean((y_hat-y)**2))#Residual sum of squares
print("variance score: %.2f"%regr.score(x,y))#Variance score Degree of freedom:13 Residual sum of squares: 0.020
#In ML (Machine Learning) classification is a supervised learning approach which can be thought of as a means of categorizing
#or classifying some unknown items into a discreate set of classes.
#Classification attempts to learn the relationship between a set of features and a target variable of interest.
#The target attribute in classification is a categorical variable with dicrete values.
#Given a set of training data points along with the target labels,classification determines the class label for an unlabeled test case. 
#We have the types of classification algorithms and machine learning
#They include k-Nearest Neighbors,Support Vector Machines,Decision Trees,Random Forest,Naive Bayes,Logistic Regression,Gradient Boosting, and so on.
#The k-Nearest Neighbors algorithm is one of the most popular
#It is used for both classification and regression tasks.
#The k-Nearest Neighbors algorithm is a classification algorithm that takes a bunch of labeled points and uses them to learn how to label other points.
#This algorithm classifies cases based on their similarity to other cases.
#In k-Nearest Neighbors,data points are near each other are said to be neighbors.
#Thus,the distance between two cases is a measure of their dissimilarity.
#A low value of K causes a highly complex model as well,which might result in overfittingof the model.
#It means the prediction process isn't generalized enough to be used for out-of-sample cases.
#Out-of-sample is data that is outside of the data set used to train the model.
#In other words, it is a data that is not used to train the model.
#Overfitting is bad,as we want a general model that works for any data,not just the training data
#if we choose a very high value of K such as K equals 20 then the mode becomes overly generalized.
#The general solution is to reserve a part of your data for testin the accuracy of the model.
#Then,choose k uquals one and then use the training part for modeling and calculate the accuracy of the model using all samples in your test set.
#Repeat this process until the accuracy of the model is good enough.
#Naereast beightbors analysis can also be used to compute values for a continuous target.
#Evaluation metrics explain the performance of a model.
#Evaluation metrics, provide a key role in the development of a model, as it provides insight to areas that require improvement.
#There are different model evaluation metrics.Some of them are Jaccard Index,F1 Score and Log Loss.
#The confusion matrix shows the model's ability to correctly predict or seperate the classes.
#Precision is a measure of classifier's accuracy when it makes only correct decisions.
#precision=true positive/true positive+false positive
#Recall is a measure of how many of the actual positives were correctly identified.
#Recall=true positive/true positive+false negative
#F1 score is a weighted average of precision and recall.
#F1 score=2*(precision*recall)/(precision+recall)
#Log loss is logarithmically related to the cross-entropy loss.
#log loss is a measure of misclassification.
#log loss=−1/n∑i=1(yi=1)log(1−yi)+(1-yi)log(yi)
#Jaccard coefficient measures the similarity between two sets.
#Jaccard coefficient = intersection of two sets/union of two sets
#Jaccard Index = Jaccard coefficient
#Jaccard Index is a measure of similarity between two sets.
#Jaccard Index = intersection of two sets/union of two sets = intersection of two sets/sum of two sets
#K-Nearest Neighbors is an algorithm for supervised learning.
#Where the data is "trained" with data points corresponding to their classification.
#Once a point is to be predicted,it takes into account its k nearest neighbors.
#Loading the dataset
df=pd.read_csv(r'/run/media/panos/SAMSUNG T7/panag/Documents/ΕΡΓΑΣΤΗΡΙΑΚΕΣ ΑΣΚΗΣΕΙΣ/Python tries/FuelConsumptionCo2.csv')#('F:/panag/Documents/ΕΡΓΑΣΤΗΡΙΑΚΕΣ ΑΣΚΗΣΕΙΣ/Python tries/teleCust1000t.csv')#Reading csv file
df.head()#showing first five rows of the dataframe
#Visualizing the distribution of custcat (target variable)
df['custcat'].value_counts()#Counting the number of customers in each category
df.hist(column='income',bins=50)#Histogram of income column showing the distribution of income
#array([[<matplotlib.axes._subplots.AxesSubplot object at 0x000001A5F0C6B5F8>]], dtype=object)#Array of subplots
df.columns 
#Index(['region', 'tenure', 'age', 'marital', 'address', 'income', 'ed', 'employ', 'retire', 'gender', 'reside', 'custcat'], dtype='object')
y=df['custcat'].values
y[0:5]
x = df.drop('custcat', axis=1).values
#array([1, 4, 3, 1, 3])
#Normalize Data
#Data Standardization give data zero mean and unit variance
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=4)
print('Train set:',x_train.shape,y_train.shape)
print('Test set:',x_test.shape,y_test.shape)
k=4
#Train Model and Predict
neigh=KNeighborsClassifier(n_neighbors=k).fit(x_train,y_train)
neigh
KNeighborsClassifier(algorithm='auto', leaf_size=30, metric='minkowski', metric_params=None, n_jobs=None, n_neighbors=4, p=2, weights='uniform')
y_hat=neigh.predict(x_test)
y_hat[0:5]
#array([1'1'3'4'])
#In multilabel classification,accuracy classification score is a function that computes subset accuracy.
#This function is equal to the jaccard_similarity_score function.
#Essentially,it calculates how closely the actual labels and predicted labels are to each other. 
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=4)
print('Train set:',x_train.shape,y_train.shape)
print('Test set:',x_test.shape,y_test.shape)
#Decision tree
#Decision trees are built by splitting the training set into distinct nodes,where one node contains all of or most of one category of the data.
#Decision trees are about testing an attribute and branching the cases based on the result of the test.
#Decision trees are used in large datasets
#Each internal node corresponds to a test, and each branch corresponds to a result of the test,and each leaf node assigns a patient to a class.
#A decision tree can be used in both classification and regression.
#Decision trees can be used to predict the class of an unknown case.
#A decision tree can be constructed by  considering the attributes one by one.
#First,choose an attribute from our dataset.
#Calculate the significance of the attribute in the splitting of the data.
#Next,split the data based on the value of the best attribute,then go to each branch and repeat it for the rest of the attributes.
#DT(Decision tree) are built using recursive partitioning to classify the data.
#A node in the tree is considered pure if in 100% of the cases,the nodes fall into a specific category of the target field.
#In fact, the method uses recursive partitioning to split the training records into segments by minimizing te impurity at each step.
#Impurity of nodes is calculated by entropy of data in the node. 
#The impurity is calculated using the Gini index. 
#Gini index is the amount of disorder in the data. It is defined as the sum of the probability for each class.
#Gini Index = 1 - pureness of the node i.e., 1-Pureness
#Entropy is the amount of information disorder or the amount of randomness in the data.
#The entropy in the node depends on how much random data is in that node and is calculated for each node.
# Entropy = -1 * (p1 * log2(p1) + p2 * log2(p2) + ... + pn * log2(pn))
#In DT,we're looking for trees that have the smallest entropy in their nodes.
#The entropy is used to measure the randomness in the data.Also it measure the homogeneity of the samples in that node.
#If the entropy is small,then the node is pure.
#If the entropy is large,then the node is not pure.
#If the samples are completely homogeneous,the entropy is 0.
#If the samples are equally divided it has an entropy of 1.
#Information gain is the information that can increase the level of certainly after splitting.
#It is the entropy of a tree before the split minus the weighted entropy after the split by an attribute.
#Information gain is used to measure the randomness in the data.
# Information gain=(entropy of the parent node or entropy before the split)-(weighted entropy of the child nodes Or entropy after the split)
#We can think of information gain and entropy as opposites.
#As entropy of the amount of randomness decreases,the information gain or amount of certainty increases and vice versa.
my_data=pd.read_csv(r'/run/media/panos/SAMSUNG T7/panag/Documents/ΕΡΓΑΣΤΗΡΙΑΚΕΣ ΑΣΚΗΣΕΙΣ/Python tries/drug200.csv',delimiter=',')#Reading csv file
my_data[0:5]#showing first five rows of the dataframe
#pre-processing
x=my_data# Check if 'Na-to-K' is in the columns of my_data before accessing it
if 'Na-to-K' in my_data.columns:
    x = my_data[['Age', 'Sex', 'BP', 'Cholesterol', 'Na-to-K']].values
    # Proceed with the rest of your code
else:
    print("'Na-to-K' column not found in the DataFrame.")
    # Handle the case where 'Na-to-K' column is missing[['Age', 'Sex', 'BP', 'Cholesterol', 'Na-to-K']].values
x[0:5]
#array([[23, 'F', 'HIGH', 'HIGH', 23.355],
#       [47, 'M', 'LOW', 'HIGH', 10.113999999999999],
#       [28, 'F', 'NORMAL', 'HIGH', 7.79799999999999],
#       [61, 'F', 'LOW', 'HIGH', 18.043]], dtype=object)
Le_sex=preprocessing.LabelEncoder()#label encoder converts categorical variable into numerical values
Le_sex.fit(['F','M'])#converts all the 'F's and 'M's to 0 and 1 respectively
#x[:,1]=Le_sex.transform(z=x.iloc[:, 1] = Le_sex.transform(x.iloc[:, 1]) = Le_sex.transform(x.iloc[:, 1])[:,1])#transforms all the 'F's and 'M's to 0 and 1 respectively
# Transform the values in the specified column using Le_sex
transformed_values = Le_sex.transform(x.iloc[:, 1])

# Assign the transformed values back to the specified column in x
x.iloc[:, 1] = transformed_values
Le_BP=preprocessing.LabelEncoder()#label encoder converts categorical variable into numerical values
Le_BP.fit(['LOW','NORMAL','HIGH'])#converts all the 'F's and 'M's to 0 and 1 respectively
# Transform the values in the specified column using Le_BP
transformed_values2 = Le_BP.transform(x.iloc[:, 2])

# Assign the transformed values back to the specified column in x
x.iloc[:, 2] = transformed_values2
Le_Chol=preprocessing.LabelEncoder()#label encoder converts categorical variable into numerical values
Le_Chol.fit(['NORMAL','HIGH'])#converts all the 'F's and 'M's to 0 and 1 respectively
#x[:,3]=Le_Chol.transform(x[:,3])#transforms all the 'F's and 'M's to 0 and 1 respectively
# Transform the values in the specified column using Le_BP
transformed_values3 = Le_BP.transform(x.iloc[:, 3])

# Assign the transformed values back to the specified column in x
x.iloc[:, 3] = transformed_values3
x[0:5]#shows first five rows of the array with transformed variables
# array([[23, 0, 0, 0, 23.355],
#        [47, 1, 1, 0, 10.113999999999999],
#        [28, 0, 2, 0, 7.79799999999999],
#        [61, 0, 1, 0, 18.043]], dtype=object)
#fill the target variable
y=my_data["Drug"]#extracting the target variable from the dataframe
y[0:5]#shows first five rows of the array with transformed variables
#array(['drugY', 'drugC', 'drugC', 'drugX', 'drugY'], dtype=object)
#Setting up the decision tree
x_trainset,x_testset,y_trainset,y_testset=train_test_split(x,y,test_size=0.3,random_state=3)#splitting the data into train and test sets classifier 
#Modeling
drugTree=DecisionTreeClassifier(criterion="entropy",max_depth=4)#creating the decision tree instance
drugTree#prints the decision tree model
#DecisionTreeClassifier(class_weight=None, criterion='entropy', max_depth=4,
#            max_features=None, max_leaf_nodes=None,
#            min_impurity_decrease=0.0,
#            min_samples_leaf=1, min_samples_split=2,
#            min_weight_fraction_leaf=0.0, presort="deprecated", random_state=None,
#            splitter='best')#prints the decision tree model
le = LabelEncoder()#label encoder converts categorical variable into numerical values
le.fit(y_trainset)#converts all the 'drugY','drugC','drugX','drugA','drugB' to 0,1,2,3,4 respectively
y_trainset = le.transform(y_trainset)#converts all the 'drugY','drugC','drugX','drugA','drugB' to 0,1,2,3,4 respectively

# Initialize the label encoder
#label_encoder = LabelEncoder()

# Encode the target variable y_trainset
#y_trainset_encoded = label_encoder.fit_transform(y_trainset)
#drugTree.fit(x_trainset,y_trainset)#fitting the decision tree model on the train set
#DecisionTreeClassifier(class_weight=None, criterion='entropy', max_depth=4,
#            max_features=None, max_left_nodes=None,
#            min_impurity_decrease=0.0, min_impurity_split=None,
#            min_samples_leaf=1, min_samples_split=2,
#            min_weight_fraction_leaf=0.0, presort="deprecated", random_state=None,
#            splitter='best')
#Prediction


# Initialize OneHotEncoder and LabelEncoder
onehot_encoder = OneHotEncoder()
label_encoder = LabelEncoder()

# Convert categorical labels to numerical labels
y_trainset_encoded = label_encoder.fit_transform(y_trainset)

# Reshape y_trainset_encoded for compatibility with OneHotEncoder
y_trainset_encoded_reshaped = y_trainset_encoded.reshape(-1, 1)

# Fit and transform the encoded labels using OneHotEncoder
y_trainset_onehot_encoded = onehot_encoder.fit_transform(y_trainset_encoded_reshaped).toarray()
# Load the dataset
data_url = "https://raw.githubusercontent.com/kvinlazy/Dataset/master/drug200.csv"
df = pd.read_csv(data_url)

# Display the first few rows of the dataframe
print(df.head())
# Separate features and target variable
X = df.drop(columns=['Drug'])
y = df['Drug']

# One-hot encode categorical features
X_encoded = pd.get_dummies(X, columns=['Sex', 'BP', 'Cholesterol'])

# Encode target variable
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

# Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X_encoded, y_encoded, test_size=0.2, random_state=42)

# Now, you can proceed to train your model using X_train and y_train
# and evaluate it using X_test and y_test
# fit the DecisionTreeClassifier with the training data
#drugTree.fit(x_trainset, y_trainset_onehot_encoded)


# Initialize the OneHotEncoder
#encoder = OneHotEncoder()

# Fit and transform the target variable y_trainset
#y_trainset_encoded = encoder.fit_transform(y_trainset.reshape(-1, 1)).toarray()
# fit the DecisionTreeClassifier with the training data
#drugTree.fit(x_trainset, y_trainset_encoded)  
# Make predictions on the test set
#predTree = drugTree.predict(x_testset)
#drugTree.predict(x_testset)#predicting the test set
#print(predTree[0:5])#shows first five rows of the array with transformed variables
#print(y_testset[0:5])#shows first five rows of the array with transformed variables
#Evaluation
#Visualize the decision tree
#dot_data=StringIO()#for Python 3 compatibility
#filename="drugtree.png"#name of the file where you want to save the graph
#feautureNames=my_data.columns[0:5]#names of the features in the dataset
#targetNames=my_data["Drug"].unique().tolist()#names of the target classes in the dataset
#out=tree.export_graphviz(drugTree,feature_names=feautureNames, out_file=dot_data, class_names= np.unique(y_trainset), filled=True, special_characters=True,rotate=False)#visualize the decision tree 
#graph=pydotplus.graph_from_dot_data(dot_data.getvalue())#visualize the decision tree 
#graph.write_png(filename)#visualize the decision tree 
#img=plt.imread(filename)#visualize the decision tree 
#plt.figure(figsize=(100,200))#Setting figure size  for displaying the image
#plt.imshow(img,interpolation='nearest')#visualize the decision tree
# Separate features and target variable
# Separate features and target variable
# Separate features and target variable
X = df.drop(columns=['Drug'])
y = df['Drug']

# Encode target variable
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

# One-hot encode categorical features
X_encoded = pd.get_dummies(X, columns=['Sex', 'BP', 'Cholesterol'])

# Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X_encoded, y_encoded, test_size=0.2, random_state=42)

# Initialize the Decision Tree Classifier
drug_tree = DecisionTreeClassifier()

# Train the classifier
drug_tree.fit(X_train, y_train)

# Predict on the test set
y_pred = drug_tree.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Visualize the decision tree
plt.figure(figsize=(12, 8))#Setting figure size  for displaying the image
plot_tree(drug_tree, feature_names=X_encoded.columns, class_names=label_encoder.classes_, filled=True)# Visualize the decision tree
plt.show()# Visualize the decision tree

# Open the PNG image
img = Image.open(r"/run/media/panos/SAMSUNG T7/panag/Documents/ΕΡΓΑΣΤΗΡΙΑΚΕΣ ΑΣΚΗΣΕΙΣ/Figure_2.png")

# Display the image
img.show()

#Logistic Regression Model is used for binary classification.

#\\dsl-ac56u\panag (at sda1)\Documents\ΕΡΓΑΣΤΗΡΙΑΚΕΣ ΑΣΚΗΣΕΙΣ\Logistic Regression.png
Churn_url="https://raw.githubusercontent.com/kvinlazy/Dataset/master/ChurnData.csv"

# Read the CSV file with error handling
try:
    Churn_df = pd.read_csv(Churn_url, on_bad_lines='skip')
    print(Churn_df.head())
except pd.errors.ParserError as e:
    print(f"ParserError: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
    
Churn_df=Churn_df[['tenure','age','address','income','ed','employ','equip','callcard','wireless','churn']]
Churn_df['churn']=Churn_df['churn'].astype('int')
print(Churn_df.head())
X_train,X_test,Y_train,Y_test=train_test_split(x,y,test_size=0.2,random_state=4)
print("Train set: ",X_train)
print("Test set: ",X_test.shape,Y_test.shape)
# Fill the target variable
y = my_data["Drug"]

# Separate features and target variable
x = my_data.drop(columns=['Drug']).values

# Apply StandardScaler to the features
scaler = preprocessing.StandardScaler()
X = scaler.fit_transform(x)
x[0:5]
# X_train,X_test,Y_train,Y_test=train_test_split(x,y,test_size=0.2,random_state=4)
# print("Train set: ",X_train)
# print("Test set: ",X_test.shape,Y_test.shape)
# def plot_confusion_matrix(Blues,cm,classes,normalize=False,title="Confusion matrix",cmap=plt.cm):
#     if normalize:
#         cm=cm.astype('float')/cm.sum(axis=1)[:,np.newaxis]
#         print("Normalized confusion matrix")
#     else:
#         print("Confusion matrix, without normalization")
#     print(cm)
#     plt.imshow(cm,interpolation='nearest',cmap=cmap)
#     plt.title(title)
#     plt.colorbar()
#     tick_marks=np.arange(len(classes))
#     plt.xticks(tick_marks,classes,rotation=45)
#     plt.yticks(tick_marks,classes)
#     fmt=".2f" if normalize else "d"
#     thresh=cm.max()/2
#     for i,j in itertools.product(range(cm.shape[0]),range(cm.shape[1])):
#         plt.text(j,i,format(cm[i,j],fmt),horizontalalignment="center",color="white" if cm[i,j]>thresh else "black")
#     plt.tight_layout()
#     plt.ylabel("True label")
#     plt.xlabel("Predicted label")
#     print(confusion_matrix(y_test,y_hat,labels=(1,0)))
#     plt.show()
# #Compute confusion matrix
# cnf_matrix=confusion_matrix(y_test,y_hat,labels=(1,0))
# np.set_printoptions(precision=2)
# #Plot non-normalized confusion matrix
# plt.figure()
# plot_confusion_matrix(cnf_matrix,classes=["churn=1,churne"],normalize=False,title="Confusion matrix")
# plt.show()
# Split data into training and testing sets
# X_train, X_test, Y_train, Y_test = train_test_split(x, y, test_size=0.2, random_state=4)
# print("Train set: ", X_train.shape)
# print("Test set: ", X_test.shape, Y_test.shape)

# # Assuming model is already trained
# # Generate predictions for the test set
# y_hat = model.predict(X_test)
# print("Predictions shape: ", y_hat.shape)

# # Define function to plot confusion matrix
# def plot_confusion_matrix(cm, classes, normalize=False, title="Confusion matrix", cmap=plt.cm.Blues):
#     if normalize:
#         cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
#         print("Normalized confusion matrix")
#     else:
#         print("Confusion matrix, without normalization")
    
#     print(cm)
#     plt.imshow(cm, interpolation='nearest', cmap=cmap)
#     plt.title(title)
#     plt.colorbar()
#     tick_marks = np.arange(len(classes))
#     plt.xticks(tick_marks, classes, rotation=45)
#     plt.yticks(tick_marks, classes)
    
#     fmt = ".2f" if normalize else "d"
#     thresh = cm.max() / 2
#     for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
#         plt.text(j, i, format(cm[i, j], fmt), horizontalalignment="center",
#                  color="white" if cm[i, j] > thresh else "black")
    
#     plt.tight_layout()
#     plt.ylabel("True label")
#     plt.xlabel("Predicted label")
#     plt.show()

# # Compute confusion matrix
# cnf_matrix = confusion_matrix(Y_test, y_hat, labels=(1, 0))
# np.set_printoptions(precision=2)

# # Plot non-normalized confusion matrix
# plt.figure()
# plot_confusion_matrix(cnf_matrix, classes=["churn=1", "churn=0"], normalize=False, title="Confusion matrix")
# plt.show()
# Assuming x and y are already defined as your features and target variables
# For example:
# x = ... (your feature data)
# y = ... (your target data)

# Split data into training and testing sets
# X_train, X_test, Y_train, Y_test = train_test_split(x, y, test_size=0.2, random_state=4)
# print("Train set shape: ", X_train.shape)
# print("Test set shape: ", X_test.shape, Y_test.shape)

# # **Added the model training section**
# # Train a model
# model = LogisticRegression()  # Initialize the model
# model.fit(X_train, Y_train)  # Train the model

# # **Added the prediction section**
# # Generate predictions for the test set
# y_hat = model.predict(X_test)
# print("Predictions shape: ", y_hat.shape)

# # Define function to plot confusion matrix
# def plot_confusion_matrix(cm, classes, normalize=False, title="Confusion matrix", cmap=plt.cm.Blues):
#     if normalize:
#         cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
#         print("Normalized confusion matrix")
#     else:
#         print("Confusion matrix, without normalization")
    
#     print(cm)
#     plt.imshow(cm, interpolation='nearest', cmap=cmap)
#     plt.title(title)
#     plt.colorbar()
#     tick_marks = np.arange(len(classes))
#     plt.xticks(tick_marks, classes, rotation=45)
#     plt.yticks(tick_marks, classes)
    
#     fmt = ".2f" if normalize else "d"
#     thresh = cm.max() / 2
#     for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
#         plt.text(j, i, format(cm[i, j], fmt), horizontalalignment="center",
#                  color="white" if cm[i, j] > thresh else "black")
    
#     plt.tight_layout()
#     plt.ylabel("True label")
#     plt.xlabel("Predicted label")
#     plt.show()

# # Compute confusion matrix
# cnf_matrix = confusion_matrix(Y_test, y_hat, labels=[1, 0])
# np.set_printoptions(precision=2)

# # Plot non-normalized confusion matrix
# plt.figure()
# plot_confusion_matrix(cnf_matrix, classes=["churn=1", "churn=0"], normalize=False, title="Confusion matrix")
# plt.show()
# Assuming x and y are already defined as your features and target variables
# For example:
# x = ... (your feature data)
# y = ... (your target data)

# Ensure y contains only integers or strings, not a mix
# Convert y to integers if it's not already
# y = y.astype(str)  # or y = y.astype(str) if your labels are strings

# # Split data into training and testing sets
# X_train, X_test, Y_train, Y_test = train_test_split(x, y, test_size=0.2, random_state=4)
# print("Train set shape: ", X_train.shape)
# print("Test set shape: ", X_test.shape, Y_test.shape)

# # Train a model
# model = LogisticRegression()  # Initialize the model
# model.fit(X_train, Y_train)  # Train the model

# # Generate predictions for the test set
# y_hat = model.predict(X_test)
# print("Predictions shape: ", y_hat.shape)

# # Define function to plot confusion matrix
# def plot_confusion_matrix(cm, classes, normalize=False, title="Confusion matrix", cmap=plt.cm.Blues):
#     if normalize:
#         cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
#         print("Normalized confusion matrix")
#     else:
#         print("Confusion matrix, without normalization")
    
#     print(cm)
#     plt.imshow(cm, interpolation='nearest', cmap=cmap)
#     plt.title(title)
#     plt.colorbar()
#     tick_marks = np.arange(len(classes))
#     plt.xticks(tick_marks, classes, rotation=45)
#     plt.yticks(tick_marks, classes)
    
#     fmt = ".2f" if normalize else "d"
#     thresh = cm.max() / 2
#     for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
#         plt.text(j, i, format(cm[i, j], fmt), horizontalalignment="center",
#                  color="white" if cm[i, j] > thresh else "black")
    
#     plt.tight_layout()
#     plt.ylabel("True label")
#     plt.xlabel("Predicted label")
#     plt.show()

# # Ensure labels are integers if the labels in Y_test and y_hat are integers
# # If they are strings, convert the labels to strings, e.g., labels=["1", "0"]
# cnf_matrix = confusion_matrix(Y_test, y_hat, labels=[1, 0])
# np.set_printoptions(precision=2)

# # Plot non-normalized confusion matrix
# plt.figure()
# plot_confusion_matrix(cnf_matrix, classes=["churn=1", "churn=0"], normalize=False, title="Confusion matrix")
# plt.show()
# Assuming x and y are already defined as your features and target variables
# For example:
# x = ... (your feature data)
# y = ... (your target data)

# Ensure y contains only strings
y = y.astype(str)

# Split data into training and testing sets
X_train, X_test, Y_train, Y_test = train_test_split(x, y, test_size=0.2, random_state=4)
print("Train set shape: ", X_train.shape)
print("Test set shape: ", X_test.shape, Y_test.shape)

# Train a model
model = LogisticRegression()  # Initialize the model
model.fit(X_train, Y_train)  # Train the model

# Generate predictions for the test set
y_hat = model.predict(X_test)
print("Predictions shape: ", y_hat.shape)

# Define function to plot confusion matrix
def plot_confusion_matrix(cm, classes, normalize=False, title="Confusion matrix", cmap=plt.cm.Blues):
    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        print("Normalized confusion matrix")
    else:
        print("Confusion matrix, without normalization")
    
    print(cm)
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)
    
    fmt = ".2f" if normalize else "d"
    thresh = cm.max() / 2
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, format(cm[i, j], fmt), horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")
    
    plt.tight_layout()
    plt.ylabel("True label")
    plt.xlabel("Predicted label")
    plt.show()

# Compute confusion matrix
# Ensure labels are strings if the labels in Y_test and y_hat are strings
cnf_matrix = confusion_matrix(Y_test, y_hat, labels=['drugY', 'drugX', 'drugA', 'drugB', 'drugC'])
np.set_printoptions(precision=2)

# Plot non-normalized confusion matrix
plt.figure()
plot_confusion_matrix(cnf_matrix, classes=['drugY', 'drugX', 'drugA', 'drugB', 'drugC'], normalize=False, title="Confusion matrix")
plt.show()
print(classification_report(Y_test,y_hat))

#Vector Machine(SVM)

#Vector Machine(SVM) which is used for classification.

#A Support Vector Machine is a supervised algorithm that can classify cases by finding a separator.
#SVM works by first mapping data to a high dimensional feature space so that data points can be categorized, 
# even when the data are not otherwise linearly separable.Then, a separator is estimated for the data.
#The data should be transformed in such a way that a separator could be drawn as a hyperplane.
#Basically,mapping data into a higher-dimensional space is called, kernelling.
#The math func used for the transformation is known as the kernel function and can be of different types, such as linear,
#polynomial,Radial Basis Function, or RBF,and sigmoid.
#The disadvantages of SVMs include the fact that the algorithm is prone for over-fitting if the number of features is much greater than the number of samples.
# Also,SVMs don't directly provide probability estimates,which are desirable in most classification problems.
# Finally, SVMs aren't very efficient computationally if your dataset is very big,such as when you have more than 1000 rows.
#SVM is good for image analysis tasks,such as image classification and handwritten digit recognition.
#SVM is also good for text classification,such as spam filtering and sentiment analysis.


# cell_url="F:\panag\Documents\ΕΡΓΑΣΤΗΡΙΑΚΕΣ ΑΣΚΗΣΕΙΣ\Python tries\cell_samples.csv"
# cell_df = pd.read_csv(cell_url,on_bad_lines='skip')
# print(cell_df.head())
# cell_df['Class']=cell_df['Class'].astype('int')
# y=np.asarray(cell_df['Class'])
# y[0:5]
# x_train,x_test,y_train,y_test-train_test_split(x,y,test_size=0.2,random_state=4)
# print('Train set:',x_train.shape,y_train.shape)
# print('Test set:',x_test.shape,y_test.shape)

# #SVM

# # Load the dataset
# cell_url = "F:\\panag\\Documents\\ΕΡΓΑΣΤΗΡΙΑΚΕΣ ΑΣΚΗΣΕΙΣ\\Python tries\\cell_samples.csv"
# cell_df = pd.read_csv(cell_url, on_bad_lines='skip')
# print(cell_df.head())

# # Ensure 'Class' column is of integer type
# cell_df['Class'] = cell_df['Class'].astype('int')

# # Check for missing values and drop rows with any missing values
# cell_df.dropna(inplace=True)

# # Assuming all columns except 'Class' are features
# X = cell_df.drop(columns=['Class']).values
# y = cell_df['Class'].values

# # Check shapes of X and y to confirm they match
# print(f"Shape of X: {X.shape}")
# print(f"Shape of y: {y.shape}")

# # Split the dataset into training and testing sets
# x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=4)

# print('Train set:', x_train.shape, y_train.shape)
# print('Test set:', x_test.shape, y_test.shape)

# clf=svm.SVC(kernel='rbf')
# clf.fit(x_train,y_train)
# DSVC(C=1.0,break_ties=False,cache_size=200,class_weight=None,coefp=0.0,
#     decision_function_shape='ovr',degree=3,gamma='scale',kernel='rbf',
#     max_iter=-1,probability=False,random_state=None,shrinking=True,
#     tol=0.001,verbose=False)

# y_hat=clf.predict(x_test)

# print(y_hat[0:5])

# #Compute confusion matrix
# cnf_matrix=confusion_matrix(y_test,y_hat,labels=(2,4))
# np.set_printoptions(precision=2)
# print(classification_report(y_test,y_hat))
# #Plot non-normalized confusion matrix
# plt.figure()
# plot_confusion_matrix(cnf_matrix,classes=['Benign(2)','Malignant(4)'],normalize=False,title="Confusion matrix")
# f1_score(y_test,y_hat,average='weighted')
# jaccard_score(y_test,y_hat)


#Define a function to plot the confusion matrix
def plot_confusion_matrix(cm, classes, normalize=False, title='Confusion matrix', cmap=plt.cm.Blues):
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)

    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        print("Normalized confusion matrix")
    else:
        print('Confusion matrix, without normalization')

    print(cm)

    thresh = cm.max() / 2.
    for i, j in np.ndindex(cm.shape):
        plt.text(j, i, format(cm[i, j], '.2f'),
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')

# Load the dataset
cell_url = r"/run/media/panos/SAMSUNG T7/panag/Documents/ΕΡΓΑΣΤΗΡΙΑΚΕΣ ΑΣΚΗΣΕΙΣ/Python tries/cell_samples.csv" # "F:\\panag\\Documents\\ΕΡΓΑΣΤΗΡΙΑΚΕΣ ΑΣΚΗΣΕΙΣ\\Python tries\\cell_samples.csv"
cell_df = pd.read_csv(cell_url, on_bad_lines='skip')
print(cell_df.head())

# Replace non-numeric values with NaN and drop rows with NaN values
cell_df.replace('?', np.nan, inplace=True)
cell_df.dropna(inplace=True)

# Ensure 'Class' column is of integer type
cell_df['Class'] = cell_df['Class'].astype('int')

# Assuming all columns except 'Class' are features, convert them to numeric
X = cell_df.drop(columns=['Class']).apply(pd.to_numeric).values
y = cell_df['Class'].values

# Check shapes of X and y to confirm they match
print(f"Shape of X: {X.shape}")
print(f"Shape of y: {y.shape}")

# Split the dataset into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=4)

print('Train set:', x_train.shape, y_train.shape)
print('Test set:', x_test.shape, y_test.shape)

# Create and train the SVM model
clf = svm.SVC(kernel='rbf')
clf.fit(x_train, y_train)

# Make predictions
y_hat = clf.predict(x_test)

print(y_hat[0:5])

# Compute confusion matrix
cnf_matrix = confusion_matrix(y_test, y_hat, labels=[2, 4])
np.set_printoptions(precision=2)
print(classification_report(y_test, y_hat))

# Plot non-normalized confusion matrix
plt.figure()
plot_confusion_matrix(cnf_matrix, classes=['Benign(2)', 'Malignant(4)'], normalize=False, title="Confusion matrix")

# Calculate and print the F1 and Jaccard scores
f1 = f1_score(y_test, y_hat, average='weighted')
jaccard = jaccard_score(y_test, y_hat, average='weighted')

print(f"F1 Score: {f1}")
print(f"Jaccard Score: {jaccard}")

plt.show()

#Clusters

# A general segmentation process isn't usually feasible for large volumes of very data,
# therefore,you need an analytical approach to deriving segments and groups from large datasets.
#Clustering can group data only unsupervised,based on the similarity of customers to each other.
#Now,we can greate a  profile for each group,considering the common characteristics of each cluster.
#The goal of clustering is to identify patterns or structures in the data that are not immediately apparent.
#Clustering is a type of unsupervised machine learning.
#Clustering is a method of unsupervised machine learning that can be used to group similar data points into clusters.
#Finally,we can assign each individual in our dataset to one of these groups or segments of customers.
#A cluster is a group of data points or 
# objects in a dataset that are similar to other objects in the group,
# and dissimilar to data points in other clusters.
#Classification algorithms predict categorical classed labels.
#This means assigning instances to predefined classes such as defaulted or not defaulted.
#Generally speaking,classification is a supervised learning where each training data instance belongs to a particular class.
#In clustering however,the data is unlabeled and the process is unsupervised.

# K-means Clustering

# K-Means can group data only unsupervised based on the similarity of customers to each other.
# Generally, K-Means is a type of partitioning clustering, that is,
# it divides the data into K non-overlapping subsets or clusters without any cluster internal structure or labels.
# This means it's an unsupervised algorithm.
# K-Means is a method of unsupervised machine learning that can be used to group similar data points into clusters.
# Objects within a cluster are very similar, and objects across different clusters are very different or dissimilar.
# K-Means tries to minimize the intra-cluster distances and maximize the inter-cluster distances
# There're other dissimilarity measures as well that can be used for this purpose,but it is highly dependent on datatype and also the domain that clustering is done for it.
# For example, you may use Euclidean distance,Cosine similarity,Average distance, and so on.
# Indeed,the similarity measure highly controls how the clusters are formed,
# so it is recommended to understand the domain knowledge of your dataset and datatype of features and then choose the meaningful distance measurement.
# In the first step, we should determine the number of clusters.
# The key concept of the K-Means algorithm is that it randomly picks a center point for each cluster.
# It means we must initialize K which represents the number of clusters.
# The center point is called the centroid of the cluster and should be of the same feature size of our customer feature set.
# The number of clusters is the number of clusters we want to form.
# The process of K-Means is as follows:
# 1. Randomly assign each customer to a cluster
# 2. Compute the centroid of each cluster
# 3. Assign each customer to a cluster
# 4. Repeat until the clusters converge
#There are two  approaches to choose these centroids:
# 1. We can randomly choose three observations out of the dataset and use these observations as the initial means.
# 2. We can create three random points as centroids of the clusters which is our choice that is shown in the  plot with  red clolor.
# After the initialization step which was defining the centroid of each cluster,
# we have to assign each customer to the closest center.
# For this purpose, we have to  calculate the distance of each data point or
# in our case each customer from the centroid points.
# Therefore, you will form a matrix where each row represents the distance of a customer from each centroid.
# It is called the Distance Matrix.
# The main objective of K-Means clustering is to minimize the distance of data points from the centroid of this cluster
# and maximize the distance of data points from the other cluster centroids.
# We can use the distance matrix to find the nearest centroid to data points.
# Finding the closest centroids for each data points,
# we assign each data point to that cluster.
# In other words, all the customers will fall to a cluster based on their distance from centroids.
# We can easily say that it doesn't result in good clusters since the centroids were chosen randomly from the first.
# Indeed,the model would have a high error.
# Here, Error is the total distance of each point from its centroid.
# It can be shown as a within-cluster sum of squares error.
# Intuitively, we try to reduce this error.
# It means we should shape lusters in such a way taht the total distance of all members of a cluster from its centroid be minimized.
# Please note that whenever a centroidmoves, each point's distance to the centroid needs to be measured again.

# # We need to set up a random seed.
# np.random.seed(0)
# n_samples=5000
# centers=[[4,4],[-2,-1],[2,-3],[1,1]]
# cluster_std=0.9

# X,y=make_blobs(n_samples=n_samples,centers=centers,cluster_std=cluster_std)

# plt.scatter(X[:,0],X[:,1],marker='.')

# KMeans.fit(x) - KMeans (algorithm='auto',copy_x=True,init='k-means++',max_iter=300,n_clusters=4,n_init=12,n_jobs=None,precompute_distances='auto',random_state=None,tol=0.0001,verbose=0)
# k_means_labels=KMeans.labels_
# k_clusters_centers=KMeans.cluster_centers_

# #Initialize the plot with the specified dimensions.
# fig=plt.figure(figsize=(6,4))

# #Colors uses a color map, which will produce an array of colors based on
# # the number of labels there are. We use set(k_means_labels) to get the unique labels

# colors=plt.cm.Spectral(np.linspace(0,1,len(set(k_means_labels))))

# #Create a plot
# ax=plt.subplot(1,1,1)

# #For loop that plots the data points and centroids
# #k will range from 0-3, which will match the possible clusters that each point is in
# #data point is in.
# for k,col in zip(range(len(centers)),colors):
#     #create a list of all points that are in the cluster
#     #in the cluster (ex. cluster 0) are labeled as true,else they are
#     # labeles are false.
#     my_members=(k_means_labels==k)
#     #Define the centroid,or cluster center
#     cluster_center=KMeans.cluster_centers_[k]
    
#     #title of the plot
#     ax.set_title('KMeans')
    
#     #plot the datapoints with color col
#     ax.plot(X[my_members,0],X[my_members,1],'w',markerfacecolor=col,marker='.')
    
#     #plot the centroids with specified color, but with a darker outline
#     ax.plot(cluster_center[0],cluster_center[1],'o',markerfacecolor=col,markeredgecolor='k',markersize=6)
    
#     #remove x-axis ticks
#     ax.set_xticks(())
    
#     #remove y-axis ticks
#     ax.set_yticks(())
    
#     plt.show()
    
#     #set the y-axis label
#     ax.set_ylabel('Y')
    
#     #set the x-axis label
#     ax.set_xlabel('X')
    
#     plt.show()
    
    
 
# Set up a random seed
np.random.seed(0)

# Parameters
n_samples = 5000
centers = [[4, 4], [-2, -1], [2, -3], [1, 1]]
cluster_std = 0.9

# Generate the dataset
X, y = make_blobs(n_samples=n_samples, centers=centers, cluster_std=cluster_std)

# Scatter plot of the data
plt.scatter(X[:, 0], X[:, 1], marker='.')
plt.show()

# KMeans clustering
kmeans = KMeans(n_clusters=4, init='k-means++', n_init=12, max_iter=300, random_state=0)
kmeans.fit(X)
k_means_labels = kmeans.labels_
k_clusters_centers = kmeans.cluster_centers_

# Initialize the plot with the specified dimensions
fig = plt.figure(figsize=(6, 4))

# Colors uses a color map, which will produce an array of colors based on the number of labels there are.
colors = plt.cm.Spectral(np.linspace(0, 1, len(set(k_means_labels))))

# Create a plot
ax = plt.subplot(1, 1, 1)

# For loop that plots the data points and centroids
for k, col in zip(range(len(centers)), colors):
    # Create a list of all points that are in the cluster
    my_members = (k_means_labels == k)
    # Define the centroid, or cluster center
    cluster_center = k_clusters_centers[k]
    
    # Plot the datapoints with color col
    ax.plot(X[my_members, 0], X[my_members, 1], 'w', markerfacecolor=col, marker='.')
    
    # Plot the centroids with specified color, but with a darker outline
    ax.plot(cluster_center[0], cluster_center[1], 'o', markerfacecolor=col, markeredgecolor='k', markersize=6)
    
# Title of the plot
ax.set_title('KMeans')

# Remove x-axis and y-axis ticks
ax.set_xticks(())
ax.set_yticks(())

# Set the axis labels
ax.set_xlabel('X')
ax.set_ylabel('Y')

plt.show()    

# Customer segmentation is the practice of partitionig a customer base into groups of individuals that have similar characteristics.
# It is a significant strategy as a business can target these specific groups of customers and effectively allocate marketing resources.

# cust_df=pd.read_csv("F:\panag\Documents\ΕΡΓΑΣΤΗΡΙΑΚΕΣ ΑΣΚΗΣΕΙΣ\Python tries\Cust_Segmentation.csv")
# print(cust_df.head())

# # Normalizing over the standard deviation
# # Normalization is a statistical method that helps mathematical-based algorithms to interpret features with different magnitudes and distributions equally.
# x=df.values[:,1:]
# x=np.nan_to_num(x)
# Clus_dataSet - StandardScaler().fit_transform(x)
# # Modeling
# clusterNum=3
# k_means=KMeans(init="k-means++",n_clusters=clusterNum,n_init=12)
# k_means.fit(x)
# labels=k_means.labels_
# print(labels)
# # Insights, we assign  the labels to each row in dataframe
# df["Clus_km"]=labels
# df.head(5)

# df.groupby('Clus_km').mean()

# print(labels)

# area=np.pi + (x[:,1])**2
# plt.scatter(x[:, ®], [:,3],starea,c-labels.astype (np.float), alpha=0.5)
# plt.xlabel('Age',fontsize=18)
# plt.ylabel('Income',fontsize=16)
# plt.show()

# fig=plt.figure(1,figsize=(8,6))
# plt.clf()
# ax=Axes3D(fig,rect=[0,0,.95,1],elev=48,azim=134)
# plt.cla()

# # plt.ylabel('Age',fontsize=18)
# # plt.xlabel('Income',fontsize=16)
# # plt.zlabel('Education',fontsize=16)
# ax.set_xlabel('Education')
# ax.set_xlabel('Age')
# ax.set_xlabel('Income')

# ax.scatter(x[:,1],x[:,0],x[:,3],c=labels.astype(np.float))

# # Load the dataset
# cust_df = pd.read_csv("F:\\panag\\Documents\\ΕΡΓΑΣΤΗΡΙΑΚΕΣ ΑΣΚΗΣΕΙΣ\\Python tries\\Cust_Segmentation.csv")
# print(cust_df.head())

# # Normalizing over the standard deviation
# x = cust_df.values[:, 1:]  # Skipping the first column assuming it's an ID or non-numeric
# x = np.nan_to_num(x)
# clus_dataSet = StandardScaler().fit_transform(x)

# # Modeling
# clusterNum = 3
# k_means = KMeans(init="k-means++", n_clusters=clusterNum, n_init=12)
# k_means.fit(clus_dataSet)
# labels = k_means.labels_
# print(labels)

# # Assign the labels to each row in the dataframe
# cust_df["Clus_km"] = labels
# print(cust_df.head(5))

# # Grouping by clusters and calculating the mean
# cluster_means = cust_df.groupby('Clus_km').mean()
# print(cluster_means)

# # Plotting
# area = np.pi * (x[:, 1] ** 2)  # Bubble sizes based on some feature, modify as needed
# plt.scatter(x[:, 0], x[:, 3], s=area, c=labels.astype(np.float), alpha=0.5)
# plt.xlabel('Age', fontsize=18)
# plt.ylabel('Income', fontsize=16)
# plt.show()

# # 3D plot
# fig = plt.figure(1, figsize=(8, 6))
# ax = fig.add_subplot(111, projection='3d')
# ax.scatter(x[:, 1], x[:, 0], x[:, 3], c=labels.astype(np.float))
# ax.set_xlabel('Education')
# ax.set_ylabel('Age')
# ax.set_zlabel('Income')
# plt.show()

# # Load the dataset
# cust_df = pd.read_csv("F:\\panag\\Documents\\ΕΡΓΑΣΤΗΡΙΑΚΕΣ ΑΣΚΗΣΕΙΣ\\Python tries\\Cust_Segmentation.csv")
# print(cust_df.head())

# # Extracting only numeric columns for clustering
# numeric_columns = cust_df.select_dtypes(include=[np.number]).columns
# x = cust_df[numeric_columns].values

# # Normalizing over the standard deviation
# x = np.nan_to_num(x)
# clus_dataSet = StandardScaler().fit_transform(x)

# # Modeling
# clusterNum = 3
# k_means = KMeans(init="k-means++", n_clusters=clusterNum, n_init=12)
# k_means.fit(clus_dataSet)
# labels = k_means.labels_
# print(labels)

# # Assign the labels to each row in the dataframe
# cust_df["Clus_km"] = labels
# print(cust_df.head(5))

# # Grouping by clusters and calculating the mean
# cluster_means = cust_df.groupby('Clus_km').mean()
# print(cluster_means)

# # Plotting
# area = np.pi * (x[:, 1] ** 2)  # Bubble sizes based on some feature, modify as needed
# plt.scatter(x[:, 0], x[:, 3], s=area, c=labels.astype(np.float), alpha=0.5)
# plt.xlabel('Age', fontsize=18)
# plt.ylabel('Income', fontsize=16)
# plt.show()

# # 3D plot
# fig = plt.figure(1, figsize=(8, 6))
# ax = fig.add_subplot(111, projection='3d')
# ax.scatter(x[:, 1], x[:, 0], x[:, 3], c=labels.astype(np.float))
# ax.set_xlabel('Education')
# ax.set_ylabel('Age')
# ax.set_zlabel('Income')
# plt.show()

# Load the dataset
cust_df = pd.read_csv(r"/run/media/panos/SAMSUNG T7/panag/Documents/ΕΡΓΑΣΤΗΡΙΑΚΕΣ ΑΣΚΗΣΕΙΣ/Python tries/Cust_Segmentation.csv")#("F:\\panag\\Documents\\ΕΡΓΑΣΤΗΡΙΑΚΕΣ ΑΣΚΗΣΕΙΣ\\Python tries\\Cust_Segmentation.csv")
print(cust_df.head())

# Extracting only numeric columns for clustering
numeric_columns = cust_df.select_dtypes(include=[np.number]).columns
x = cust_df[numeric_columns].values

# Normalizing over the standard deviation
x = np.nan_to_num(x)
clus_dataSet = StandardScaler().fit_transform(x)

# Modeling
clusterNum = 3
k_means = KMeans(init="k-means++", n_clusters=clusterNum, n_init=12)
k_means.fit(clus_dataSet)
labels = k_means.labels_
print(labels)

# Assign the labels to each row in the dataframe
cust_df["Clus_km"] = labels
print(cust_df.head(5))

# Grouping by clusters and calculating the mean of numeric columns
cluster_means = cust_df.groupby('Clus_km')[numeric_columns].mean()
print(cluster_means)

# Plotting
area = np.pi * (x[:, 1] ** 2)  # Bubble sizes based on some feature, modify as needed
plt.scatter(x[:, 0], x[:, 3], s=area, c=labels.astype(float), alpha=0.5)
plt.xlabel('Age', fontsize=18)
plt.ylabel('Income', fontsize=16)
plt.show()

# 3D plot
fig = plt.figure(1, figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x[:, 1], x[:, 0], x[:, 3], c=labels.astype(float))
ax.set_xlabel('Education')
ax.set_ylabel('Age')
ax.set_zlabel('Income')
plt.show()

#THIS IS THE END