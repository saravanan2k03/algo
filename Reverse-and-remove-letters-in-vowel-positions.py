S=input().strip()
ans=''
vowels='aeiouAEIOU'
positions = []
for i,char in enumerate(S):
    if char in vowels:
        positions.append(i+1)
S=S[::-1]
print(positions)
print(S)

for i in range(len(S)):
    if i+1 in positions:
        print(S[i])
    else:
        ans+=S[i]
print(ans)