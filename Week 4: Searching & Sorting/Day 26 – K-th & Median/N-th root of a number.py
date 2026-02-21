def nthRoot(n, x):
    # If x is negative and n is even, no real solution exists
    if x < 0 and n % 2 == 0:
        return None
    # For positive x → root lies between 0 and max(1, x)
    # For negative x (and odd n) → root lies between x and 0
    if x >= 0:
        low = 0
        high = max(1, x)
    else:
        low = min(-1, x)
        high = 0

    # Precision value
    # We stop when the interval becomes very small.
    # This ensures the answer is accurate up to about 1e-6.
    eps = 1e-6

    # Continue binary search until the search range is small enough
    while high - low > eps:

        # Midpoint of current range
        # This is the best guess for the root in the middle of the interval
        mid = (low + high) / 2

        # If mid^n is smaller than x,
        # the root must be to the right
        if mid ** n < x:
            low = mid
        else:
            # Otherwise, the root is to the left
            high = mid

    # Return midpoint of final small interval
    # This gives the most accurate approximation
    return (low + high) / 2
if __name__ == "__main__":
    n = 2
    x = 8
    result = nthRoot(n, x)
    print("Result:", result)
#Tc: O(log(x)) Sc: O(1)
