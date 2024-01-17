N=int(input())
state=[]
capital=[]
val=''
for i in range(N):
    sta,cap=map(str,input().split())
    state.append(sta)
    capital.append(cap)
c=input().strip()
for i in range(len(state)):
    if c == state[i]:
        print(capital[i])
        break
    else:
        val='NONE'
print(val)



# 10 
# Rwanda Kigali 
# Afghanistan Kabul
# Austria Vienna 
# Armenia Yerevan 
# Uganda Kampala 
# Zimbabwe Harare 
# Syria Damascus 
# Senegal Dakar 
# Sweden Stockholm 
# Libya Tripoli 
# Pakistan


# 5 
# Kosovo Pristina 
# Kenya Nairobi 
# Pakistan Islamabad 
# India Delhi 
# Srilanka Colombo 
# Kenya