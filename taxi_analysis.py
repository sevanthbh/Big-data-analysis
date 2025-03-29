import dask.dataframe as dd

# Load CSV file
df = dd.read_csv("your_taxi_data.csv")  # Change to your actual file name

# Display dataset information
print(df.info())  
print(df.head())  # Show first few rows
