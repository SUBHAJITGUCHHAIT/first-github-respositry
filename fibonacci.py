lis=input()
n=int(input())
lis1=list(map(int,lis.split()))
print(lis1)
k=len(lis1)
for value in lis1:
    if n == value:
        print(n,"is found in list")
        break
else:
    print(n,"n is not found")
