arr = [1,1,1,2,2]

def removeDuplicates(arr):
    x = 1
    for i in range(1, len(arr)):
        if arr[i-1] != arr[i]:
            arr[x] = arr[i]
            x += 1
    return x, arr

# removeDuplicates(arr)
# print(arr)

arr = [0,0,1,1,1,2,2,3,3,4]
unique, arr = removeDuplicates(arr)
print(arr)