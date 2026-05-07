'Section 1: Basic File Operations'

# 1. Open the CSV file using open() in read mode and print its contents.

# with open('sample_data_50.csv','r')as f:
#     print(f.read())





# 2. Count the total number of lines in the file.

# count = 0
# with open('sample_data_50.csv','r')as f:
#     for line in f:
#         count += 1
# print('total lines :',count)


#3. Read only the first 5 rows from the file.


#4. Read the file line by line using readline().

# with open('sample_data_50.csv','r')as f:
#     line = f.readline()
#     while line:
#         print(line.strip())
#         line = f.readline()

#5. Read all lines using readlines() and display them.
#6. Print only the header row of the CSV file.

# with open('sample_data_50.csv','r')as f:
#     print(f.readline())

#7. Check whether the file exists before opening it.
#8. Close the file manually after reading.

# with open('sample_data_50.csv','r')as f:
#     print(f.read())
#     f.close()

#9. Use with statement to open and read the file.
# with open('sample_data_50.csv','r')as f:
#     data = f.read()
#     print(data)

#10. Print file size in bytes.

'🔹 Section 2: Working with CSV Data'

# Read the CSV file using the csv module.
# Print all rows as lists.
# Print all rows as dictionaries using DictReader.
# Extract and print all names from the file.
# Extract and print all cities.
# Count how many records are there in total.
# Print records where Age > 30.
# Print records where City = "Kochi".
# Count how many people belong to each city.
# Find the maximum age in the dataset.


'🔹 Section 3: Writing to CSV'

# Create a new CSV file and write 5 records manually.
# Copy contents from original file to a new file.
# Append a new record to the existing CSV file.
# Write only names and ages to a new file.
# Save filtered data (Age > 25) into a new CSV.
# Write a CSV file with custom delimiter (e.g., ;).
# Write a file with uppercase names.
# Remove duplicate rows (if any) and write to new file.
# Write sorted data based on Age.
# Write data in reverse order.

'🔹 Section 4: Data Processing'

# Calculate average age of all records.
# Find youngest person in the dataset.
# Find oldest person in the dataset.
# Count how many people are from each city.
# Display names of people whose age is between 25–30.
# Replace all city names "Delhi" with "New Delhi".
# Convert all names to lowercase.
# Add a new column "Status" (Adult/Young based on age).
# Create a new CSV with only unique cities.
# Merge two CSV files (create another sample file).

'🔹 Section 5: Intermediate Tasks'

# Search for a record by name.
# Update age of a specific person and rewrite file.
# Delete a record based on ID.
# Sort data by Name alphabetically.
# Group data by City and display counts.
# Find top 5 oldest people.
# Find average age per city.
# Validate data (check for missing values).
# Handle exceptions while opening file.
# Build a menu-driven program:
# View records
# Add record
# Delete record
# Search record