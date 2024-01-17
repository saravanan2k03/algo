import pandas as pd

# Load the CSV file into a DataFrame
csv_file = "BigML_Dataset.csv"
df = pd.read_csv(csv_file)

# Assuming the date column in the CSV is named 'Date' (with a capital 'D')
# Convert the date format from 'dd-mm-yyyy' to 'dd-mm-yyyy'
print(df['Date'])
    
df['Date'] = pd.to_datetime(df['Date'], format=r'%d-%m-%Y').dt.strftime(r'%Y-%m-%d')

# Save the DataFrame back to a new CSV file
output_csv_file = "output_file.csv"
df.to_csv(output_csv_file, index=False)
