# List
list1 = ['Apple' , 'Banana' , 'Cherry']
print(list1)

# Empty List 
list2 = []
print(list2)

# Constructor List
list4 = list((1,2,3,4,5))
print(list4)

# Length (len())
numbers = [10, 20, 30, 40]
print("Length of numbers list:", len(numbers))  

# List
nums = [5, 2, 9, 1, 7]

# map() → square each number
squared_nums = list(map(lambda x: x**2, nums))
print(squared_nums)  

# filter() → keep only even numbers
even_nums = list(filter(lambda x: x % 2 == 0, nums))
print(even_nums) 
