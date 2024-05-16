def cheakgcd (a,b):
    for i in range(1,min(a,b)+1):
        if i%a==0 and i%b==0:
            gcd=i
a=int(input())
b=int(input())
print(cheakgcd(a,b))
