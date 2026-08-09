def is_prime(n):
    """Helper function to check if n is prime."""
    if n < 2:
        return False
    for k in range(2, n):
        if n % k == 0:
            return False
    return True

def sum_primes(a, b = None):
    """Return sum of primes in range [1, a) or [a, b)."""
    s = 0
    if b == None:
        for x in range(2, a):
            if is_prime(x):
                s = s + x
    else:
        if a > b:
            return 0
        for x in range(a, b):
            if is_prime(x):
                s = s + x
    return s
