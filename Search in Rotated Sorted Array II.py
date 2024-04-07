nums = [1,2,3,4,5,6,7,8,9,13]
target = 13
def searchtheval(nums,target) -> int:
    low,high=0,len(nums)-1
    while(low <= high):
        mid = (low + high)//2
        if nums[mid]==target :return True
        if nums[mid]==nums[low] and nums[mid] == nums[high]:
            low += 1
            high -= 1
            continue
        if nums[low]<=nums[mid] :
            if nums[low]<= target <= nums[mid] :
                high = mid -1
            else:
                low = mid + 1
        else:
            if nums[mid]<= target <= nums[high] :
                low = mid+1
            else:
                high = mid -1
    return False 


val = searchtheval(nums, target)
print(val)