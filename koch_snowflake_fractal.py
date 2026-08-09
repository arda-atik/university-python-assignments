def koch_length(n, s):
    """
    Recursively calculates the perimeter of a Koch snowflake.
    n: Number of iterations (int >= 1)
    s: Initial side length (float or int >= 0)
    Returns the perimeter length, or None if preconditions are not met.
    """
    # Check preconditions
    if not isinstance(n, int) or n < 1:
        return None
    if s < 0:
        return None
        
    # Base case: initial equilateral triangle
    if n == 1:
        return s * 3
        
    # Recursive step: perimeter increases by a factor of 4/3 at each iteration
    return koch_length(n - 1, s) * (4 / 3)
