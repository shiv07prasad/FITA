n = 10

a, b = 0, 1  # First two terms

for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b  # Update values
