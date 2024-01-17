arr = [1, 7, 3, 4, 9, 5] 
# result = []
# for i in range(len(arr)):
#     for j in range(len(arr)):
#         if i != j:
#             result.append(arr[i]*arr[j])
# print(max(result))
            
firstmax = max(arr)
arr.remove(firstmax)
secondmax = max(arr)
print(firstmax * secondmax)