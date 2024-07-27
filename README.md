# safeline
Analyzing Chicago Crime Dataset Using an Unsupervised Machine Learning Model

## Intriguing Questions

In the city of Chicago,

* How does temperature affect the incident rate of violent crime (assault or battery)?

* Which month, location generally has the greatest number of crime reported?
  
* How do crime rates and types vary across different seasons and days of the week?

* What categories of crime exhibited the greatest year-over-year increase between 2021 and 2022?

* How do crime patterns differ between residential blocks and commercial/industrial blocks within the same community area?

* Are certain types of crimes more likely to result in arrests than others?

Predictive modeling

* Can a machine learning model accurately predict the safest times and locations for being in residential or commercial areas?

* Can a machine learning model accurately predict the primary type of crime (e.g., theft, assault) based on features like date, location description, community area, and time of day (derived from date)?

* Can temporal patterns (e.g., time of day, day of the week) combined with location descriptions predict hotspots for specific types of crimes (e.g., burglary in residential areas, theft in commercial areas)?

## Data Collection and Preparation

I used the Chicago Crime dataset, a comprehensive dataset (exported from https://data.cityofchicago.org/ in .csv format). This dataset provides detailed information on reported crime incidents across the city. 

To clean the data, I used Pandas to filter out data points (columns) irrelevant to the "Intriguing questions" I want answered and removed the rows that have missing values, ensuring its accuracy and completeness. 

### Before Cleaning
#### Missing Values in Each Column

| Column                | Missing Values |
|-----------------------|----------------|
| ID                    | 0              |
| Date                  | 0              |
| Block                 | 0              |
| Primary Type          | 0              |
| Description           | 0              |
| Location Description  | 153            |
| Arrest                | 0              |
| Domestic              | 0              |
| Community Area        | 12             |
| Year                  | 0              |
| Location              | 326            |


### After Cleaning
#### Missing Values in Each Column

| Column                | Missing Values |
|-----------------------|----------------|
| ID                    | 0              |
| Date                  | 0              |
| Block                 | 0              |
| Primary Type          | 0              |
| Description           | 0              |
| Location Description  | 0              |
| Arrest                | 0              |
| Domestic              | 0              |
| Community Area        | 0              |
| Year                  | 0              |
| Location              | 0              |

### Converting the 'Date' Column to Datetime Format
From 03/18/2015 12:00:00 PM to 2015-03-18 12:00:00

In this step,I converted the 'Date' column in the DataFrame to datetime format. This allows for easier manipulation and analysis of date and time information. The conversion is done using the `pd.to_datetime` function from the pandas library.

```python
# Convert the 'Date' column to datetime format
df_clean['Date'] = pd.to_datetime(df_clean['Date'], format='%m/%d/%Y %I:%M:%S %p')
```


## Exploratory Data Analysis
