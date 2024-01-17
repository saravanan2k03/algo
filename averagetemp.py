inp = int(input("Enter the Temperature:"))
mylist = []
count = 0
for i in range(0,inp):
    inp = float(input("Enter the Temperature"))
    mylist.append(inp)


print(mylist)

value = sum(mylist) / len(mylist)
new_list = [i for i in mylist if i==value]
for i in mylist:
    if i==value:
        count +=1 
    
    
print(value)
print(count)
print(new_list)
print(len(new_list))