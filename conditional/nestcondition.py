calculation_to_units = 24
name_of_unit = "hours"

def days_to_unit(number_of_days):
    if number_of_days > 0:
        return f"{number_of_days} days are {number_of_days * calculation_to_units} {name_of_unit}"
    elif number_of_days == 0:
        return "You entered 0 days, which equals 0 hours"
    else:
        return "You have entered a negative number, so it cannot be converted"

def validate_and_execute():
    if user_input.isdigit():
        user_input_number = int(user_input)
        if user_input_number > 0:
            calculated_value = days_to_unit(user_input_number)  # FIXED
            print(calculated_value)
        elif user_input_number == 0:
            print("You have entered a negative number, so it cannot be converted")
    else:
        print("Please enter a valid number")

user_input = input("Enter number of days you want to calculate: ")
validate_and_execute()


