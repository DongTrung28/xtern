import pandas as pd
import matplotlib.pyplot as plt

file_path = "/kaggle/input/xtern-dataset/DataSet.xlsx"
df = pd.read_excel(file_path)

print("Data Overview:")
print(df.info()) 
print("\nSample Data:")
print(df.head()) 


categorical_columns = ['Year', 'Major', 'University', 'Time', 'Order']

import os
if not os.path.exists('overview_plots'):
    os.makedirs('overview_plots')

for col in categorical_columns:
    plt.figure(figsize=(16, 8))
    df[col].value_counts().plot(kind='bar')
    plt.title(f'Distribution of {col}')
    plt.xlabel(col)
    plt.ylabel('Count')
    plt.savefig(f'overview_plots/{col}_distribution.png', facecolor='w', bbox_inches="tight", pad_inches=0.3)
    plt.close()


shutil.make_archive("overview_plots", 'zip', ".", "overview_plots")

