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

columns_to_remove = ['Main ID', 'Incident ID', 'UNSD Geographical Grouping', 'URL', 'Source Quality', 'Information Source']
data = data.drop(columns=columns_to_remove)

# Columns renaming to suit visualisations

columns_new_names = {
    'Region of Incident': 'Incident Region',
    'Date of Incident': 'Incident Date',
    'Year of Incident': 'Incident Year',
    'Number of Dead': 'Death Toll',
    'Minimum Estimated Number of Missing': 'Estimated Missing Count',
    'Total Number of Dead and Missing': 'Total Missing and Dead',
    'Number of Survivors': 'Survivors Count',
    'Number of Females': 'Females Count',
    'Number of Males': 'Males Count',
    'Number of Children': 'Children Count',
    'Country of Origin': 'Origin Country',
    'Region of Origin': 'Origin Region',
    'Country of Incident': 'Incident Country',
    'Location of Death': 'Incident Location',
}

# Applying column renaming
data.rename(columns=columns_new_names, inplace=True)
print(data.info())

# Altering null data to 0 for death count

print(data.isna().sum())

data['Death Toll'].fillna(0, inplace=True)

print(data.info())
