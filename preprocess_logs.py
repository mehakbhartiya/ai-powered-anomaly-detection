import pandas as pd

def preprocess_logs(log_file):
    logs = []
    with open(log_file) as f:
        for line in f:
            log_type = line.split(" ")[0].strip("<>").upper()
            logs.append(log_type)
    return pd.DataFrame(logs, columns=['log_type'])

df = preprocess_logs('logs/app.log')
df['log_type'] = df['log_type'].astype('category').cat.codes  # Encode log types
df.to_csv('logs/preprocessed_logs.csv', index=False)
