import csv

# Writing to CSV Files
with open("example.csv", "w", newline='', encoding="utf-8") as file:
    writer = csv.writer(file)  
    # Writing header
    writer.writerow(["Name", "Age", "City"])
    # Writing multiple rows
    writer.writerow(["CodeQueen", 18, "Karachi"])
    writer.writerow(["Anusha", 19, "Lahore"])
print("CSV file written successfully ")

# Reading CSV Files (csv.reader)
with open("example.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    print("---- Reading CSV ----")
    for row in reader:
        print(row)

# Using DictReader
with open("example.csv", "r", encoding="utf-8") as file:
    dict_reader = csv.DictReader(file)
    print("---- Using DictReader ----")
    for row in dict_reader:
        print(row["Name"], row["City"])

# Using DictWriter
with open("example.csv", "a", newline='') as file:
    dict_writer = csv.DictWriter(file, fieldnames=["Name", "Age", "City"])
    # Writing one more row
    dict_writer.writerow({"Name": "Sumbal", "Age": 18, "City": "Karachi"})
print("Row appended using DictWriter")

# Custom Delimiter
with open("example_custom.csv", "w", newline='') as file:
    writer = csv.writer(file, delimiter=';')  
    writer.writerow(["Name", "Age", "City"])
    writer.writerow(["Ali", 25, "Multan"])
print("CSV file with custom delimiter created ")

# Reading Large CSV Efficiently (row by row)
print("---- Reading Large CSV Efficiently ----")
with open("example.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    for row in reader: 
        print(row)