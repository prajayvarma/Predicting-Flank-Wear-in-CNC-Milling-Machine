import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import numpy as np
import matplotlib.pyplot as plt

# Load the training dataset and select only 'VIB' and 'DC' as features
data = pd.read_excel('Train.xlsx')
X = data[['vib_mean','Dc_mean','time','vib_median','DOC']]
y = data['VB']            # Target variable

# Train the Linear Regression model
lr_model = LinearRegression()
lr_model.fit(X, y)
lr_predictions = lr_model.predict(X)
lr_rmse = np.sqrt(mean_squared_error(y, lr_predictions))
print(f"Linear Regression RMSE (train): {lr_rmse}")

# Load the test dataset and select only 'VIB' and 'DC' as features
df_1 = pd.read_excel('Test.xlsx')
X_1 = df_1[['vib_mean','Dc_mean','time','vib_median','DOC']]
y_1 = df_1['VB']           # Target variable in test data

# Predict and evaluate on the test data
prediction_1 = lr_model.predict(X_1)
lr_rmse_1 = np.sqrt(mean_squared_error(y_1, prediction_1))
print(f"Linear Regression RMSE (test): {lr_rmse_1}")
print(lr_model.score(X_1,y_1))

plt.figure(figsize=(10, 6))
plt.scatter(y_1, prediction_1, color='blue', alpha=0.6, label='Predicted vs Actual')
plt.plot([y_1.min(), y_1.max()], [y_1.min(), y_1.max()], color='red', linestyle='--', label='Ideal Fit')
plt.xlabel('Actual VB')
plt.ylabel('Predicted VB')
plt.title('Predicted vs Actual Values (Test Data)')
plt.legend()
plt.grid(alpha=0.3)
plt.show()
