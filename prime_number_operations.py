def is_prime(n):
    """Helper function to check if a given number is prime."""
    if n < 2:
        return False
        
    for k in range(2, n):
        if n % k == 0:
            return False
            
    return True

def sum_primes(a, b=None):
    """
    Calculates the sum of prime numbers in a given range.
    If only 'a' is provided: returns the sum in interval [1, a).
    If both 'a' and 'b' are provided: returns the sum in interval [a, b).
    """
    total_sum = 0

    if b is None:
        # Sum primes in interval [1, a)
        for x in range(2, a):
            if is_prime(x):
                total_sum += x
    else:
        # Return 0 if the interval is invalid (empty or a > b)
        if a > b:
            return 0
            
        # Sum primes in interval [a, b)
        for x in range(a, b):
            if is_prime(x):
                total_sum += x

    return total_sum
