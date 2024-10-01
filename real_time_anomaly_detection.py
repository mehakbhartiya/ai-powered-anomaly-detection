import pandas as pd
import pickle
from loguru import logger

# Load the trained Isolation Forest model
with open('model/isolation_forest.pkl', 'rb') as file:
    model = pickle.load(file)

# Set up loguru logger to write to the anomaly detection log file
logger.add("logs/anomaly_detection.log")

def detect_anomalies():
    # Load the preprocessed logs
    data = pd.read_csv('logs/preprocessed_logs.csv')

    # Predict anomalies
    predictions = model.predict(data)

    # Separate normal and anomalous entries
    anomalies = data[predictions == -1]
    normal = data[predictions == 1]

    # Log the detection results
    logger.info(f"Total entries: {len(data)}")
    logger.info(f"Normal entries: {len(normal)}")
    
    if not anomalies.empty:
        logger.warning(f"Anomalous entries detected: {len(anomalies)}")
        logger.error(f"Anomalies details:\n{anomalies}")
    else:
        logger.info("No anomalies detected.")

# Call the detect_anomalies function
detect_anomalies()
