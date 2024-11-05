
#In this program you will calculate the age difference between the user and Alan Turing, and print the result. 
#Proceed with the following instructions:

#Create a new file called program1.py


# Declare a constant and store Alan Turing's birth year, 1912.
# In Python, constants (variables with fixed values) are typically written in uppercase to indicate they shouldn't change.  
# Though not enforced by Python, using uppercase variable names improves readability and helps distinguish constants from regular variables.
# Naming convention: Snake Case (snake_case) is used for readability, with underscores separating words. 
# Assignment operator "=" assigns the value 1912 to the variable.
ALAN_TURING_BIRTH_YEAR = 1912


# Prompt the user to enter their year of birth and store it in a variable.
# Naming convention: Underscores are used as word separators to enhance readability.
# input(x) function: Collects user input as a string.
# int(x) function: Converts the input string to an integer for numerical operations.
# Assignment operator "=" assigns the converted integer value to the variable.
user_enter_your_birth_year = int(input("Enter your year of birth: "))


# Calculate the difference between the user's birth year and Alan Turing's birth year. Store the result in a variable.
# abs(x) function: Returns the absolute value of the difference to ensure a positive result.
# Arithmetic operator "-" : Used for subtraction.
# Assignment operator "=" assigns the calculated result to the variable.
age_difference=abs(user_enter_your_birth_year - ALAN_TURING_BIRTH_YEAR)

# Print the difference between the user's birth year and Turing's birth year. The output should be formatted as shown in the example run. 
# Use string concatenation to combine the strings and the variable (not f-strings).
# Conditional Statements "if" statement Executes a block of code if a condition is True.
#	Python's built-in functions print(*objects, sep=' ', end='\n', file=sys.stdout) Prints objects to the console or another file, Or Python's built-in function str([object], encoding='utf-8', errors='strict')
# Conditional Statements else: Executes a block of code if all previous conditions are False.
#    print("You are " + str(age_difference) + " years younger than Alan Turing.")
if user_enter_your_birth_year > ALAN_TURING_BIRTH_YEAR: 
    print("You are " + str(age_difference) + " years younger than Alan Turing.")
else:
    print("You are " + str(age_difference) + " years older than Alan Turing.")











