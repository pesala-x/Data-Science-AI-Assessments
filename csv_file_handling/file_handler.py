import csv

FILE_PATH = "csv_file_handling/my_csv.csv"

data = [
    {"Name": "Jhon Doe", "Age": 30, "City": "New York"},
    {"Name": "Jane Smith", "Age": 25, "City": "Los Angeles"},
    {"Name": "Bob Johnson", "Age": 35, "City": "Chicago"}
]

field_names = ["Name", "Age", "City"]

# Write data to the CSV file
with open(FILE_PATH, mode='w', newline='') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=field_names)
    writer.writeheader()  # Write the header row
    writer.writerows(data)  # Write the data rows

print(f"Data written successfully to {FILE_PATH}")
