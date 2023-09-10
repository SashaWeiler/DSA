# Remove value at index i before shifting elements to the left.
# Assuming i is a valid index.
def removeMiddle(arr, i, length):
    # Shift starting from i + 1 to end.
    for index in range(i + 1, length):
        arr[index - 1] = arr[index]
        a=0
    # No need to 'remove' arr[i], since we already shifted

arr = [4,5,6]
removeMiddle(arr, 0, len(arr))
print(arr)
arr = [4,5,6]

def insertMiddle(arr, i, n, length):
    # Shift starting from the end to i.
    for index in range(length - 2, i - 1, -1):
        arr[index + 1] = arr[index]
        print(index)
    
    # Insert at i
    arr[i] = n
    
insertMiddle(arr, 1, 8, len(arr))
print(arr)