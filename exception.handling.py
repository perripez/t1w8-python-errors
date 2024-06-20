def convert_to_int(value):
    try:
        result = int(value)
        print(f'Conversion Succesful! Result: {result}')
    except ValueError:
        print('Conversion failed. Please enter a valid number')
    finally:
        print("Closing any open resources")

# User input
user_input=input("Enter a number to convert to integer: ")

# Cnvert to integer
convert_to_int(user_input)