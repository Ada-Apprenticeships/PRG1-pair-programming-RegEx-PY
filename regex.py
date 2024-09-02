import re

# Regular expressions
valid_whole_number_regex = r"^[0-9]+$"
valid_positive_whole_decimal_number = r"^(?:0|[1-9]\d*)(?:\.\d+)?$"
valid_floating_point_2dp = r"^[0-9]+\.[0-9][0-9]$"
valid_alphabetic_string = r"^[A-Za-z]+$"

# Test a regular expression
if re.match(valid_whole_number_regex, "456"):
    print("Match found!")
else:
    print("No match.")





# Example code from the lesson slides

# def valid_input(user_input):
#     """Checks if the input consists only of alphabetic characters."""
#     alphabetic_regex = r"^[A-Za-z]+$" 
#     return bool(re.match(alphabetic_regex, user_input))

# while True:
#     user_input = input("Please enter alpha characters only: ")
#     if valid_input(user_input):
#         print("Thank you. Please continue.")
#         break
#     else:
#         print("Incorrect input.")
