a=int(input())
l=[]
v=[]
k=[]
for i in range(a):
    l.append(input())
    v.append(float(input()))
g=min(v)
for j in range(len(l)):
    if v[j]==g:
        l.remove(l[j])
    
v.remove(g)

for i in range(len(v)):
    if(min(v)==v[i]):
        k.append(l[i])
d=sorted(k)
print(d)
for i in d:
    print(i)
    
        
