# HW3_P1: Exceptional Weather Forecast

# Task 1: Start
'''
Begin by setting up a simple user input loop that asks the user to enter 
the temperature in Fahrenheit.

Ensure that your program only accepts numerical input and provides a friendly 
error message if the user enters something that can't be converted to a number.
'''

while True:
    try:
        temperature = float(input("Please enter temperature in Fahrenheit: "))
        break
    except ValueError:
        print("Please try again, seems you did not enter a proper temperature in Fahrenheit.")


# Task 2: Temperature Conversion
'''
Write a function that converts the Fahrenheit temperature to Celsius. 
Remember that the formula is (Fahrenheit - 32) * 5/9.

Use a try block to catch any potential errors during the conversion process, 
such as division by zero or overflow errors.
'''

def conv_celsius(temp):
    try:
        celsius = (temp - 32) * 5 / 9
        return celsius
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Task 3: User Experience
'''
Implement an else block that prints the converted temperature in a 
user-friendly format.

Add a finally block that thanks the user for using the weather forecast 
application, ensuring that this message is displayed regardless of whether 
an exception was caught or not.
'''

conv_celsius(temperature)
try:
    print(f"The given temperature in Celsius is {conv_celsius(temperature)}°C")
finally:
    print("Thank you so much for trusting our Weather Forcast Application!")
