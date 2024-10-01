import pandas as pd
from sklearn.ensemble import IsolationForest
import pickle

#load Preprocessed logs 
data = pd.read_csv('logs/preprocessed_logs.csv')


#Train Isolation Forest model
model = IsolationForest(contamination=0.05, random_state=42)
model.fit(data)


#Save the trained model
with open('model/isolation_forest.pkl', 'wb') as f:
    pickle.dump(model, f)


print("Model Trained and Saved")

