import pandas as pd
import json

# Read Excel file into a DataFrame
df = pd.read_excel('answers.xlsx', header=None)  # Assuming there is no header

# Create a dictionary to store the JSON data
json_data = {}

# Iterate through each row
for i, row in df.iterrows():
    # Convert the row to a list and store it in the dictionary
    json_data[str(i + 1)] = row.tolist()

# Save the dictionary as a JSON file
with open('output.json', 'w', encoding='utf-8') as json_file:
    json.dump(json_data, json_file, ensure_ascii=False, indent=4)

print("JSON file created successfully.")
