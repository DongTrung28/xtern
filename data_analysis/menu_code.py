import pandas as pd
import matplotlib.pyplot as plt
import os

file_path = "/kaggle/input/xtern-dataset/Menu.csv"
df = pd.read_csv(file_path)

print("Data Overview:")
print(df.info()) 
print("\nSample Data:")
print(df.head())

numerical_columns = ['Price', 'Calories']
categorical_columns = ['Item']

if not os.path.exists('overview_plots'):
    os.makedirs('overview_plots')
    
for col in numerical_columns:
    plt.figure(figsize=(8, 4))
    plt.hist(df[col], bins=20)
    plt.title(f'Distribution of {col}')
    plt.xlabel(col)
    plt.ylabel('Frequency')
    plt.savefig(f'overview_plots/{col}_distribution.png', facecolor='w', bbox_inches="tight", pad_inches=0.3)
    plt.show()
    plt.close()

for col in categorical_columns:
    plt.figure(figsize=(8, 4))
    df[col].value_counts().plot(kind='bar')
    plt.title(f'Distribution of {col}')
    plt.xlabel(col)
    plt.ylabel('Count')
    plt.savefig(f'overview_plots/{col}_distribution.png', facecolor='w', bbox_inches="tight", pad_inches=0.3)
    plt.show()
    plt.close()

