def tamGiacDuoi(a):
    c=0
    for i in range(len(a)):
        for j in range(len(a)):
            if j>i:
                if a[i][j]!=0:
                    c+=1
    if c!=0 :
        return False
    else:
        return True

a=[[1,0,0],[1,1,0],[1,1,1]]
b=[[1,2,3],[4,5,6],[7,8,9]]
print(tamGiacDuoi(a))
print(tamGiacDuoi(b))