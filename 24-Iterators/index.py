# Iterators : An object in Python that allows you to loop through a sequence (like list, tuple, or 
# string) one element at a time
nums = [10, 20, 30]
it = iter(nums)
print(next(it))   
print(next(it)) 
print(next(it)) 
print() 

# Iterator Inside a Function
def show():
    nums = [5, 6, 7]
    it = iter(nums)
    print("Iterator Inside Function:")
    print(next(it))
    print(next(it))
    print(next(it))

show()
print()

# Iterator Used by For Loop
nums2 = [1, 2, 3]
print("Iterator with For Loop:")
for n in nums2:   
    print(n)