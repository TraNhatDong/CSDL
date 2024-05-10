def chuoiConDauTien(a,b):
    c=[]
    d=[]
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i]==b[j]:
                while(a[i+1]==b[j+1]):
                    c.append(a[i])
        d.append(c)
    print(c)
    print(d)
a=[6,5,3,7,8,9,0,2]
b=[2,3,7,8,9,2,7,3]
print(chuoiConDauTien(a,b))
