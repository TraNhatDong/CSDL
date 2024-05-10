def Nhan(a):
    av=1
    for i in a:
        av*=i
    return int(av)
a=[111,33]
print(Nhan(a))