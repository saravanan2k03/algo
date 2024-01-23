height = [1,8,6,2,5,4,8,3,7]
# height = [1,1]


left = 0
right = len(height)-1
maxArea = 0


while left < right:
    area = min(height[left],height[right]) * abs(left - right)
    maxArea = max(maxArea,area)

    if height[left] < height[right]:
        left +=1
    else :
        right -=1



print(maxArea)