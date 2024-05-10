def tongUocSo(n):
    a=0
    for i in range(1,n):
        if n%i==0:
            a+=i
    return a
def Number(a,b):
    for n in range(a,b+1):
        if tongUocSo(n)<n:
            print("Số "+str(n)+" là deficient")
        elif tongUocSo(n)==n:
            print("Số "+str(n)+" là perfect")
        else:
            print("Số "+str(n)+" là abundant")
Number(6,12)