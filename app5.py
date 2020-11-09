n=int(input("n: "))
niilber=0
while n>0:
    print(n%10)
    niilber+=n%10
    n=n//10
print(niilber)