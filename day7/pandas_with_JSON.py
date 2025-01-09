import pandas as pd 

FILE_PATH = "day7/my_csv.csv"
df = pd.read_json(FILE_PATH)
print(df)

