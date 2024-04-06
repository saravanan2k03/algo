def sub1(a):
    b=2
    return a+b
def sub2(c):
    d = sub1(c)
    return c+d

result1 = sub1(4)
result2 = sub2(7)

print (result1, result2)


def natural(n):
    if n==1:
        return
    print(n)
    return natural(n-1)


natural(10)


def fact(n):
    if n == 0:
        return 1
    return n * fact(n-1)



print(fact(5))

count = 0
def printer(name):
    global count
    if count <=10:
        print(name)
        count +=1
        printer(name)
    


printer('saravanan')



n = 10
res = []

for i in range(1,n):
    if i == 1:
        res.append(i)
    else:
        res.append(sum(res))

print(res)