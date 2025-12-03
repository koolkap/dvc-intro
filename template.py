import pandas as pd
import os

data = {
    'Name': ['John', 'Bob' , 'Ajit'],
    'Age': [25,30,35],
    'City': ['America', 'Brazil', 'Seoul']
}

df = pd.DataFrame(data)

print(df)

data_dir = 'data'

os.makedirs(data_dir,exist_ok=True)

file_path = os.path.join(data_dir, 'sample_data.csv')

df.to_csv(file_path,index=False)

print(f'CSV file is saved to {file_path}')