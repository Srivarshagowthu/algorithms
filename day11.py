##a=[2,3,5,7,11,13,17,19,23]
##c=0
##for i in range(len(a)):
##    for j in range(i+1,len(a)):
##        for k in range(j+1,len(a)):
##            if a[i]<a[j]<a[k]:
##                if a[i]+a[j]==a[k]:
##                    if a[k]<=25:
##                    c+=1
##print(c)
############SEIVE##########
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
#####################################################
#segmented seive
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
def seg(l,r):
    k=int(math.floor(math.sqrt(r))+1)
    primes=seive(k)
    array=[True for i in range(r-l+1)]
    for j in (primes):
        w=(l//j)*j#209
        if(w < l):
            w += j
        while(w<=r):
            array[w-l]=False
            w+=j
    return [i for i in range(l, r + 1) if array[i - l]]
l=10
r=50
print(seg(l,r))
######################################################################
#prime in a range using seive and segmented
import math
class Solution:        
    def primeRange(self,M,N):
        #code here
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
        def seg(l,r):
            ans=[]
            k=int(math.floor(math.sqrt(r))+1)#4
            primes=seive(k)
            array=[True for i in range(r-l+1)]
            for j in (primes):
                w=(l//j)*j
                if(w<l):
                    w+=j
                if(j*j > w): w = j* j;#
                while(w<=r):
                    array[w-l]=False
                    w+=j
            for b in range(l,r+1):
                if array[b-l]:
                    ans.append(b)
            if l==1:
                return ans[1::]
            else:
                return ans
Note: no need to use segmented seive if the constraints aee under 10**6
                
    
    

