n=int(input("no. of elements in the lists:"))
a=[]
b=[]

for i in range(n):
    c=int(input(f"Enter element a{i}:"))
    a.append(c)
    i+=1
for i in range(n):
    d=int(input(f"Enter element b{i}:"))
    b.append(d)
    i+=1
i=0
sum=0
for i in range(n):
    sum+=a[i]*b[i]
    i+=1
print(f"dot product of above two lists:{sum}")