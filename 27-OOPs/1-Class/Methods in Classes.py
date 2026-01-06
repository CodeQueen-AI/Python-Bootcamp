class Patient():
    def __init__(self, first_name , last_name , age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        
    def say_if_minor(self):
        if self.age < 21:
            print(self.first_name + " " + self.last_name + 'is a minor')
        else:
            print(self.first_name + " " + self.last_name + 'is not a minor')
            
pid346 = Patient('Muhammad' , 'Hammad ' , 11)
pid986 = Patient('Mehmood' , 'Khattak' , 25)

pid346.say_if_minor()
pid986.say_if_minor()
