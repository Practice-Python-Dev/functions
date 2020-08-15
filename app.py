#------------------------------
# PACKING FUNCTIONS
#------------------------------

# Compress multiple values into one tuple
# Multiple arguments are packed into a singular parameter

#----- WITHOUT PACKING -----

def packer1(arg1, arg2, arg3, arg4):
    print(arg1)
    print(arg2)
    print(arg3)
    print(arg4)

packer1("hi", "i", "love", "python")

# Spacing in terminal ...
print("\n" + "-" * 20)

#----- WIIH PACKING -----

# All arguments will be converted to a tuple (* tells python to do this)
def packer2(*args):
    print(*args)

# Call function, pass four arguments
packer2("hi", "i", "love", "python")

# Spacing in terminal ...
print("\n" + "-" * 20)

#----- PACKING WITH A LOOP -----

# We can run a for loop to unpack and print each argument on another line

def packer3(*args):
    for val in args:
        print(val)

# Call function, pass four arguments
packer3("hi", "i", "love", "python")

# Spacing in terminal ...
print("\n" + "-" * 20)


#------------------------------
# UNLIMITED ARGUMENTS (*args)
#------------------------------

# Demonstrate the power of '*args'
    # The job of this function is to add up all the items in the cart
    # Using positional arguments for every item doesn't work, because we don't know how many items will be in the cart
    # E.g, 'def calculate_total(item1, item2, item3)' - what if there's a fourth parameter!!!???
    # Using '*args' as our parameter lets us pass as many arguments as we want (as a tuple)

#----- SHOPING CART APP (PRACTICE) -----

# *args works as a tuble
def calculate_total(*args):
    # Use the sum method
    total = sum(args)
    print(total)

# Pass as many arguments as you like
calculate_total(25, 25, 20, 30)

# Spacing in terminal ...
print("\n" + "-" * 20)


#------------------------------
# UNPACKING FUNCTIONS
#------------------------------

# "Exlpoding a Python sequence into individual variables"
# Sometimes called "multiple assignement" - Note, Unpacking is strict

def unpacker():
    # Tuple elements to unpack
    return (1, 2, 3)

# Call function 'unpacker', unpack the return values into the variables
var1, var2, var3 = unpacker()

print(var1, var2, var3)

# Spacing in terminal ...
print("\n" + "-" * 20)

#----- REWRITE TO RETURN STRINGS -----

def unpacker2():
    return "hey"

var1, var2, var3 = unpacker2()

# Function iterates and unpacks each letter to a variable
print(var1, var2, var3)

# Spacing in terminal ...
print("\n" + "-" * 20)

#------------------------------
# UNPACKING LISTS
#------------------------------

# Ask users to enter their full name in one input box.
# With unpacking and multiple assignment you can capture the firt name and
# last name entered by your user into their own variables in just one line of code.

# Ask for the user for their full name
    # Use the split method, the parameter it takes is the desired delimeter
    # For our case, we are using the space as the delimeter

# Store the input in multiple variables (in order)
first, last = input("Enter your full name: \n").split(" ")

# Now we're free to use these variables separately ...
print(first)
print(last)


