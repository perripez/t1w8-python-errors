def divide_numbers():
    try:
        # Get inout from the user
        dividend = float(input("Enter the dividend: "))
        divider= float(input("Enter the divider: "))

        # Perform the division
        result = dividend / divider
        print(f"Result of the division: {result}")
    
    except ZeroDivisionError:
        print("Error! Division by 0 is not allowed silly")
    
    except ValueError:
        print("Error! What the heck are you doing? Please enter valid numbers")
    
    except Exception as e:
        print(f"An unexpected error has occured:{e}")
    
    finally:
        print("Division operation closed.")

# Perfom the division
divide_numbers()
