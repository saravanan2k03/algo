S=str(input())
A=str(input())
B=str(input())
count=0
for i in range(0,len(S)):
    try:
        if S[i] == A and S[i+1] == B:
            count +=1
        
    except IndexError:
        break
print(count)    

##amapodumadam
##a
##m