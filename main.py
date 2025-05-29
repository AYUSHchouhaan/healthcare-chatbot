import pandas as pd

file_path = r"C:\Users\HP\OneDrive\Desktop\uses_alternatives\model3\ANN-ML-MODEL\medicines_50.csv"
df = pd.read_csv(file_path)  
print("CSV file loaded successfully!")
print(df.columns)