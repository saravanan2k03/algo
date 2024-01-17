N,M=map(int,input().split())
prefertime=input().strip()
hr,mi=prefertime.split(":")
count =0
atime=input().split()
print(hr,mi,atime)
tottime = int(hr)*60+int(mi)
print(tottime)
for i in atime:
    print(i)
    lhr,lmi=i.split(":")
    ltottime = int(lhr)*60+int(lmi)
    print(ltottime)
    if tottime >= ltottime or ltottime == 0:
        count+=1

if count >=M:
    print('NO')
else:
    print('YES')








# 6 3
# 9:30
# 9:30 9:38 9:30 9:32 9:31 9:28

# 5 3
# 9:30
# 9:30 9:38 9:31 9:32 9:31

# 6 4
# 11:10
# 10:30 10:40 10:55 11:20 11:10 11:12

# 4 3
# 15:00
# 15:00 14:55 14:22 13:55