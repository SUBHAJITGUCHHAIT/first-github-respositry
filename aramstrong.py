num1=int(input("Enter a number "))
num=num1
digits=len(str(num1))
arm=0
while num1>0:
    arm=arm+((num1%10)**digits)
    num1=num1//10
if num==arm:
    print("It is Armstrong Number")
else:
    print("It is not Armstrong Number")



