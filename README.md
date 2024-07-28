# safeline
Analyzing Chicago Crime Dataset Using an Unsupervised Machine Learning Model

## Intriguing Questions

In the city of Chicago,

* How does time of day (morning, afternoon, night) affect the incident rate of violent crime (assault or battery)?

* From which locations were the greatest number of crime reported?
  
* How do crime rates and types vary across different seasons and days of the week?

* What categories of crime exhibited the greatest month-over-over increase between 2023 and Now?

* How do crime patterns differ between residential blocks and commercial/industrial blocks

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

In this step,I converted the 'Date' column in the DataFrame to datetime format. This allows for easier manipulation and analysis of date and time information. The conversion is done using the `pd.to_datetime` function from the pandas library.

## Goals achieved with Data Cleaning Process

#### Loading the Dataset
The dataset was loaded into a pandas DataFrame from a CSV file. This dataset contains information about various crime incidents in Chicago.

#### Removing Null Rows and Unwanted Columns:
Null Rows: All rows with any missing values were removed using the dropna() method.
Unwanted Columns: The following columns were dropped as they were deemed unnecessary for the analysis:
            CASE#
            IUCR
            BEAT
            WARD
            FBI CD
            X COORDINATE
            Y COORDINATE
            LATITUDE
            LONGITUDE
            LOCATION

Renaming Columns:
The columns were renamed for consistency and ease of use. The columns with leading and trailing spaces in their names were corrected. The new column names are:
            DATE OF OCCURRENCE
            BLOCK
            PRIMARY DESCRIPTION
            SECONDARY DESCRIPTION
            LOCATION DESCRIPTION
            ARREST
            DOMESTIC
            

#### Converting Date Column to Datetime Format:
The DATE OF OCCURRENCE column was converted to a datetime format using pd.to_datetime(). This ensures that the date information can be used effectively for time-based analysis.

#### Resulting DataFrame Information
The final columns in the DataFrame are:

    DATE OF OCCURRENCE
    BLOCK
    PRIMARY DESCRIPTION
    SECONDARY DESCRIPTION
    LOCATION DESCRIPTION
    ARREST
    DOMESTIC
    

This cleaned dataset is now ready for further analysis, including time-based trends, location-based patterns, and predictive modeling.


## Exploratory Data Analysis
