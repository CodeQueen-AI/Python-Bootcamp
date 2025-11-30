class Patient():
    def __init__(self, last_name):
        self.last_name = last_name
    
p1 = Patient('Ifra')
pid123 = Patient('Fatima')
pid987 = Patient('Anusha')
print(p1.last_name)
print(pid123.last_name)
print(pid987.last_name)

# Add more Attributes
class Patient():
    def __init__(self, first_name , last_name , age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        
pid12 = Patient('Sumbal' , 'Naz' , 18)
pid34 = Patient('Anusha' , 'Akhter' , 20)
pid56 = Patient('Ifra' , 'Akhter' , 17)
pid78 = Patient('Sumbul' , 'Jawed' , 22)

print(pid12.first_name , pid12.last_name , pid12.age)
print(pid34.first_name , pid34.last_name , pid34.age)
print(pid56.first_name , pid56.last_name , pid56.age)
print(pid78.first_name , pid78.last_name , pid78.age)

# Accessing Attributes of Class Instances
class Patient():
    def __init__(self, last_name, first_name, age):
        self.last_name = last_name
        self.first_name = first_name
        self.age = age
        
pid1234 = Patient('Taleb' , 'Sue' , 20)
age_of_patient = pid1234.age
print('Age of Patient : ' , age_of_patient)

print('Patient Name : ' , pid1234.first_name, pid1234.last_name)
