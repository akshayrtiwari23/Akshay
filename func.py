
def fact(n):
    f=1
    for i in range(1,1+n):
        f=f*i
    return f

def armstrong(n):
    sum=0
    a=0
    temp=n
    while temp>0:
        a = temp % 10
        sum=sum+a*a*a
        temp=temp//10
    if n== sum:
        print(n,"armstrong")
    else:
        print(n,"not an Armstrong")
        


def palindrome(x):
    rev=0
    temp=x
    while x>0:
        r=x%10
        x=int(x/10)
        rev=rev*10+r
    if rev==temp:
       print(temp,"is palindrome")
    else:
       print(temp,"is not palindrome")

def pow(n,m):
    return n**m

