# matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 13
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]

for nums in matrix:
    l=0
    r=len(nums)-1
    nums.sort()
    while l <= r:
        mid = (l+r)//2
        if nums[mid] < target:
            l= mid+1
        elif nums[mid] > target:
            r= mid-1
        else:
            print(nums[mid])
            break
    break