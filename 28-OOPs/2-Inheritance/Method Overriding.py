class A:
    def show(self):
        print("Parent Show")

class B(A):
    def show(self):
        print("Child Show")

B().show()
