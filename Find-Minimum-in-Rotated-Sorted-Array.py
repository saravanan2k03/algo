nums = [11,13,15,17]
ans=float("inf")


def Searchminval(nums,ans):
    low,high=0,len(nums)-1
    while(low <= high):
        mid = (high + low) //2
        if nums[low] <= nums[mid]:
            ans = min(ans,nums[low])
            low = mid+1
        else:
            ans = min(ans,nums[mid])
            high = mid-1
    return ans

val = Searchminval(nums,ans)
print(val)




# def findMin(nums) -> int:
#     l, r = 0, len(nums) - 1
#     while nums[r] < nums[l]:
#         mid = (l+r)//2
#         print(mid)
#         if nums[mid] < nums[r]: #if right part is sorted
#             r = mid
#         else: #if left part is sorted
#             l = mid + 1
        
#     return nums[l]

# val = findMin(nums)

# print(val)