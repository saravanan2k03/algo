S=input().strip(),
X,Y = input().split()
print(S,X,Y)
repeated_string = S * len(S)
print(len(repeated_string),repeated_string)
X=int(X)
Y=int(Y)
print(S[X])
print(len())
print(repeated_string[Y])
if S[X-1] == repeated_string[Y-1]:
    print('YES')
else:
    print('NO')
