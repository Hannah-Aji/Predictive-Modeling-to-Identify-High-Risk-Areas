# safeline
Analyzing Chicago Crime Dataset Using an Unsupervised Machine Learning Model

## Intriguing Questions

In the city of Chicago,

* How do crime rates and types vary across different seasons and days of the week?

* How do crime patterns differ between residential blocks and commercial/industrial blocks within the same community area?

* Are certain types of crimes more likely to result in arrests than others?

* What are the most common locations where domestic-related crimes occur?

Predictive modeling

* Can a machine learning model accurately predict the safest times and locations for being in residential or commercial areas?

* Can a machine learning model accurately predict the primary type of crime (e.g., theft, assault) based on features like date, location description, community area, and time of day (derived from date)?

* Can temporal patterns (e.g., time of day, day of the week) combined with location descriptions predict hotspots for specific types of crimes (e.g., burglary in residential areas, theft in commercial areas)?

## Data Collection and Preparation

I used the Chicago Crime dataset, a comprehensive dataset (exported from https://data.cityofchicago.org/ in .csv format). This dataset provides detailed information on reported crime incidents across the city. 

To clean the data, I used Pandas to filter out data points (columns) irrelevant to the "Intriguing questions" I want answered and ensured that there no missing values. 


## Exploratory Data Analysis
