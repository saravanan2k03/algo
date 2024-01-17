# L1L,L2L=input().split()
L1 = input("Enter the first value: ").strip().split(' ')
L2 = input("Enter the second value: ").strip().split(' ')
print(L1)
print(L2)
lst = L1+L2
finallst=list(lst)
l1in=[]
B=[]
for i in finallst:
    if i not in B:
        B.append(i)
    else:
        l1in.append(i)

A = set(l1in)
for i in A:
    B.remove(i)
print(len(B))









# 100 23 31
# 23 31 100

# 6 5
# 1 5 9 10 29 31
# 22 5 12 9 5