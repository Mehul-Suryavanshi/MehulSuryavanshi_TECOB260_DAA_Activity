def rotate(a,m,n,r,c):
    dim=c
    cm=m-2*c
    cn=n-2*c
    s=[]
    for i in range(c,c+cm):
        s.append(a[i][c])
    for i in range(c+1,c+cn):
        s.append(a[c+cm-1][i])
    for i in range(c+cm-2,c-1,-1):
        s.append(a[i][c+cn-1])
    for i in range(c+cn-2,c,-1):
        s.append(a[c][i])
    lens=len(s)
    r = r % lens
    circle=[]
    circle=s[(lens-r):]+s[:(lens-r)]
    index=0
    for i in range(c,c+cm):
        a[i][c]=circle[index]
        index+=1
    for i in range(c+1,c+cn):
        a[c+cm-1][i]=circle[index]
        index+=1
    for i in range(c+cm-2,c-1,-1):
        a[i][c+cn-1]=circle[index]
        index+=1
    for i in range(c+cn-2,c,-1):
        a[c][i]=circle[index]
        index+=1
    return a

m,n,r=[int(i) for i in input().split(" ")]
s=[]
for i in range(m):
    s.append([int(i) for i in input().split(" ")])
d=min(m,n)//2
for i in range(d):
    rotate(s,m,n,r,i)
for i in range(m):
    x=""
    for j in range(n):
       x=x+str(s[i][j])+" "
    print(x)