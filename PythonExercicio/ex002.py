"""
Create a program that reads a person's age for calculate the next Birthday and display it on the screen
"""

# The "input()" function allows user input, and it will be representing a default message before the input

# We're going to convert the user's age to an integer number using the "int()" function.

# Then, we'll add 1 (year) to that age.

# On the final line of our code, we allow our value to print on the screen, alongside a short message.

# Let's check the code in action:

age = int(input('Hello, tell us your age: '))

final_age = float(age + 1)

print(f'\nOn your next Birthday, you will be: {final_age} years old! \n')

ages = [age, final_age]

ages_dictionary = dict.fromkeys(ages, "Age's Vitor")

print(ages_dictionary)
