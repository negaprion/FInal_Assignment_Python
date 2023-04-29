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

# Find sales by store and sales by store percentage
sales_by_store = data.groupby(['store_number'])['sale_dollars'].sum().reset_index()
total_sales = sales_by_store['sale_dollars'].sum()
sales_by_store['percent_sales'] = sales_by_store['sale_dollars'] / total_sales * 100

# Print result (2)
print(sales_by_store)



# VISUALISATIONS
# Define the colormap to use
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


# Create the horizontal bar plot of sales by store percentage, sorted in descending order
plt.barh(sales_by_store['store_number'], sales_by_store['percent_sales'], color='red')
plt.gca().invert_yaxis()

# Set axis labels, title, ticks, and colors to match black background
plt.xlabel('Percentage of Sales', fontsize=20, color='white')
plt.ylabel('Store Number', fontsize=20, color='white')
plt.title('SALES BY STORE', fontdict={'fontsize': 35, 'color': 'white'}, loc='center', pad=None)
plt.xticks(color='gray')
plt.yticks(color='gray')

# Set the colour of the axes to black
plt.gca().set_facecolor('black')

# Display the plot
plt.show()




"""


# Visualize percentage of sales by store

plt.figure(figsize=(16, 9), facecolor='black')
plt.pie(sales_by_store['percent_sales'], labels=sales_by_store['store_number'], autopct='%1.1f%%')
plt.axis('equal')
plt.title('Sales by Store Percentage', fontdict=({'fontsize':35, 'color':'white'}), loc='center', pad=None)
plt.pie(sales_by_store['percent_sales'], labels=sales_by_store['store_number'], autopct='%1.1f%%', textprops={'color':'white'})

# Sort the data by percent_sales in descending order
sales_by_store.sort_values(by='percent_sales', ascending=False, inplace=True)

# Create a horizontal bar chart
plt.figure(figsize=(16,9), facecolor='white')
plt.barh(sales_by_store['store_number'], sales_by_store['percent_sales'], color='blue')

# Set the labels, title and axis limits
plt.xlabel('Percentage of Sales', fontsize=24, color='white')
plt.ylabel('Store Number', fontsize=24, color='white')
plt.title('Sales by Store Percentage', fontdict=({'fontsize': 35, 'color':'white'}), loc ='center', pad=None)
plt.xlim(0, 25)

# Show the plot
plt.show()


# Define the figure size and facecolor
plt.figure(figsize=(16,9), facecolor='black')

# Sort the sales by store in descending order based on percent_sales
sales_by_store = sales_by_store.sort_values('percent_sales', ascending=False)

# Create the horizontal bar chart with store number on y-axis and percentage of sales on x-axis
plt.barh(sales_by_store['store_number'], sales_by_store['percent_sales'], color='blue')

# Set the x-axis label and color
plt.xlabel('Percentage of Sales', fontsize=24, color='white')

# Set the y-axis label and color
plt.ylabel('Store Number', fontsize=24, color='white')

# Set the chart title and font size and color
plt.title('Percentage of Sales by Store', fontdict={'fontsize':35, 'color':'white'}, loc='center', pad=None)

# Show the plot
plt.show()






plt.show()





# Create the figure object
fig = plt.figure(figsize=(10, 10), facecolor='black')

# Create the scatter plot of most popular item per zip code, with colors based on bottles_sold
plt.scatter(most_popular_per_zip['zip_code'], most_popular_per_zip['bottles_sold'], c=most_popular_per_zip['bottles_sold'], cmap=cmap)

# Set the x and y axis labels and title
plt.xlabel('Zip Code', fontsize=24, color='white')
plt.ylabel('Bottles Sold', fontsize=24, color='white')
plt.title('Most Popular Items Per Zip Code', fontdict={'fontsize': 35, 'color': 'white'}, loc='center', pad=None)

# Set the facecolor of the axes to black
# plt.gca().set_facecolor('black')

# Show the colorbar
plt.colorbar()

# Display the plot
plt.show()


"""