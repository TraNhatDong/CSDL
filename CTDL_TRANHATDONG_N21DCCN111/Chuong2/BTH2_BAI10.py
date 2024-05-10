def trungCot(a):
    c=0
    d=[]
    for i in range(len(a)-1):
        for j in range(len(a)):
            if a[j][i]==a[j][i+1]:
                c+=1
                if c==len(a):
                    d.append(i)
                    c=0
            else:
                c*=0
    for j in range(len(a)):
        if a[j][len(a)-1]==a[j][0]:
            c += 1
            if c == len(a):
                d.append(len(a)-1)
        else:
            c*= 0
    for i in range(len(d)):
        if d[i]==len(a)-1:
            print("Cột (0,"+str(d[i])+") :",end="")
            print(a[i])
        else:
            print("Cột ("+str(d[i])+","+str(d[i]+1)+") :",end="")
            print(a[i])
b=[[1,1,1],[1,1,1],[1,1,0]]
trungCot(b)