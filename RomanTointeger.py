roman = {"I": 1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
ans = 0
sub = "XII"



for i in range(len(sub)):
    print(len(sub))
    print("index",i+1)
    if i + 1 < len(sub) and roman[sub[i]] < roman[sub[i+1]]:
        ans -=roman[sub[i]]
    else:
        ans += roman[sub[i]]
print(ans)

