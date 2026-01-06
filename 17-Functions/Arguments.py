# Positional Arguments
def say_names_of_couple(husband_name, wife_name):
    print("The names of the couple are " + husband_name + " and " + wife_name)
say_names_of_couple("Ali", "Ayesha") 
print("-" * 40)

# Keyword Arguments
def make_shirt(size, message):
    print(f"Making a {size} shirt with message: '{message}'")

make_shirt(message="Code Everyday!", size="Large")  
print("-" * 40)

# Default Arguments
def display_result(winner, score="0-0"):
    print("The winner was " + winner)
    print("The score was " + score)

display_result("Team A")     
display_result("Team B", "5-2")    
print("-" * 40)

# Arbitrary Arguments (*args)
def make_pizza(size, *toppings):
    print(f"Making a {size}-inch pizza with toppings:")
    for t in toppings:
        print("-", t)

make_pizza(12, "pepperoni", "mushrooms", "cheese", "olives") 

# Arbitrary Arguments (**kwargs)
def show_info(**info):
    print(info)
show_info(name="Sumbal", age=20)
