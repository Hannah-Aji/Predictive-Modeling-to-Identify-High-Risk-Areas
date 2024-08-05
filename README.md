# safeline
Analyzing the Chicago Crime Dataset Using a Machine Learning Model

## Intriguing Questions

In the city of Chicago,

* How does time of day (morning, afternoon, night) affect the incident rate of violent crime (assault or battery)?

* From which locations were the greatest number of crime reported?
  
* How do crime rates and types vary across different seasons and days of the week?

* What categories of crime exhibited the greatest month-over-over increase between 2023 and Now?

* How do crime patterns differ between residential blocks and commercial/industrial blocks

* Are certain types of crimes more likely to result in arrests than others?

#### Predictive modeling

* Can a machine learning model accurately predict the safest times and locations for being in residential or commercial areas?

* Can a machine learning model accurately predict the primary type of crime (e.g., theft, assault) based on features like date, location description, community area, and time of day (derived from date)?

* Can temporal patterns (e.g., time of day, day of the week) combined with location descriptions predict hotspots for specific types of crimes (e.g., burglary in residential areas, theft in commercial areas)?

## Data Collection and Preparation

I used the Chicago Crime dataset, a comprehensive dataset (exported from https://data.cityofchicago.org/ in .csv format). This dataset provides detailed information on reported crime incidents across the city from 2023 to the Present (July 2024). 

To clean the data, I used Pandas to filter out data points (columns) irrelevant to the "Intriguing questions" I want answered and removed the rows that have missing values, ensuring its accuracy and completeness. 

## Goals achieved with Data Cleaning Process

#### Loading the Dataset
The dataset was loaded into a pandas DataFrame from a CSV file. This dataset contains information about various crime incidents in Chicago.

#### Removing Null Rows and Unwanted Columns:
Null Rows: All rows with any missing values were removed using the dropna() method.
Unwanted Columns: The following columns were dropped as they were unnecessary for the analysis:

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

To summarize the conclusions to the above questions, these are visualization that were made to present insights using Matplotlib, Seaborn and Pandas

### How does time of day (morning, afternoon, night) affect the incident rate of violent crime (assault or battery)?

![image](https://github.com/user-attachments/assets/4118bdbf-8a20-412e-aa14-8ff0e979b3ba)

#### The analysis shows that assault and battery crimes in Chicago peak around midnight to 2 AM and again between 3 PM and 4 PM. The lowest occurrence is between 3 AM and 5 AM. These findings suggest focusing law enforcement efforts during these peak hours to enhance community safety.

### From which locations were the greatest number of crime reported?

![image](https://github.com/user-attachments/assets/e02907e6-3849-4df1-8b91-dd990bcbb58e)

#### This analysis shows that crime is primarily reported crimes from Streets, Apartments, Residential homes and Sidewalks. This suggests that these types of locations are more prone to crime incidents.

### Crime Types that show significant month-over-month increase between 2023 and now

![image](https://github.com/user-attachments/assets/1ca6148b-c546-4a07-aa23-936365169107)

![image](https://github.com/user-attachments/assets/491de434-612a-4953-8a53-48681c8f383d)

### Are there more Crime types/patterns common to residential than commercial/industrial blocks?

![image](https://github.com/user-attachments/assets/b3d4c0bf-cff8-406c-9f53-e65816967489)

#### From the analysis,  Battery, Theft, and Assault are common in both Commercial and Residential areas however Deceptive practice crime reports are unique to Commercial areas while Criminal damage is unique to Residential areas. So, there is not primarily distinct crime types reported in both areas.


### Number of Crimes in Residential vs Commercial Areas

![image](https://github.com/user-attachments/assets/95b4b575-55d7-454b-a9bd-fd1e1cde1948)



### Are certain types of crimes more likely to result in arrests than others?
![image](https://github.com/user-attachments/assets/8e1c5447-d71f-452e-8b2f-882daf363d82)

#### The analysis of the data for all reported crime types shows that there were no instances where an arrest did not occur. This means every recorded crime event had an arrest associated with it.

### Predicting the safest locations ( residential or commercial areas) using a Logistic Regression model

![image](https://github.com/user-attachments/assets/feb9aa74-48e4-424a-99dc-8c3aafee9479)

#### Location Description has the highest feature importance value, as determined by the logistic regression model. This indicates that location is the most significant factor in our analysis. Based on previous insights, individuals are generally safer in commercial areas of Chicago compared to residential areas, as crimes are reported more frequently in residential zones than in commercial ones






