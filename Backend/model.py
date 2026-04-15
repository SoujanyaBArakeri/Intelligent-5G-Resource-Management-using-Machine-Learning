import numpy as np
from sklearn.linear_model import LinearRegression

# Dummy Dataset
# distance, users  → required power
X = np.array([
    [10, 5],
    [20, 10],
    [30, 15],
    [40, 20],
    [50, 25]
])

y = np.array([5, 10, 15, 20, 25])

# Train Model
model = LinearRegression()
model.fit(X, y)

# Prediction Function
def predict_power(distance, users):
    power = model.predict([[distance, users]])
    return float(power[0])