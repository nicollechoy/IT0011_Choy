def pattern_b(n):
    i = 1
    while i <= n:
        if i % 2 == 1 or i == 6:  # Print for odd numbers and include 6
            print(str(i) * i)
        i += 1

print("Pattern B:")
pattern_b(7)