import pandas as pd

# Define the path to the dataset
# file_path = r'C:\Users\quavi\safeline\datasets\Crimes.csv'

# Define the number of rows to read
nrows_to_read = 50000

# Read the first 500,000 rows of the dataset
df = pd.read_csv(file_path, nrows=nrows_to_read)

# Check for missing values
missing_values = df.isnull().sum()
print("Missing values in each column:")
print(missing_values)

# Handle missing values (e.g., drop rows with missing values)
df = df.dropna()

# Convert the 'Date' column to datetime format
df['Date'] = pd.to_datetime(df['Date'], format='%m/%d/%Y %I:%M:%S %p')

# Extract year, month, day, hour, and day of the week
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
df['Day'] = df['Date'].dt.day
df['Hour'] = df['Date'].dt.hour
df['DayOfWeek'] = df['Date'].dt.dayofweek

# Encode categorical variables
df = pd.get_dummies(df, columns=['Primary Type', 'Description', 'Location Description', 'Community Area'])

# Verify the dataframe after preprocessing
print(df.head())
print(df.info())

# Save the cleaned data to a new CSV file
# df.to_csv(r'C:\Users\quavi\safeline\datasets\Crimes_cleaned.csv', index=False)
