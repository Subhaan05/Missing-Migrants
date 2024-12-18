import pandas as pd

# Load dataset into a df
file_path = 'Missing_Migrants_Global_Figures_allData.csv'
data = pd.read_csv(file_path)

# Display information about the dataset
print(data.head())
print(data.describe())
print(data.info())
print(data.columns)
print(data.shape)

# Columns dropping

columns_to_remove = ['Main ID', 'Incident ID', 'UNSD Geographical Grouping', 'URL', 'Source Quality']
data = data.drop(columns=columns_to_remove)

print(data.columns)
print(data.shape)