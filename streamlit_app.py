import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import streamlit as st
import plotly.express as px

# Load the data from the Excel file
file_path = 'foodhub_nyc_online_order_data.xlsx'  # Replace with the actual file path
df = pd.read_excel(file_path)

# Sidebar filters
st.sidebar.title("Filters")
cuisine_filter = st.sidebar.multiselect('Select Cuisine Types', df['cuisine_type'].unique())
day_filter = st.sidebar.multiselect('Select Days of the Week', df['day_of_the_week'].unique())
order_cost_filter = st.sidebar.selectbox('Select Order Cost Threshold', [20, 30, 40, 50])

if cuisine_filter:
    df = df[df['cuisine_type'].isin(cuisine_filter)]
if day_filter:
    df = df[df['day_of_the_week'].isin(day_filter)]

# Display the first few rows of the dataframe
st.title("FoodHub NYC Online Order Data Analysis")
st.write("Data Preview:", df.head())

# Check for missing values
missing_values = df.isnull().sum()
# st.write("Missing Values:", missing_values)

# Check data types
# st.write("Data Types:", df.dtypes)

# Convert 'cost_of_the_order' and 'rating' columns to numeric types
df['cost_of_the_order'] = pd.to_numeric(df['cost_of_the_order'], errors='coerce')
df['rating'] = pd.to_numeric(df['rating'], errors='coerce')

# Fill missing values if necessary
df['rating'].fillna(0, inplace=True)

# Display summary statistics
st.write("Summary Statistics:", df.describe())

# Preparation time statistics
prep_time_stats = df['food_preparation_time'].agg(['min', 'mean', 'max'])
st.write("Preparation Time Statistics:")
st.write(f"Minimum: {prep_time_stats['min']} minutes")
st.write(f"Average: {prep_time_stats['mean']} minutes")
st.write(f"Maximum: {prep_time_stats['max']} minutes")

# Plot preparation time distribution
fig, ax = plt.subplots()
sns.histplot(df['food_preparation_time'], bins=30, kde=True, ax=ax, color='blue')
ax.set_title('Food Preparation Time Distribution')
st.pyplot(fig)

# Number of unrated orders
unrated_orders = df[df['rating'] == 0].shape[0]
st.write("Number of Unrated Orders:", unrated_orders)

# Data cleanliness check
is_clean = missing_values.sum() == 0
st.write("Is the data clean?", is_clean)

# Popular cuisine types
popular_cuisines = df['cuisine_type'].value_counts()
st.write("Popular Cuisine Types:", popular_cuisines)

# Cuisine price range and ratings
cuisine_stats = df.groupby('cuisine_type').agg({
    'cost_of_the_order': ['mean', 'median', 'min', 'max'],
    'rating': ['mean', 'count']
}).reset_index()
st.write("Cuisine Statistics:", cuisine_stats)

# Plot popular cuisines
fig = px.bar(popular_cuisines, x=popular_cuisines.index, y=popular_cuisines.values, title='Most Popular Cuisine Types', labels={'y':'Number of Orders', 'x':'Cuisine Type'}, color=popular_cuisines.index)
st.plotly_chart(fig)

# Orders on weekdays vs weekends
orders_by_day = df['day_of_the_week'].value_counts()
st.write("Orders by Day of the Week:", orders_by_day)

# Plot orders by day of the week
fig = px.bar(orders_by_day, x=orders_by_day.index, y=orders_by_day.values, title='Orders on Weekdays vs Weekends', labels={'y':'Number of Orders', 'x':'Day of the Week'}, color=orders_by_day.index)
st.plotly_chart(fig)

# Preparation time on weekdays vs weekends
prep_time_by_day = df.groupby('day_of_the_week')['food_preparation_time'].mean()
st.write("Preparation Time by Day of the Week:", prep_time_by_day)

# Plot preparation time by day of the week
fig = px.bar(prep_time_by_day, x=prep_time_by_day.index, y=prep_time_by_day.values, title='Preparation Time on Weekdays vs Weekends', labels={'y':'Average Preparation Time (minutes)', 'x':'Day of the Week'}, color=prep_time_by_day.index)
st.plotly_chart(fig)

# Delivery time on weekdays vs weekends
delivery_time_by_day = df.groupby('day_of_the_week')['delivery_time'].mean()
st.write("Delivery Time by Day of the Week:", delivery_time_by_day)

# Plot delivery time by day of the week
fig = px.bar(delivery_time_by_day, x=delivery_time_by_day.index, y=delivery_time_by_day.values, title='Delivery Time on Weekdays vs Weekends', labels={'y':'Average Delivery Time (minutes)', 'x':'Day of the Week'}, color=delivery_time_by_day.index)
st.plotly_chart(fig)

# Top restaurants
top_restaurants = df['restaurant_name'].value_counts().head(10)
st.write("Top Restaurants:", top_restaurants)

# Plot top restaurants
fig = px.bar(top_restaurants, x=top_restaurants.index, y=top_restaurants.values, title='Top Restaurants with Orders Received', labels={'y':'Number of Orders', 'x':'Restaurant Name'}, color=top_restaurants.index)
st.plotly_chart(fig)

