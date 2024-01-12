#gfg potd Techfest and queeue with seive
'''import math
def seive(n):
    q=[]
    l=[True for i in range(n+1)]
    p=2
    while(p*p<=n):
        if l[p]:
            for i in range(p*p,n+1,p):
                l[i]=False
        p+=1
    for j in range(2,n+1):
        if l[j]:
            q.append(j)
    return q
def primeseive(n):
    array=[0 for k in range(n+1)]
    prime=seive(n)
    for a in prime:
        if array[a]==0:
            array[a]=a
            while(a*a<=n+1):
                if array[a]:
                    for i in range(a*a,n+1,a):
                        if array[i]==0:
                            array[i]=a
                a+=1
    return array
l=24
r=27
c=0
new=primeseive(r)
for i in range(l,r+1):
    p=new[i]
    if p:
        while(new[i]):
            q=i//new[i]
            c+=1
            i=q
print(c)'''
####
import math
def seive(n):
    q=[]
    l=[True for i in range(n+1)]
    p=2
    while(p*p<=n):
        if l[p]:
            for i in range(p*p,n+1,p):
                l[i]=False
        p+=1
    for j in range(2,n+1):
        if l[j]:
            q.append(j)
    return q
def primeseive(n):
    array=[0 for k in range(n+1)]
    prime=seive(n)
    for a in prime:
        if array[a]==0:
            array[a]=a
            while(a*a<=n+1):
                if array[a]:
                    for i in range(a*a,n+1,a):
                        if array[i]==0:
                            array[i]=a
                a+=1
    return array
w=list(map(int,input().split()))#246
new=primeseive(max(w))#6
r=[]
for i in w:
    while(i):
        r.append(new[i])#2#2#2
        p=i//new[i]#1#2
        if p!=1:
            i=p#2
        if p==1:
            break
print(r)
l1=list(set(r))
s=1
for k in range(len(l1)):
    s*=(r.count(l1[k])+1)
print(s)
    
        
    
    
