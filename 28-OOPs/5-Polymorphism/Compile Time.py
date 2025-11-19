# Compile-time / Method Overloading
class Math:
    def add(self, a, b=0):
        return a + b

m = Math()
print(m.add(5))      # 1 argument
print(m.add(5, 10))  # 2 arguments
