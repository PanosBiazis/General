# # Import necessary libraries
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LinearRegression
# from sklearn.metrics import mean_squared_error, r2_score

# # Load your dataset (replace with the path to your own file)
# data = pd.read_csv(r"F:\panag\Documents\ΕΡΓΑΣΤΗΡΙΑΚΕΣ ΑΣΚΗΣΕΙΣ\Python tries\FuelConsumptionCo2.csv")

# # 1. Basic EDA
# print("First 5 rows of the dataset:")
# print(data.head())

# # Check for missing values
# print("\nMissing values in each column:")
# print(data.isnull().sum())

# # Descriptive statistics
# print("\nDescriptive statistics:")
# print(data.describe())

# # 2. Visualizations
# # Pairplot to visualize relationships between features
# sns.pairplot(data)
# plt.show()

# # Correlation heatmap
# correlation_matrix = data.corr()
# plt.figure(figsize=(10, 6))
# sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
# plt.title('Correlation Heatmap')
# plt.show()

# # 3. Data Preprocessing
# # Drop rows with missing target values (if applicable)
# data_clean = data.dropna(subset=['target_column_name'])

# # Define features (X) and target (y)
# X = data_clean.drop(columns=['target_column_name'])
# y = data_clean['target_column_name']

# # Split the data into training and testing sets
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# # 4. Apply Linear Regression Model
# model = LinearRegression()
# model.fit(X_train, y_train)

# # Predictions
# y_pred = model.predict(X_test)

# # 5. Model Evaluation
# mse = mean_squared_error(y_test, y_pred)
# r2 = r2_score(y_test, y_pred)

# print("\nModel Evaluation:")
# print(f"Mean Squared Error (MSE): {mse}")
# print(f"R-squared (R2): {r2}")

# # Plot the actual vs predicted values
# plt.scatter(y_test, y_pred)
# plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], color='red', linestyle='--')
# plt.xlabel('Actual Values')
# plt.ylabel('Predicted Values')
# plt.title('Actual vs Predicted Values')
# plt.show()


# Import necessary libraries
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LinearRegression
# from sklearn.metrics import mean_squared_error, r2_score
# from sklearn.preprocessing import LabelEncoder

# # Load your dataset (replace with the path to your own file)
# data = pd.read_csv(r"F:\panag\Documents\ΕΡΓΑΣΤΗΡΙΑΚΕΣ ΑΣΚΗΣΕΙΣ\Python tries\FuelConsumptionCo2.csv")

# # 1. Basic EDA
# print("First 5 rows of the dataset:")
# print(data.head())

# # Check for missing values
# print("\nMissing values in each column:")
# print(data.isnull().sum())

# # Descriptive statistics
# print("\nDescriptive statistics:")
# print(data.describe())

# # 2. Visualizations
# # Pairplot to visualize relationships between features
# sns.pairplot(data)
# plt.show()

# # 3. Encode categorical columns if needed
# encoder = LabelEncoder()
# data_encoded = data.copy()

# # Iterate through the columns and encode non-numeric ones
# for column in data_encoded.select_dtypes(include=[object]).columns:
#     data_encoded[column] = encoder.fit_transform(data_encoded[column])

# # Now calculate the correlation matrix on the encoded data
# correlation_matrix = data_encoded.corr()

# # Correlation heatmap
# plt.figure(figsize=(10, 6))
# sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
# plt.title('Correlation Heatmap')
# plt.show()

# # 4. Data Preprocessing
# target_column = 'CO2EMISSIONS;;;;;;;;;;;;;;;;;;;'
# # Drop rows with missing target values (if applicable)
# data_clean = data.dropna(subset=[target_column])

# # Define features (X) and target (y)
# X = data_clean.drop(columns=[target_column])
# y = data_clean[target_column]

# # Split the data into training and testing sets
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# # 5. Apply Linear Regression Model
# model = LinearRegression()
# model.fit(X_train, y_train)

# # Predictions
# y_pred = model.predict(X_test)

# # 6. Model Evaluation
# mse = mean_squared_error(y_test, y_pred)
# r2 = r2_score(y_test, y_pred)

# print("\nModel Evaluation:")
# print(f"Mean Squared Error (MSE): {mse}")
# print(f"R-squared (R2): {r2}")

# # Plot the actual vs predicted values
# plt.scatter(y_test, y_pred)
# plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], color='red', linestyle='--')
# plt.xlabel('Actual Values')
# plt.ylabel('Predicted Values')
# plt.title('Actual vs Predicted Values')
# plt.show()



# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

# Load your dataset (replace with the path to your own file)
data = pd.read_csv(r"/run/media/panos/SAMSUNG T7/panag/Documents/ΕΡΓΑΣΤΗΡΙΑΚΕΣ ΑΣΚΗΣΕΙΣ/Python tries/FuelConsumptionCo2.csv")

# 1. Basic EDA
print("First 5 rows of the dataset:")
print(data.head())

# Check for missing values
print("\nMissing values in each column:")
print(data.isnull().sum())

# Descriptive statistics
print("\nDescriptive statistics:")
print(data.describe())

# 2. Visualizations
# Pairplot to visualize relationships between features
sns.pairplot(data)
plt.show()

# 3. Encode categorical columns using One-Hot Encoding
data_encoded = data.copy()

# Apply One-Hot Encoding for categorical columns like 'MAKE' and 'MODEL'
data_encoded = pd.get_dummies(data_encoded, drop_first=True)

# Now calculate the correlation matrix on the encoded data
correlation_matrix = data_encoded.corr()

# Correlation heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()

# 4. Data Preprocessing
# Replace 'CO2EMISSIONS;;;;;;;;;;;;;;;;;;;' with the exact name of your target column
target_column = 'CO2EMISSIONS;;;;;;;;;;;;;;;;;;;'

# Drop rows with missing target values
data_clean = data.dropna(subset=[target_column])

# Define features (X) and target (y)
X = data_clean.drop(columns=[target_column])
y = data_clean[target_column]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 5. Apply Linear Regression Model
model = LinearRegression()
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# 6. Model Evaluation
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\nModel Evaluation:")
print(f"Mean Squared Error (MSE): {mse}")
print(f"R-squared (R2): {r2}")

# Plot the actual vs predicted values
plt.scatter(y_test, y_pred)
plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], color='red', linestyle='--')
plt.xlabel('Actual Values')
plt.ylabel('Predicted Values')
plt.title('Actual vs Predicted Values')
plt.show()
