def print_stars(n):
    if n < 1:
        return
    print("*" * n)
    print_stars(n - 1)

# Run
print_stars(5)