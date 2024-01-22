
nums = [-1,0,1,2,-1,-4]
ans=[]
nums.sort()
for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            x=i
            left = i+1
            right = len(nums)-1
            sumval=0
            while left < right:
                sumval = nums[x]+nums[left]+nums[right]
                triplet = [nums[x],nums[left],nums[right]]
                if sumval == 0:
                    ans.append(triplet)
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left +=1
                    right -=1
                else:
                    if sumval > 0:
                        right -=1
                    else:
                        left+=1
print(ans)

        