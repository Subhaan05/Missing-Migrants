import pandas as pd

# Load dataset into a df
file_path = '/Users/subhaan/Desktop/Code/Missing_Migrants_Global_Figures_allData.csv'
data = pd.read_csv(file_path)

# Display information about the dataset
print(data.head())
print(data.describe())
print(data.info())
print(data.columns)
print(data.shape)

