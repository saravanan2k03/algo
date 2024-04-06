n = 10
res = []

for i in range(1,n):
    if i == 1:
        res.append(i)
    else:
        res.append(sum(res))

print(res)