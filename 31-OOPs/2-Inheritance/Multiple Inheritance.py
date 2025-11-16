class Mother:
    def feature1(self):
        print("Mother Feature")

class Father:
    def feature2(self):
        print("Father Feature")

class Child(Mother, Father):
    pass

c = Child()
c.feature1()
c.feature2()
