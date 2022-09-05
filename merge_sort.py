def mergeSort(inputList):
    length = len(inputList)
    # Base case for recursion (infinite loop without this!)
    if length <= 1:
        return inputList

    print(f'mergeSort called with a list of length {length}: {inputList}')

    middleIndex = length // 2
    left = inputList[:middleIndex]
    right = inputList[middleIndex:]

    left = mergeSort(left)
    right = mergeSort(right)
    return list(merge(left, right))


def merge(left, right):
    print(f'Merging two lists of length {len(left)} and {len(right)}')
    return left + right

# Implement a merge sort for a list of integers. Your solution must run in O(n*logn) time for a list of length n.

# Input: unsorted list of integer values, e.g., [1, 9, -32, 4]
# Output: sorted list of integer values, e.g., [-32, 1, 4, 9]

# The starter code contains the scaffolding for a working merge sort algorithm. It recursively divides the list then puts it back together, but all of the sorting-specific logic is missing.

# Test cases:
unsortedList = [1, 97, 36, -4, 0, 124, 3000]
print(mergeSort(unsortedList)) # -4, 0, 1, 36, 97, 124, 3000