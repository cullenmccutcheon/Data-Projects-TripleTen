# Zomato Market Analysis Report

**Dashboard:**  
[View Interactive Dashboard](https://public.tableau.com/views/FinalTTFinal/Story10?:language=en-US&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)

## Description & Instructions

This dashboard is designed to help users explore restaurant data interactively, with a focus on cuisine types, ratings, and city-wise distribution. Several filters and custom groupings make the analysis intuitive and flexible.

### Key Features and Filters

- Filters for City, Cuisine Category, and Rating.
- Users can select one or more cities, filter by broad cuisine categories (created using a calculated field), and narrow down results by average restaurant ratings.

### How I Grouped Cuisines

To make the cuisine filter more user-friendly, a calculated field called **Cuisine Category** was created. This field groups the many different cuisine names in the data into broader, more meaningful categories. For example, anything containing "Ice Cream" is grouped under "Desserts." A long list of other cuisines is grouped under "All" to keep the filter manageable. If a cuisine doesn’t match any conditions, it’s labeled as "Other."  
This approach ensures users can easily filter and compare similar types of food, even if the original data had a lot of variety in cuisine names.

### Visualizations

The dashboard includes:
- Bar charts showing the number of restaurants by cuisine category and city.
- Maps displaying restaurant locations.
- Summary metrics (KPIs) for total restaurants, average ratings, and possibly review counts.

All visuals update dynamically based on the filters selected.

### Data Connections

The dashboard is connected to a dataset with fields like **Cuisine**, **City**, **Rating**, and geographic coordinates. The calculated field for cuisine categories is essential for grouping and filtering the data effectively. If new cuisine types are added in the future, the calculated field logic will need to be updated.

### How to Use the Dashboard

1. **Select a City:** Use the city filter to focus on restaurants in a particular location.
2. **Choose a Cuisine Category:** Use the cuisine category filter to analyze specific types of food, as grouped by the calculated field.
3. **Adjust the Rating Filter:** Narrow down the results to restaurants with certain average ratings.
4. **Explore the Visuals:** Interact with the bar charts, maps, and summary metrics to gain insights into restaurant distribution, popularity, and performance.

### Special Notes

- The **Cuisine Category** calculated field is key to making the dashboard easy to use, especially given the variety of cuisine names in the data.
- If you notice any new or uncategorized cuisines, let the author know so the grouping logic can be updated.
- The dashboard is designed to be flexible and interactive, so feel free to experiment with different filter combinations to discover trends.

---

## Executive Summary

This analysis of Zomato’s restaurant and customer sales data uncovers actionable insights to drive growth and engagement across the platform. By focusing on sales performance and customer segmentation, clear opportunities have been identified for both restaurant partners and customer experience teams.

Leading brands like Domino’s Pizza, McDonald’s, Paratha Plaza, Chaat House, and Dosa Express command significant market share. Domino’s Pizza stands out for its consistent sales and order volume, while McDonald’s leads in the beverage segment. Paratha Plaza achieves strong results despite fewer outlets, and Dosa Express demonstrates reliable growth, especially during festival periods. Chaat House, however, experiences more volatile sales, often relying on a small group of top customers.

Customer segmentation analysis reveals that a small group of high-value customers is responsible for a large share of total sales, especially for brands like Domino’s. In contrast, McDonald’s beverage segment has a broad customer base, but most buyers fall into low or medium-value segments, highlighting an opportunity to nurture more high-value customers. Brands with focused menus, such as Domino’s, consistently outperform those with broader offerings, suggesting that menu optimization can drive stronger results.

### Strategic Recommendations

1. Launch targeted marketing and retention programs for high-value, high-frequency customers to maximize their lifetime value.
2. Advise restaurant partners to streamline menus and focus on top-performing items to boost sales efficiency.
3. Encourage brands to use customer segmentation data to identify and nurture potential high-value customers, especially in segments with many low or medium-value buyers.
4. Support partners in developing loyalty programs and personalized offers to increase repeat purchases and move more customers into higher-value segments.
5. Monitor sales and customer trends at the city level to identify local growth opportunities and tailor promotional strategies accordingly.

---

## Project Description

### Business Problem

Zomato aims to enhance business performance by leveraging data-driven insights from sales patterns across restaurant partners and the customer base. The goal is to identify actionable intelligence that can inform growth strategies, improve customer retention, and drive operational improvements across the platform.

### Analysis Focus

This project addresses the following key objectives:
- Track and analyze sales and revenue trends over time
- Identify the highest-performing brands, products, and cities by revenue
- Analyze sales metrics and revenue distribution patterns
- Assess how menu structure and customer spending segments impact overall sales performance
- Segment customers using RFM analysis to inform targeted marketing and loyalty strategies

### Data Description

The analysis utilizes two comprehensive tables from the Zomato data archive:
- **orders:** Detailed customer order information including order IDs, timestamps, product details, and transaction values
- **restaurant:** Restaurant partner information including name, location, and cuisine type
