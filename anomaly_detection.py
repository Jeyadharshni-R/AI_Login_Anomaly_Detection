import pandas as pd
from sklearn.ensemble import IsolationForest

data = pd.read_csv("login_data.csv")

features = data[['login_time', 'failed_attempts']]

model = IsolationForest(contamination=0.3, random_state=42)
data['anomaly'] = model.fit_predict(features)

print("Suspicious Login Activities:\n")
print(data[data['anomaly'] == -1])
