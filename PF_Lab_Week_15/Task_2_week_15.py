try:
    num = int(input("Write any number: "))/int(input("Write any number: "))
except ZeroDivisionError:
    print("Cannot divide by zero.")
else:
    print(f"Success! Result: {num}")