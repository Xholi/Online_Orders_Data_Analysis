# FoodHub NYC Order Data Analysis Dashboard

## Overview
This Streamlit application provides comprehensive analysis and visualization of FoodHub NYC's online food ordering data. The dashboard offers interactive filters and multiple visualizations to help understand ordering patterns, customer behavior, cuisine preferences, and operational metrics.

## Features
- Interactive filters for cuisine types and days of the week
- Customizable order cost threshold analysis
- Comprehensive data visualizations including:
  - Food preparation time distribution
  - Popular cuisine types
  - Order patterns across weekdays and weekends
  - Restaurant performance metrics
  - Cost and rating analysis by cuisine type
  - Delivery time analysis
  - Revenue insights

## Prerequisites
- Python 3.7+
- pip (Python package installer)

## Required Libraries
```
pandas
matplotlib
seaborn
numpy
streamlit
plotly.express
```

## Installation
1. Clone this repository or download the source code
2. Install the required packages:
```bash
pip install -r requirements.txt
```

## Data Requirements
- The application expects an Excel file named 'foodhub_nyc_online_order_data.xlsx'
- Required columns:
  - cuisine_type
  - day_of_the_week
  - cost_of_the_order
  - rating
  - food_preparation_time
  - delivery_time
  - restaurant_name
  - customer_id

## Usage
1. Place your data file in the same directory as the script
2. Run the Streamlit application:
```bash
streamlit run app.py
```
3. Access the dashboard through your web browser (typically http://localhost:8501)

## Dashboard Sections
1. **Data Overview**
   - Data preview
   - Summary statistics
   - Data quality checks

2. **Time Analysis**
   - Preparation time distribution
   - Delivery time patterns
   - Weekday vs weekend comparisons

3. **Cuisine Analysis**
   - Popular cuisine types
   - Price ranges by cuisine
   - Rating distribution

4. **Restaurant Performance**
   - Top performing restaurants
   - Promotional eligibility analysis
   - Order volume distribution

5. **Revenue Analysis**
   - Net revenue calculations
   - Order cost distribution
   - Customer spending patterns

## Filter Options
- Cuisine Type: Multi-select filter for specific cuisine types
- Days of Week: Multi-select filter for specific days
- Order Cost Threshold: Adjustable threshold for cost analysis

## Business Insights
The dashboard automatically generates conclusions and recommendations based on:
- Popular cuisine patterns
- Weekly ordering trends
- Delivery performance
- Customer engagement metrics
- Revenue generation opportunities
- Operational efficiency

## Notes
- The application includes automatic handling of missing values
- Revenue calculations use a tiered commission structure
- Performance metrics consider both volume and quality indicators

## Contributing
Feel free to submit issues, fork the repository, and create pull requests for any improvements.

## License
[Specify your license here]
