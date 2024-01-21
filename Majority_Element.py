nums = [3,2,3]
res={}

for i in nums:
    if i in res:
        res[i] +=1
    else:
        res[i] =1
print(res)

op=max(res,key=res.get)
print(op)