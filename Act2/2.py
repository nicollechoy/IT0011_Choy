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

def is_prime():
    try:
        num = int(input("Enter a number: "))
        
        if num <= 1:
            print(f"{num} is not a prime number")
            return
        
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                print(f"{num} is not a prime number")
                return
        
        print(f"{num} is a prime number")
    except ValueError:
        print("Invalid input! Please enter a valid number.")

compute_sum()
is_prime()
