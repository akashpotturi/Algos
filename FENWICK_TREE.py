n = int(input())
bit = [0]*(n+1)
a = [0]*(n+1)

def update(id,val):
    while id<=n:
        bit[id]+=val
        id+=(id&-id)
        
def query(id):
    ans = 0
    while id>0:
        ans+=bit[id]
        id-=(id&-id)
    return ans

for i in range(1,n+1):
    a[i] = int(input())
    update(i,a[i])

q = int(input())
while q>0:
    typeofquery = int(input())
    if typeofquery == 1:
        l,r = map(int,input().split())
        ans = query(r)-query(l-1)#l and r should be 1 based
        print(ans)
    else:
        id,val = map(int,input().split())
        update(id,-a[id])#take out the contribution of previous value  
        a[id] = val
        update(id,a[id])#update the contribution of new value

    q-=1