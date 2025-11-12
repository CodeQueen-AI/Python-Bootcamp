students = {
    "student1": {
        "name": "Ali",
        "age": 20,
        "course": "Python"
    },
    "student2": {
        "name": "Sara",
        "age": 22,
        "course": "Java"
    }
}

# Accessing elements
print(students["student1"]["name"])   
print(students["student2"]["course"]) 

# Modifying nested dictionary
students["student1"]["age"] = 21
print(students["student1"]["age"])   

# Iterating through nested dictionary
for student, info in students.items():
    print(student, "->")
    for key, value in info.items():
        print("   ", key, ":", value)
