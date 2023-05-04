# Import all necessary packages
import pandas as pd
import matplotlib.pyplot as plt

# Read the previously extracted csv file
data = pd.read_csv('finance_liquor_sales_2016_to_2019.csv')

# Drop unnecessary columns
cols_to_drop = ['invoice_and_item_number',
                'date',
                'address',
                'city',
                'store_location',
                'county_number',
                'county',
                'category',
                'category_name',
                'vendor_number',
                'vendor_name',
                'pack',
                'bottle_volume_ml',
                'state_bottle_cost',
                'state_bottle_retail',
                'volume_sold_liters',
                'volume_sold_gallons',
                'item_number']
data.drop(cols_to_drop, axis=1, inplace=True)


# Group the data by zip code and item description
grouped_data = data.groupby(['zip_code', 'item_description'])

# Aggregate the data to get the total number of bottles sold for each item in each zip code
sales_per_item = grouped_data['bottles_sold'].sum().reset_index()

# Sort the data by zip code and number of bottles sold to get the most popular item in each zip code
most_popular_per_zip = sales_per_item.sort_values(['zip_code', 'bottles_sold'], ascending=[True, False])
most_popular_per_zip = most_popular_per_zip.groupby('zip_code').first().reset_index()

# Print result (1)
print(most_popular_per_zip)


# Find sales per store and sales per store percentage
sales_per_store = data.groupby(['store_number'])['sale_dollars'].sum().reset_index()
total_sales = sales_per_store['sale_dollars'].sum()
sales_per_store['sale_dollars_percentage'] = sales_per_store['sale_dollars'] / total_sales * 100
sales_per_store = sales_per_store.sort_values('sale_dollars_percentage', ascending=False)


# Print result (2)
print(sales_per_store)



# Visualisation 1 - Scatter - Most popular item per zip code
# Define the colormap
cmap = plt.cm.get_cmap('jet')

# Create the figure object
fig = plt.figure(figsize=(16, 10), facecolor='black')

# Create the scatter plot of most popular item per zip code, with colors based on bottles_sold
plt.scatter(most_popular_per_zip['zip_code'], most_popular_per_zip['bottles_sold'], c=most_popular_per_zip['bottles_sold'], cmap=cmap)

# Set axis labels, title, ticks , grid and colors to match black background
plt.xlabel('Zip Code', fontsize=20, color='white')
plt.ylabel('Bottles Sold', fontsize=20, color='white')
plt.title('MOST POPULAR ITEMS PER ZIP CODE', fontdict={'fontsize': 35, 'color': 'white'}, loc='center', pad=None)
plt.xticks(color='gray')
plt.yticks(color='gray')
plt.grid(color='lightgray', alpha=0.1)

# Set the colour of the axes to black
plt.gca().set_facecolor('black')

# Show the colorbar
plt.colorbar()

# Get the indices of the top 8 most popular items (because these are the ones that stand apart in the plot)
top10 = most_popular_per_zip.sort_values('bottles_sold', ascending=False).iloc[:8].index

# Add annotations for the top 10 items
for idx in top10:
    x = most_popular_per_zip.loc[idx, 'zip_code']
    y = most_popular_per_zip.loc[idx, 'bottles_sold']
    text = most_popular_per_zip.loc[idx, 'item_description']
    plt.annotate(text, xy=(x, y), xytext=(x, y + 50), color='gray', fontsize=10, ha='center', va='center')


# Display the plot
plt.show()


# Visualisation 2 - Horizontal Bar - Percent of sales
# Define the colormap
cmap = plt.cm.get_cmap('plasma')

# Create the figure object
fig = plt.figure(figsize=(16, 10), facecolor='black')

# Create the horizontal bar plot of sales per store percentage
plt.barh(range(len(sales_per_store)), sales_per_store['sale_dollars_percentage'],
         color=cmap(sales_per_store['sale_dollars_percentage']/100))

# Set axis labels, title, ticks, and colors to match black background
plt.xlabel('Percentage of Total Sales', fontsize=16, color='white')
plt.ylabel('Store Number', fontsize=16, color='white')
plt.title('SALES % PER STORE', fontdict={'fontsize': 35, 'color': 'white'}, loc='center', pad=None)
plt.xticks(color='gray')
plt.yticks(range(len(sales_per_store)), sales_per_store['store_number'], color='gray', ha='center', va='center')

# Set the colour of the axes to black
plt.gca().set_facecolor('black')

plt.show()






