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