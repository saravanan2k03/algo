nums = [2,7,11,15]
target = 9

for i in range(len(nums)):
    for j in range(len(nums)):
        if i != j:
            sumval = nums[i] + nums[j]
            if sumval == target:
               print(i,j)
               print(sumval)


        # print(sumval)
        
            

                