# arr = [[1, 2, 3, 4],
#        [4, 5, 6, 7],
#        [8, 9, 10, 11],
#        [12, 13, 14, 15]]
# for i in range(0, 4):
#     print(arr[i].pop())



#     data = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
# def fun(m):
#     v = m[0][0]
 
#     for row in m:
#         for element in row:
#             if v < element: v = element
 
#     return v
# print(fun(data[0]))



# arr = [1, 2, 3, 4, 5, 6]
# for i in range(1, 6):
#     arr[i - 1] = arr[i]
#     print(arr)
# for i in range(0, 6): 
#     print(arr[i], end = " ")

# print(arr[3:-1])
# print(arr[::-1])

from ast import List


arr=[1,2,3,4,5,6,7,8,9,10,11]
for i in range(len(arr)-2):
    print(arr[i], end = " ")



lst = [0,3,0,3]
lst2=[0,3,7,3,0,3]
result = []
l=0

while l < len(lst2):
    if len(lst2) == 0:
        break
    else:
        if lst2[l] == lst[l]:
            l+=1
        else:
            result.append(lst2.pop(l))



print(result)


totwater=0
lst = [0,1,0,2,1,0,1,3,2,1,2,1]
for i in range(1,len(lst)-1):
    leftmax = max(lst[:i])
    rightmax = max(lst[i+1:])
    unit = min(leftmax, rightmax) -lst[i]
    if unit > 0:
        totwater +=unit
print(totwater)

#     print(l)
# print(l)
    

lst = [1,2,3,4,5]
print(lst[:4])
print(lst[0:])

ls=[1]*(len(lst))
print(ls)



class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        l = 0
        r = len(height)-1
        lMax = 0
        rMax = 0
        if r < 2:
            return res

        while l < r:
            if height[l] < height[r]:
                lMax = max(lMax, height[l])
                res += lMax - height[l]
                l += 1
            else:
                rMax = max(rMax, height[r])
                res += rMax - height[r]
                r -= 1
        
        return res
    


lst = [0,1,0,2,1,0,1,3,2,1,2,1]
# if 1 < 1:
#     print("right")
# else:
#     print("left")

if lst :
    print("left")



s="saravanan"
left = 0
right = len(s)-1
result = ""
while(left <= right):
    result +=s[right]
    right-=1

print(result)

