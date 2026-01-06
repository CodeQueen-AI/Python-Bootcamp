class A:
    def showA(self):
        print("A")

class B(A):
    def showB(self):
        print("B")

class C(A):
    def showC(self):
        print("C")

class D(B, C):
    pass

d = D()
d.showA()
d.showB()
d.showC()
