def Doixung(a):
    c=0
    for i in range(len(a)):
        for j in range(len(a)):
            if a[i][j]!=a[j][i]:
                c+=1
    if c!=0 :
        return False
    else:
        return True

a=[[1,1,1],[1,1,1],[1,1,1]]
b=[[1,2,3],[4,5,6],[7,8,9]]
print(Doixung(a))
print(Doixung(b))



