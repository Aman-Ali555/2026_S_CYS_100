user = int(input("Write any number: "))
try:
    num = int(user)
    result = 100 / num
except ValueError:
    print("Error: Input must be a number.")
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
else:
    print(f"Division successful: {result}")
finally:
    print("Program execution cycle complete.")