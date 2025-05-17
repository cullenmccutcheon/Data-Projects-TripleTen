# Manhattan Airbnb Property Analysis

[LINK TO PROJECT](https://docs.google.com/spreadsheets/d/1HhwsPi5hr1pvMp4p94ci_fIJ3q6zTYCcYrR50fxo6oY/edit?usp=sharing)
---
[PDF](https://github.com/cullenmccutcheon/Data-Projects-TripleTen/blob/main/Manhattan%20Airbnb%20Property%20Analysis/Manhattan%20Airbnb%20Property%20Analysis.pdf)
---

## Executive Summary

This analysis provides actionable insights for investors in the Manhattan Airbnb market. By focusing on the most attractive neighborhoods and property sizes, and by quantifying revenue potential, this project offers a data-driven roadmap for maximizing returns in the vacation rental sector.

---

## Project Overview

You've been hired to help a client analyze the Manhattan vacation rental market and provide guidance on which property types to invest in. This project leverages NYC Airbnb data to answer key business questions about neighborhood and property size attractiveness, as well as revenue potential for vacation rentals.

---

## 🔗 [NYC Airbnb Data](https://docs.google.com/spreadsheets/d/1qdnGCyf_eMhtXXvbPIc8wnz3WIlllL2GnlYvVBlufx8/copy)


---

## Table of Contents

- [Project Overview](#project-overview)
- [Business Questions](#business-questions)
- [Analysis Approach](#analysis-approach)
- [Key Findings](#key-findings)
- [Visualizations](#visualizations)
- [Data Cleaning & Documentation](#data-cleaning--documentation)
- [Executive Summary](#executive-summary)
- [Assumptions](#assumptions)
- [Contact](#contact)

---

## Business Questions

1. **Which neighborhoods and property sizes (number of bedrooms) are most attractive for vacation rentals?**
2. **How much money did these listings generate?**

---

## Analysis Approach

**Data Cleaning:**  
- Cleaned neighborhood column for consistent capitalization and removed trailing spaces (`neighborhood_clean`).
- Cleaned bedrooms column, treating empty cells as studios (`bedrooms_clean`).
- Documented all cleaning steps in a separate change log sheet and preserved a copy of the raw data.

**Attractiveness Metric:**  
- Used `number_of_reviews_ltm` (reviews in the last 12 months) as a proxy for rental frequency and attractiveness.

**Pivot Table Analysis:**  
- Identified the top 10 most attractive neighborhoods by total reviews.
- Determined the most popular property sizes (studios, 1-bedrooms, 2-bedrooms).
- Analyzed neighborhood-specific preferences for property size.

**Revenue Analysis:**  
- Filtered for top listings (most popular size in each top neighborhood).
- Calculated revenue using the `calendar` sheet:  
  - Added `revenue_earned` column (only if property was rented).
  - Summed 30-day revenue and estimated annual revenue by multiplying by 12.
- Ranked top listings by revenue.

---

## Key Findings

**Top 3 Most Attractive Neighborhoods:**  
- Lower East Side  
- Hell's Kitchen  
- Harlem

**Top 3 Most Popular Property Sizes:**  
- Studios  
- 1-bedrooms  
- 2-bedrooms

**Neighborhood Preferences:**  
- Example: 1-bedroom is the most popular in Harlem.

**Top-Earning Listing:**  
- Listing ID: `49946551`  
- 30-day Revenue: **$29,940**  
- Estimated Annual Revenue: **$359,280**

---

## Visualizations

- Bar chart of number of reviews for the top 10 neighborhoods.
- Pivot tables showing property size popularity and revenue by neighborhood.

---

## Data Cleaning & Documentation

- All data cleaning steps are documented in a dedicated change log sheet.
- Raw data is preserved in a separate sheet.
- Unnecessary columns are hidden for clarity.
- Formatting, borders, cell background colors, and font styles are consistent throughout the analysis.
- All assumptions are clearly documented.

---

## Assumptions

- Reviews are a reliable proxy for rental frequency.
- Empty bedroom cells represent studio apartments.
- Revenue is estimated by multiplying 30-day earnings by 12 for annual projection.

---

*This project demonstrates advanced skills in data cleaning, pivot table analysis, and business intelligence storytelling using real-world Airbnb data.*
