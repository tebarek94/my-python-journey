calculation_to_unit=24*60*60
name_of_unit='seconds'

def days_t0_unites(numbers_of_days,custom_message):
    print(f'{numbers_of_days} days are  {numbers_of_days * calculation_to_unit} {name_of_unit}')
    print("Hello World")

days_t0_unites(34,'Awesome!')
days_t0_unites(20,'Looks good')