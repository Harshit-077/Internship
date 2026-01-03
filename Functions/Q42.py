# Calculate the sum of all elements in a list:
def suml(nums):
    if len(nums) == 0:
        return 0
    else:
        return nums[0]+suml(nums[1:])
final_sum = suml([1,2,3,4,5])
print(final_sum)