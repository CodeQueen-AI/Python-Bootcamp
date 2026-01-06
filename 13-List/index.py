# Lists in Python are ordered, changeable, and can hold multiple data types They are defined using
# square brackets []
list1 = ['Apple', 'Banana', 'Cherry']
print(list1)

# Empty List → a list with no items
list2 = []
print(list2)

# Constructor List → create list using list() function
list4 = list((1,2,3,4,5))
print(list4)

# Length (len()) → counts number of items in the list
numbers = [10, 20, 30, 40]
print("Length of numbers list:", len(numbers))  

# map() → applies a function to each item in the list
nums = [5, 2, 9, 1, 7]
squared_nums = list(map(lambda x: x**2, nums))   
print(squared_nums)  

# filter() → filters items based on a condition
even_nums = list(filter(lambda x: x % 2 == 0, nums))  
print(even_nums)
