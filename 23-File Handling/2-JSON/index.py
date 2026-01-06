import json

# Writing JSON Files (Saving Python List or Dictionary)
data = {
    "name": "CodeQueen",
    "age": 20,
    "skills": ["Python", "TypeScript", "Web Development"],
    "location": "Karachi"
}
with open("data.json", "w") as file:
    json.dump(data, file, indent=4)  
print("JSON file created successfully")

# Reading JSON Files
with open("data.json", "r") as file:
    content = json.load(file)
    print("---- Reading JSON ----")
    print(content)

# Converting Python Objects to JSON (dumps)
python_dict = {"project": "AI", "duration": "6 months"}
json_str = json.dumps(python_dict, indent=2)
print("---- Python to JSON String ----")
print(json_str)

# Converting JSON to Python Objects (loads)
json_data = '{"name": "Anusha", "age": 21, "skills": ["ML", "Python"]}'
python_obj = json.loads(json_data)
print("---- JSON String to Python Object ----")
print(python_obj)

# Working with Nested JSON Structures
nested_data = {
    "user": {
        "name": "Sumbal",
        "age": 22,
        "education": {
            "degree": "BSCS",
            "university": "ABC University"
        }
    }
}

with open("nested_data.json", "w") as file:
    json.dump(nested_data, file, indent=4)
print("Nested JSON file saved")

# Retrieving Data from JSON Files
with open("nested_data.json", "r", encoding="utf-8") as file:
    data = json.load(file)
    print("---- Retrieving Nested Data ----")
    print("User Name:", data["user"]["name"])
    print("User Degree:", data["user"]["education"]["degree"])
