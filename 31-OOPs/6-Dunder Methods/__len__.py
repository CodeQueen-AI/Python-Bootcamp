class Book:
    def __init__(self, pages):
        self.pages = pages

    def __len__(self):
        return self.pages

b = Book(150)
print(len(b))   # __len__ call hota hai
