# ai_model.py

from sklearn.linear_model import LinearRegression
import numpy as np

class AIModel:
    def __init__(self):
        self.model = LinearRegression()

    def update(self, data):
        """
        Update the AI model with new data.
        """
        # Extract features and target from data
        features = [[float(data['features']['feature1']), float(data['features']['feature2'])]]
        target = float(data['target'])

        # Train the model with the new data
        self.model.fit(features, [target])

    def predict(self, X):
        """
        Make predictions using the AI model.
        """
        return self.model.predict(X)

    def get_coefficients(self):
        """
        Get the coefficients of the linear regression model.
        """
        return self.model.coef_

    def get_intercept(self):
        """
        Get the intercept of the linear regression model.
        """
        return self.model.intercept_
