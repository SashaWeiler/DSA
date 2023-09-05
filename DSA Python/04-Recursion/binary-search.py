"""
Consider three cases:
1. if target equals data at the midpoint, then it has been found
2. if data at the midpoint is less than the target, cut off the left side, low is now mid + 1
3. opposite, cut off the right side, now hi is mid -1

Use recursion
"""

def bin_search(target, arr, lo, hi, tries=1):

    if lo>hi:
        return (-1, tries)
    else:
        mid = int((lo+hi)/2)
        if arr[mid] == target:
            return (mid, tries)
        elif arr[mid] < target:
            return bin_search(target, arr, (mid+1), hi, tries+1)
        else:
            return bin_search(target, arr, lo, (mid-1), tries+1)

my_arr = [2,4,5,7,8,9,12,14,17,19,22,25,27,28,33,37]

index, tries = bin_search(7, my_arr, 0, len(my_arr)-1)
print(index)
print(tries)