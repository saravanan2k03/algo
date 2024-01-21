
lst = [1,2,3,4]
# result = []
# def prod(lst):
#     res = 1
#     for i in lst:
#         res *= i
#     return res
# def recprod(lst):
#     res=len(lst)

# # val = prod(lst)
# # print(val)

# # for i in lst:
# #     if i == 1:
# #         result.append(val)
# #     else:
# #         a = val / i
# #         a= int(a)
# #         result.append(a)
# # print(result)
# count = 0
# for i in range(len(lst)):
#     temp = []
#     temp.extend(lst)
#     if i == count:
#         temp.pop(i)
#         val=math.prod(temp)
#         result.append(val)
#         count+=1
# print(result)
res=[1]*(len(lst))

print(res)
prefix = 1
for i in range(len(lst)):
    res[i] = prefix
    print(prefix)
    prefix *=lst[i]
    print(prefix)
    print(res)
# print("enter")
# for i in range(len(lst) -1,-1,-1):
#     print(i)