# Popular cuisine type on weekends
weekend_data = df[df['day_of_the_week'].isin(['Saturday', 'Sunday'])]
popular_cuisine_weekends = weekend_data['cuisine_type'].value_counts().head(1)
st.write("Most Popular Cuisine Type on Weekends:", popular_cuisine_weekends)

# Orders cost distribution
order_cost_percentages = (df['cost_of_the_order'] < order_cost_filter).mean() * 100
st.write(f"Percentage of Orders Less Than ${order_cost_filter}: {order_cost_percentages:.2f}%")

# Plot order cost distribution
fig, ax = plt.subplots()
sns.histplot(df['cost_of_the_order'], bins=30, kde=True, ax=ax, color='green')
ax.set_title('Order Cost Distribution')
ax.axvline(order_cost_filter, color='r', linestyle='--')
st.pyplot(fig)

# Average delivery time
avg_delivery_time = df['delivery_time'].mean()
st.write("Average Delivery Time in NYC:", avg_delivery_time)

# Top 3 customers
top_customers = df['customer_id'].value_counts().head(3)
st.write("Top 3 Most Frequent Customers:", top_customers)

# Cost comparison by cuisine type
cuisine_costs = df.groupby('cuisine_type')['cost_of_the_order'].mean()
st.write("Cost Comparison by Cuisine Type:", cuisine_costs)

# Plot cuisine cost comparison
fig = px.bar(cuisine_costs, x=cuisine_costs.index, y=cuisine_costs.values, title='Average Cost by Cuisine Type', labels={'y':'Average Cost ($)', 'x':'Cuisine Type'}, color=cuisine_costs.index)
st.plotly_chart(fig)

# Ratings by cuisine type
cuisine_ratings = df.groupby('cuisine_type')['rating'].mean()
st.write("Ratings by Cuisine Type:", cuisine_ratings)

# Plot cuisine ratings
fig = px.bar(cuisine_ratings, x=cuisine_ratings.index, y=cuisine_ratings.values, title='Average Ratings by Cuisine Type', labels={'y':'Average Rating', 'x':'Cuisine Type'}, color=cuisine_ratings.index)
st.plotly_chart(fig)

# Preparation time by cuisine type
cuisine_prep_times = df.groupby('cuisine_type')['food_preparation_time'].mean()
st.write("Preparation Time by Cuisine Type:", cuisine_prep_times)

# Plot preparation time by cuisine type
fig = px.bar(cuisine_prep_times, x=cuisine_prep_times.index, y=cuisine_prep_times.values, title='Average Preparation Time by Cuisine Type', labels={'y':'Average Preparation Time (minutes)', 'x':'Cuisine Type'}, color=cuisine_prep_times.index)
st.plotly_chart(fig)

# Restaurants for promotional offer
promo_restaurants = df.groupby('restaurant_name').agg({
    'rating': ['mean', 'count']
}).reset_index()
promo_restaurants.columns = ['restaurant_name', 'average_rating', 'rating_count']
eligible_restaurants = promo_restaurants[(promo_restaurants['rating_count'] > 50) & (promo_restaurants['average_rating'] > 4)]
st.write("Restaurants Eligible for Promotional Offer:", eligible_restaurants)

# Calculate net revenue
df['company_revenue'] = np.where(df['cost_of_the_order'] > 20, df['cost_of_the_order'] * 0.25, np.where(df['cost_of_the_order'] > 5, df['cost_of_the_order'] * 0.15, 0))
net_revenue = df['company_revenue'].sum()
st.write("Net Revenue Generated by the Company:", net_revenue)

# Total time required to deliver food
df['total_time'] = df['food_preparation_time'] + df['delivery_time']
orders_over_60_min = (df['total_time'] > 60).mean() * 100
st.write("Percentage of Orders Taking More Than 60 Minutes:", orders_over_60_min)

# Delivery time on weekdays vs weekends
delivery_time_by_day_grouped = df.groupby('day_of_the_week')['delivery_time'].mean()
all_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
delivery_time_by_day_grouped = delivery_time_by_day_grouped.reindex(all_days, fill_value=0)

weekday_delivery_time = delivery_time_by_day_grouped.loc[['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']].mean()
weekend_delivery_time = delivery_time_by_day_grouped.loc[['Saturday', 'Sunday']].mean()
st.write("Average Delivery Time on Weekdays:", weekday_delivery_time)
st.write("Average Delivery Time on Weekends:", weekend_delivery_time)

# Conclusions and recommendations
conclusions = """
From the analysis, we can draw the following conclusions and recommendations:
1. **Most Popular Cuisines**: Some cuisines are more popular and have higher average ratings. Promoting these cuisines can drive more sales.
2. **Weekday vs Weekend Orders**: There are more orders on weekends. Special offers during weekends can attract more customers.
3. **Preparation and Delivery Times**: Preparation times are consistent, but delivery times vary slightly between weekdays and weekends. Improving delivery logistics can enhance customer satisfaction.
4. **Customer Engagement**: Rewarding the top customers can increase loyalty.
5. **Restaurant Performance**: Promoting high-performing restaurants can boost their visibility and attract more orders.
6. **Revenue Generation**: The company generates significant revenue from orders over $20. Encouraging higher spending can increase revenue.
7. **Order Efficiency**: Reducing the percentage of orders taking more than 60 minutes can improve overall customer satisfaction.
"""

st.write(conclusions)
