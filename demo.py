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

arr=[1,2,3,4,5,6,7,8,9,10,11]
for i in range(len(arr)-2):
    print(arr[i], end = " ")



lst = [0,3,0,3]
lst2=[0,3,7,3,0,3]

l=0

while l < len(lst2):
    if len(lst2) == 0:
        break
    else:
        if lst2[l] == lst[l]:
            l+=1
        else:
            lst2.pop(l)



print(lst2)