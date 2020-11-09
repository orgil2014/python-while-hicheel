n=int(input("n: "))
m=int(input("m: "))
count=0
while m>n:
    if n%2==0 and n%3==0:
        count+=1
    n+=1
print("count:  ", count)