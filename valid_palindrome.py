s = "race a car"
s=''.join(e for e in s if e.isalpha())
s=s.lower()
s= s.replace(":","")
s=s.replace(",","")
s= s.replace(" ","")
print(len(s))

if len(s) == 0:
    print("Empty")
print(s[::-1])

if (s[::-1]) == s:
    print("same")