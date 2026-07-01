def sum_n(n):
    if n == 1:
        return 1
    return n + sum_n(n - 1)

# Run
result = sum_n(5)
print(f"Sum is: {result}")