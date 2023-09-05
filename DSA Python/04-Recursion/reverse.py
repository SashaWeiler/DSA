def reverse(start, stop, s):
    if start < stop -1:
        s[start], s[stop-1] = s[stop-1], s[start]
        reverse(start+1, stop-1, s)

arr = [1,2,3,4,5,6,7]

print(arr)

reverse(0, 4, arr)

print(arr)