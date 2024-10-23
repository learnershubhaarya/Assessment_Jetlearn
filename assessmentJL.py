import pandas as pd

# Load the dataset
df = pd.read_csv('vgsales.csv')

# Fill missing 'Year' with the median year and convert to integer
df['Year'] = df['Year'].fillna(df['Year'].median()).astype(int)

# Fill missing 'Publisher' with 'Unknown'
df['Publisher'] = df['Publisher'].fillna('Unknown')

# Group by 'Publisher' and sum 'NA_Sales'
top_publishers_na = df.groupby('Publisher')['NA_Sales'].sum().sort_values(ascending=False).head(10)

print(top_publishers_na)

import matplotlib.pyplot as plt

# Group by 'Year' and 'Publisher' and sum sales for different regions
publisher_sales = df.groupby(['Year', 'Publisher'])[['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales']].sum().reset_index()

# Select the top 5 publishers based on global sales for plotting
top_publishers = df.groupby('Publisher')['Global_Sales'].sum().sort_values(ascending=False).head(5).index

# Filter the data to only include top publishers
filtered_sales = publisher_sales[publisher_sales['Publisher'].isin(top_publishers)]

# Create line plots for each region and global sales
regions = ['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales']
for region in regions:
    plt.figure(figsize=(10, 6))
    for publisher in top_publishers:
        subset = filtered_sales[filtered_sales['Publisher'] == publisher]
        plt.plot(subset['Year'], subset[region], label=publisher)
    
    plt.title(f'{region} Over Time for Top Publishers')
    plt.xlabel('Year')
    plt.ylabel(f'Sales in {region}')
    plt.legend()
    plt.show()
# Group by 'Publisher' and sum 'Global_Sales'
global_sales_by_publisher = df.groupby('Publisher')['Global_Sales'].sum()

# Find the publisher with the maximum global sales
top_global_publisher = global_sales_by_publisher.idxmax()
top_global_sales = global_sales_by_publisher.max()

print(f"The publisher that sells the most units globally is {top_global_publisher} with {top_global_sales} million units sold.")
