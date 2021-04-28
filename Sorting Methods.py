# --- Bubble Sort ---
# def sort(nums):
#     for i in range(len(nums)-1,0,-1):
#         for j in range(i):
#             if nums[j]>nums[j+1]:
#                 temp = nums[j]
#                 nums[j] = nums[j+1]
#                 nums[j+1] = temp
# nums = [23,12,56,35,78,42,91,84]
# sort(nums)
#
# for i in nums:
#     print(i)

# ---- Selection Sorting ----
def sort(list):
    for i in range(len(list)):
        minpos = i
        for j in range(i,7):
            if list[j] < list[minpos]:
                minpos = j

        temp = list[i]
        list[i] = list[minpos]
        list[minpos] = temp

        print(list)

list = [7,3,6,1,9,4,8]
sort(list)
# # print(list)
# print('sorted list is')
# for i in list:
#     print(i)