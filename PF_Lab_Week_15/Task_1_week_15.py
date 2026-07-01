try:
    num = int(input("Write any number: "))/int(input("Write any number: "))
    print(f"Result: {num}")
except ZeroDivisionError:
    print("Cannot divide by zero.")