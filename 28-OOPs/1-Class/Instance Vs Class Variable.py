# Instance Variable
class Patient:
    def __init__(self, name, age):
        self.name = name 
        self.age = age    

p1 = Patient("Ayesha", 25)
p2 = Patient("Maria", 30)

print(p1.name, p1.age)  
print(p2.name, p2.age)  


# Class Variable
class Patient():
    hospital_name = 'City Hospital'
    
    def __init__(self , name):
        self.name = name
        
p1 = Patient('Ayesha')
p2 = Patient('Maria')

print('Name : ' + p1.name , '& Hospital Name : ' + p1.hospital_name)
print('Name : ' + p2.name , '& Hospital Name : ' + p2.hospital_name)
