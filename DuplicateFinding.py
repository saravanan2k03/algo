lst = [1,1,1,3,3,4,3,2,4,2]


def duplicate(lst):
    hashset = set()
    for i in range(len(lst)):
        if lst[i] in hashset:
            return True
        else:
            hashset.add(lst[i])
    return False

print(duplicate(lst))

# for i in range(len(lst)):
#     print(lst[i],lst.count(lst[i]))