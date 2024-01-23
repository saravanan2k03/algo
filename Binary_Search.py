nums = [-1,0,3,5,9,12] 
target = 9



if target in nums:
    for index,value in enumerate(nums):
        print(index,value)
        if value == target:
            print("target reached", index)
else:
    print("target not found", target)
