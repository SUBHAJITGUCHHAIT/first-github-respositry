# Important String

string1=input("Enter a string: ")
v="aeiouAEIOU"
p=""
for i in string1:
    if i in v:
        if i not in p:
            p=p+i+str(string1.count(i))
            string1 = string1.replace(i, "")
print(string1+p)