def trungCot(a):
    c=0
    d=0
    for i in range(len(a)-1):
        for j in range(len(a)):
            if a[j][i]==a[j][i+1]:
                c+=1
                if c==len(a):
                    d+=1
                    c=0
            else:
                c*=0
    for j in range(len(a)):
        if a[j][len(a)-1]==a[j][0]:
            c += 1
            if c == len(a):
                d+=1
        else:
            c*= 0
    if d!=0:
        return True
    else:
        return False

b=[[1,1,1],[1,1,1],[1,0,1]]
c=[[1,1,1],[1,1,1],[1,2,3]]
print(trungCot(b))
print(trungCot(c))
