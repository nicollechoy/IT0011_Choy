def compute_sum():
    try:
        first = int(input("Enter first term number: "))
        last = int(input("Enter last term number: "))
        
        if first > last:
            print("First term is greater than the last term. Swapping the values.")
            first, last = last, first  
        
        print(f"First term: {first}, Last term: {last}")  # Debugging output
        
        total = 0
        for num in range(first, last + 1):
            total += num
        
        print(f"The sum of the numbers from {first} to {last} is {total}")
    except ValueError:
        print("Invalid input! Please enter a valid number.")

compute_sum()
