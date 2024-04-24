s ="abcabcbb"
charset = set()
l=0
res =0
for r in range(len(s)):
    print("starting..")
    print("r",r,s[r])
    while s[r] in charset:
        print("charset",charset)
        charset.remove(s[l])
        l+=1
    print("l",l)
    charset.add(s[r])
    print("afteradding",charset)
    res=max(res,r-l+1)
    print("res",res)
    print("ending..")


print("final..")
print(res)
