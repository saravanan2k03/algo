nums = [-1,0,3,5,9,12] 
target = 9

nums.sort()
# mid = len(nums) / 2
# print(round(mid))
# mid = int(round(mid))
# print(nums[mid])
if target in nums:
    for index,value in enumerate(nums):
        print(index,value)
        if value == target:
            print("target reached", index)
else:
    print("target not found", target)



