def giaiThua(n):
    if n==0:
        return 1
    else:
        return giaiThua(n-1)*n
def Neper(n):
    assert n >= 0 and int(n) == n
    a=0
    for i in range(0,n+1):
        a+=1/(giaiThua(i))
    return a
print(Neper(2))
