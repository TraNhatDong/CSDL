def Fibonacci_dequy(n):
    assert n >= 0 and int(n) == n
    if n==0 :
        return 0
    elif n==1 or n==2:
        return 1
    else:
        return Fibonacci_dequy(n-1)+ Fibonacci_dequy(n-2)

print(Fibonacci_dequy(5))
def Fibonacci(n):
    assert n >= 0 and int(n) == n
    a=0
    b=1
    while n>=2:
       c=a+b
       a=b
       b=c
       n-=1
    return c
print(Fibonacci(5))
