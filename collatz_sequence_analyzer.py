# Read n (first term) and k (the k-th even term) from the user
n = int(input())
k = int(input())

X = -1  # Largest odd number
Y = 0   # Number of terms in the interval [10, 100)
Z = -1  # The k-th even term

if n >= 1:
    while True:
        # X: Update the largest odd number
        if n % 2 == 1 and n > X:
            X = n
        
        # Y: Count terms between 10 (inclusive) and 100 (exclusive)
        if 10 <= n < 100:
            Y += 1
            
        # Z: Find the k-th even number
        if n % 2 == 0 and Z == -1:
            if k > 0:
                k -= 1
                if k == 0:
                    Z = n
                    
        # Terminate the loop when the sequence reaches 1
        if n == 1:
            break
            
        # Collatz Rule: Divide by 2 if even, multiply by 3 and add 1 if odd
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1

# Print the results on a single line, separated by a single space
print(f"{X} {Y} {Z}")
