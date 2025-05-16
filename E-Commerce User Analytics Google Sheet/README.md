# E-Commerce User Analytics: From Event Logs to Business Metrics

## Project Overview

This project demonstrates how to transform raw e-commerce event logs into actionable business metrics using advanced spreadsheet analytics. As a junior analyst at an e-commerce company, I was tasked with analyzing user activity data to uncover insights about user behavior, conversion rates, and customer retention. The analysis follows a structured approach, from data cleaning to advanced cohort analysis, and is fully documented for transparency and reproducibility.

## Data Source

The analysis is based on the `raw_user_activity` dataset, where each row represents a user event on the company’s website. The dataset includes:

- **user_id**: Unique customer identifier  
- **event_type**: Type of user activity (e.g., product view, cart open, purchase)  
- **category_code**: Product category  
- **brand**: Product brand  
- **price**: Product price (USD)  
- **event_date**: Date of activity (YYYY-MM-DD)  

## Project Structure

| Sheet Name           | Description                                                                 |
|----------------------|-----------------------------------------------------------------------------|
| Table of Contents    | Organized list of all sheets and their purpose                               |
| Executive Summary    | Key results, conclusions, and analysis notes                                 |
| conversion_funnel    | Pivot table showing user conversion through funnel stages                    |
| retention_rates      | Table and formulas for cohort-based retention rate calculations              |
| cohort_analysis      | Pivot table for cohort analysis by first purchase month and cohort age       |
| purchase_activity    | Filtered purchase events with calculated fields for cohort analysis          |
| first_purchase       | Pivot table with each user’s first purchase date                             |
| raw_user_activity    | Original event log data                                                      |

## Key Analyses

### 1. Conversion Funnel

- **Objective**: Measure how effectively the website converts product page views into purchases.
- **Method**: Built a three-stage funnel (product view → cart open → purchase) using a pivot table, counting unique users at each stage.
- **Metrics**: Calculated both total conversion rates and step-to-step conversion rates using spreadsheet formulas.

### 2. Cohort Analysis Preparation

- **Filtering**: Isolated purchase events into a new sheet (`purchase_activity`).
- **First Purchase Calculation**: Used a pivot table to find each user’s first purchase date, then mapped this back to all purchase events.
- **Monthly Grouping**: Added columns for event month, first purchase month, and cohort age (months since first purchase) using spreadsheet date functions.

### 3. Retention Rate Calculation

- **Cohort Grouping**: Grouped users into cohorts based on the month of their first purchase.
- **Aggregation**: Built a pivot table to count unique users by cohort and cohort age.
- **Retention Rates**: Calculated month-by-month retention rates for each cohort, showing user engagement over time.

## Executive Summary

- **Conversion Funnel**: The funnel analysis revealed the percentage of users progressing from product views to purchases, highlighting key drop-off points and opportunities for optimization.
- **Retention Analysis**: Cohort analysis showed how user retention changes over time, with clear patterns in customer engagement and repeat purchase behavior.
- **Business Insights**: The analysis identified actionable opportunities to improve conversion rates and customer retention, such as targeted marketing for high-value cohorts and optimizing the user journey.

## Methodology & Assumptions

- **Data Used**: Only unique user counts were used for conversion rates; cohort analysis was based on first purchase month.
- **Cohort Formation**: Users were grouped by the month of their first purchase, and retention was tracked for up to four months.
- **Retention Calculation**: Retention rates were calculated as the percentage of original cohort users making purchases in subsequent months.

## Spreadsheet Best Practices

- All sheets are clearly labeled and ordered for logical navigation.
- Key calculations and results are highlighted for readability.
- Dates and numbers are formatted for clarity.
- A legend and table of contents are provided for easy reference.

## How to Use

1. **Explore the Table of Contents** for an overview of the analysis flow.
2. **Review the Executive Summary** for key findings and business recommendations.
3. **Dive into the conversion_funnel and retention_rates sheets** for detailed metrics and calculations.
4. **Refer to the cohort_analysis and purchase_activity sheets** for supporting data and methodology.

---

**This project showcases my ability to turn raw data into business value using advanced spreadsheet analytics, clear documentation, and a focus on actionable insights.**
