import pandas as pd

# Load the dataset
df = pd.read_csv('LifeExpectancy.csv')

# Remove leading and trailing spaces from column names
df.columns = df.columns.str.strip()
print(df.info())

# Check for missing values in each column
missing_values = df.isnull().sum()

# Print columns with missing values and the number of missing values
print(missing_values[missing_values > 0])

# Define the threshold for missing values (15%)
threshold = len(df) * 0.15

# Drop columns with more than 15% missing values
df = df.dropna(thresh=len(df) - threshold, axis=1)
print(df.head(10))

# Identify numeric columns in the DataFrame
numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns

# Replace missing values in numeric columns with the median
df[numeric_columns] = df[numeric_columns].apply(lambda x: x.fillna(x.median()))

import matplotlib.pyplot as plt

# Filter data for the years 2000 to 2015
df_filtered = df[(df['Year'] >= 2000) & (df['Year'] <= 2015)]

# Group by 'Year' and calculate the mean life expectancy
average_life_expectancy = df_filtered.groupby('Year')['Life expectancy'].mean()

# Create a bar plot to show the change in life expectancy over the years
plt.figure(figsize=(10, 6))
average_life_expectancy.plot(kind='bar', color='skyblue')
plt.title('Average Life Expectancy Globally (2000 - 2015)')
plt.xlabel('Year')
plt.ylabel('Average Life Expectancy (years)')
plt.show()

# Find the year with the maximum life expectancy
max_life_expectancy_year = average_life_expectancy.idxmax()
print(f"The year with the maximum life expectancy is: {max_life_expectancy_year}")

# Group by 'Year' and 'Status' and calculate the mean life expectancy for each
life_expectancy_by_status = df_filtered.groupby(['Year', 'Status'])['Life expectancy'].mean().unstack()

# Create a bar plot for developed and developing countries
life_expectancy_by_status.plot(kind='bar', figsize=(10, 6), color=['lightblue', 'lightgreen'])
plt.title('Yearly Life Expectancy for Developing and Developed Countries')
plt.xlabel('Year')
plt.ylabel('Life Expectancy (years)')
plt.legend(title='Country Status')
plt.show()
