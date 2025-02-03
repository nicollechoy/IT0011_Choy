def pattern_a(n):
    for i in range(1, n + 1):
        print(" " * (n - i) + "".join(str(num) for num in range(1, i + 1)))

pattern_a(5)