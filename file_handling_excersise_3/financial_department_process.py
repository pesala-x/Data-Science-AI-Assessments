import csv

INPUT_FILE = "file_handling_excersise_3/employees.csv"
OUTPUT_FILE = "file_handling_excersise_3/high_salary_employees.csv"

field_name = {'Employe_id','Name','Departmrnt','Slary'}

data=[
        {'Employe_id': 1, 'Name': 'john', 'Departmrnt': 'It','Slary':60000},
        {'Employe_id': 2, 'Name': 'john', 'Departmrnt': 'HR','Slary':55000},
        {'Employe_id': 3, 'Name': 'john', 'Departmrnt': 'Finance','Slary':30000},
        {'Employe_id': 4, 'Name': 'john', 'Departmrnt': 'It','Slary':65000},


    
]
with open(INPUT_FILE,'w',newline='')as csv_file:
    content = csv.DictWriter(csv_file,fieldnames=field_name)
    content.writeheader()

    for row in data:
        content.writerow(row)

filtered_data = []

with open(INPUT_FILE,'r',newline='')as csv_file:

    csv_reader = csv.DictReader(csv_file)

    for row in csv_reader:

        salary =  int(row['Slary'])
        if salary > 60000:
            filtered_data.append(row)

with open(OUTPUT_FILE,'w',newline='')as csv_file:
    content = csv.DictWriter(csv_file,fieldnames=field_name)
    content.writeheader()

    for row in filtered_data:
        content.writerow(row)

# File paths

# INPUT_FILE = "file_handling_excersise_3/employees.csv"
# OUTPUT_FILE = "file_handling_excersise_3/high_salary_employees.csv"

# # Step 1: Read the input file and display all records
# print("All Employee Records:")
# with open(INPUT_FILE, mode="r") as file:
#     csv_reader = csv.reader(file)
#     for row in csv_reader:
#         print(row)

# # Step 2: Filter the records with Salary > 60000
# filtered_records = []
# with open(INPUT_FILE, "r") as file:
#     csv_reader = csv.DictReader(file)
#     for row in csv_reader:
#         # Normalize keys to match fieldnames
#         normalized_row = {key.strip().title(): value for key, value in row.items()}
#         # Convert Salary to integer and filter employees with Salary > 60000
#         if int(normalized_row["Salary"]) > 60000:
#             filtered_records.append(normalized_row)

# # Display filtered records
# print("\nFiltered Records (Salary > 60000):")
# for record in filtered_records:
#     print(record)

# # Step 3: Write the filtered records to a new CSV file
# with open(OUTPUT_FILE, "w", newline="") as file:
#     fieldnames = ["EmployeeId", "Name", "Department", "Salary"]
#     csv_writer = csv.DictWriter(file, fieldnames=fieldnames)

#     csv_writer.writeheader()  # Write header row
#     csv_writer.writerows(filtered_records)  # Write filtered data

# print(f"\nFiltered records written successfully to {OUTPUT_FILE}")