#n = int(input())
# nlist = [float(input()) for i in range(n)]
nlist=[1.3, 4.5,2.2, 6.7]
n=len(nlist)

for i in range(1,n+1):
    newlist=sorted(nlist[0:i])
    if i % 2 == 1:
        print("%0.1f" % newlist[int(i/2)])
    else:
        m = int(i/2)
        v= (newlist[m-1]+newlist[m]) / 2
        print("%0.1f" % v)