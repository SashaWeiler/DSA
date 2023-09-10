
# itsa no good
# def removeElement(nums, val):
#     l = 0
#     num_of_vals = 0
#     duplicate_found = False
#     for i in range(0, len(nums)):
#         if (nums[i] == val) and duplicate_found == False:
#             l = i
#             duplicate_found = True
#             num_of_vals += 1

#         elif (nums[i] == val) and duplicate_found == True:
#             num_of_vals += 1
#             continue
        
#         elif (nums[i] != val):
#             nums[l] = nums[i]
#             l += 1
#             duplicate_found = False
            
#     return len(nums) - num_of_vals


def removeElement(nums, val):
    k = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k +=1
    
    return k
arr = [0,1,2,2,3,0,4,2]
unique = removeElement(arr, 2)
print(unique, arr)