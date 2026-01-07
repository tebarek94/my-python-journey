calculation_to_units = 24
name_of_unit = "hours"
calculated_value = calculation_to_units * calculation_to_units

def days_to_unit(number_of_days):
    if number_of_days > 0:
        return f"{number_of_days} days are {number_of_days * calculation_to_units} {name_of_unit}"
    elif number_of_days == 0:
        return "You entered 0 days, which equals 0 seconds"
    else:
        return "You have entered a negative number, so it cannot be converted"

try:
    user_input = input("Enter number of days you want to calculate: ")
    if(user_input.isdigit()):
        user_input_number= int(user_input)
        calculated_value = days_to_unit(user_input)
        print(calculated_value)
    else:
        print("Please enter a number")
except ValueError:
    print("Invalid input. Please enter a valid integer.")
