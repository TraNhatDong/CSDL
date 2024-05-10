def trungHang(a):
    c=0
    d=[]
    for i in range(len(a)-1):
        for j in range(len(a)):
            if a[i][j]==a[i+1][j]:
                c+=1
                if c==len(a):
                    d.append(i)
                    c=0
            else:
                c*=0
    for j in range(len(a)):
        if a[len(a)-1][j]==a[0][j]:
            c += 1
            if c == len(a):
                d.append(len(a)-1)
        else:
            c*= 0
    for i in range(len(d)):
        if d[i]==len(a)-1:
            print("Hàng (0,"+str(d[i])+") :",end="")
            print(a[i])
        else:
            print("Hàng ("+str(d[i])+","+str(d[i]+1)+") :",end="")
            print(a[i])
b=[[1,1,1],[1,1,1],[1,1,1]]
trungHang(b)