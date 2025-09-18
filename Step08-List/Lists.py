#List
fruits = ["Apple", "Banana", "Mango"]
print(fruits)

#Methods
#Append()
fruits = ["apple", "banana"]
fruits.append("grapes")  
print(fruits)  

#Insert()
fruits = ["apple", "banana"]
fruits.insert(1, "watermelon")  
print(fruits)  

#Remove()
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")  
print(fruits)  

#Pop()
fruits = ["apple", "banana", "cherry"]
fruits.pop()  
print(fruits)  

fruits.pop(0)    
print(fruits)  

#Sort()
numbers = [3, 1, 4, 2]
numbers.sort()  
print(numbers)  

#Reverse()
numbers = [1, 2, 3, 4]
numbers.reverse()  
print(numbers)  

#Index()
fruits = ["apple", "banana", "cherry"]
print(fruits.index("banana"))  

#Count()
numbers = [1, 2, 3, 2, 2, 4]
print(numbers.count(2))  

#Extend()
fruits = ["apple", "banana"]
more_fruits = ["watermelon", "grapes"]
fruits.extend(more_fruits)  
print(fruits)  

#Clear()
fruits = ["apple", "banana"]
fruits.clear()  
print(fruits)  

#Copy()
fruits = ["apple", "banana", "grapes"]
new_fruits = fruits.copy()

# New list ko modify karna
new_fruits.append("watermelon")

print("Original List:", fruits)  
print("Copied List:", new_fruits)  

#sort(reverse=True)
numbers = [5, 2, 8, 1, 4]
numbers.sort(reverse=True) 
print(numbers)  

#del()
fruits = ["apple", "banana", "cherry"]
del fruits[1] 
print(fruits)  

numbers = [1, 2, 3, 4]
del numbers 

# Nested List
nested = [[1, 2, 3], ["apple", "banana"], [True, False]]
print(nested)

#List Operations
#Concatenation (+)
list1 = [1, 2, 3]
list2 = [4, 5, 6]
result = list1 + list2  
print("Concatenation:", result)  

#Repetition (*)
nums = [1, 2, 3]
result = nums * 3  
print("Repetition:", result)  

#Membership (in, not in)
fruits = ["apple", "banana", "cherry"]
print("Is 'apple' in fruits?", "apple" in fruits)     
print("Is 'mango' not in fruits?", "mango" not in fruits) 

#Length (len())
numbers = [10, 20, 30, 40]
print("Length of numbers list:", len(numbers))  

#Indexing ([])
colors = ["red", "green", "blue"]
print("Element at index 1:", colors[1])  

#Slicing (:)
nums = [0, 1, 2, 3, 4, 5]
print("Sliced list (1:4):", nums[1:4])  

#Accessing Elements
#Direct Indexing 
Fruits = ['apple', 'banana', 'cherry']
print(Fruits[2])

#Positive Indexing
Colors = ['red', 'green', 'blue']
print(Colors[0])

#Negative Indexing
Animals = ['cat', 'dog', 'elephant']
print(Animals[-2])

#Accessing a Loop
Fruits = ['apple', 'banana', 'cherry']
for fruit in Fruits:
    print(fruit)
    
#Accessing a range 
Fruits = ['apple', 'banana', 'cherry', 'date' , 'mango' , 'kiwi']
print(Fruits[1:5])  


