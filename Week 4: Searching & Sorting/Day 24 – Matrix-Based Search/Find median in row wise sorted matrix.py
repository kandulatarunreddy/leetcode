from bisect import bisect_right

def matrixMedian(matrix):
    # number of rows
    r = len(matrix)
    # number of columns
    c = len(matrix[0])

    # -------------------------------------------------
    # STEP 1: Find global minimum and maximum
    # -------------------------------------------------
    # Because rows are sorted:
    # - First element of each row is the row minimum
    # - Last element of each row is the row maximum

    # Find smallest first element among all rows
    low = matrix[0][0]
    for row in matrix:
        if row[0] < low:
            low = row[0]

    # Find largest last element among all rows
    high = matrix[0][-1]
    for row in matrix:
        if row[-1] > high:
            high = row[-1]

    # -------------------------------------------------
    # STEP 2: Find the position of median
    # -------------------------------------------------
    # Example: 3x3 matrix → 9 elements → median = 5th element
    desired = (r * c + 1) // 2

    # -------------------------------------------------
    # STEP 3: Binary search on VALUE (not index)
    # -------------------------------------------------
    while low < high:

        # Middle value in the search range
        mid = (low + high) // 2

        # This will store how many numbers in matrix are <= mid
        count = 0

        # -------------------------------------------------
        # STEP 4: Count numbers <= mid in each row
        # -------------------------------------------------
        for row in matrix:
            # bisect_right gives index where mid would be inserted
            # That index = number of elements <= mid
            count += bisect_right(row, mid)

        # -------------------------------------------------
        # STEP 5: Adjust binary search range
        # -------------------------------------------------

        # If we found fewer numbers than needed,
        # median must be bigger → move right
        if count < desired:
            low = mid + 1

        # Otherwise we have enough numbers,
        # median is smaller or equal → move left
        else:
            high = mid

    # -------------------------------------------------
    # STEP 6: low == high → median found
    # -------------------------------------------------
    return low

nums =  [[1,3,5],
         [2,6,9],
         [3,6,9]]
print(matrixMedian(nums))
#TC: O(R.logC.log(max-min))
#R = number of rows, C = number of columns, max-min = range of numbers in matrix
#Sc: O(1)