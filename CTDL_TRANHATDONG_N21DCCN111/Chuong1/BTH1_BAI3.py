def GCD_dequy(a,b):
    assert int(a)==a and int(b)==b and a>=0 and b>=0
    if b==0:
        return a
    else:
        return GCD_dequy(b,a%b)
print(GCD_dequy(372,84))
def GCD(a,b):
    c=min(a,b)
    d=0
    for i in range(c,0,-1):
        if(a%i==0 and b%i==0):
            d=i
            break
    return d
print(GCD(372,84))
