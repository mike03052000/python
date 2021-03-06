# f(n+2)=f(n)+f(n+1)
# n=0, f(0)=0
# n=1, f(1)=1
def fib(n):
    if (n==0) or (n==1):
        return n
    tmp = [None] * (abs(n) + 2)
    if (n<0):
        # f(n) = f(n+2)-f(n+1)
        tmp[0], tmp[1] = 0, 1
        for i in range(0,n,-1):
            tmp[i+2]=tmp[i+1]-tmp[i]
        print('f(%d) =  %r' % (n,tmp))
        return tmp
    else:
        # f(n) = f(n-1)+f(n-2)
        tmp[0], tmp[1] = 0, 1
        for i in range(n-1):
            tmp[i+2]=tmp[i]+tmp[i+1]
        print('f(%d) =  %r' % (n,tmp))
        return tmp

for j in [-1,0,1,2,5,10]:
    print(fib(j))

t=fib(10)
print(t[9])