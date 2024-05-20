# Minimize maximum adjacent difference in a path from top-left to bottom-right

# Python code to implement the above approach

m, n = 0, 0


# Function to check if there is a valid path
def isValid(i, j, x, visited, arr, parent):
    # Check if we go outside the matrix or
    # cell(i, j) is visited or absolute
    # difference between consecutive cell
    # is greater than our assumed maximum
    # energy required If true,
    # then return false
    if (i < 0 or j < 0 or i >= m or j >= n or visited[i][j] or abs(arr[i][j] - parent) > x):
        return False

    # Check if we reach at bottom-right
    # cell If true, then return true
    if (i == m - 1 and j == n - 1):
        return True

    # Make the current cell(i, j) visited
    visited[i][j] = True

    # Make all four direction call and
    # check if any path is valid If true,
    # then return true.
    if (isValid(i + 1, j, x, visited, arr, arr[i][j])):
        return True
    if (isValid(i - 1, j, x, visited, arr, arr[i][j])):
        return True
    if (isValid(i, j + 1, x, visited, arr, arr[i][j])):
        return True
    if (isValid(i, j - 1, x, visited, arr, arr[i][j])):
        return True

    # Otherwise, return false
    return False


# Function to find the minimum value among
# the maximum adjacent differences
def minimumEnergyPath(arr):
    # Initialize a variable start = 0
    # and end = maximum possible
    # energy required
    start, end = 0, 10000000

    # Initialize a variable result
    result = arr[0][0]

    # Loop to implement the binary search
    while (start <= end):
        mid = (start + end) // 2

        # Initialize a visited array
        # of size (m * n)
        visited = [[False for i in range(n)] for j in range(m)]

        # Check if mid energy is valid
        # energy required by choosing any
        # path into the matrix If true,
        # update the result and
        # move end to mid - 1
        if (isValid(0, 0, mid, visited, arr, arr[0][0])):
            result = mid
            end = mid - 1

        # Otherwise, move start to mid + 1
        else:
            start = mid + 1

    # Return the result
    return result


# Driver Code
arr = [[1, 2, 1], [2, 8, 2], [2, 4, 2]]
m = len(arr)
n = len(arr[0])

# Function Call
print(minimumEnergyPath(arr))

# This code is contributed by Pushpesh Raj.
