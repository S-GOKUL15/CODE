#python program to find the GCD of 2 NOS.
n1=int(input("Enter first number: "))
n2=int(input("Enter Second number: "))
for i in range(1,min(n1,n2)+1):
    if (n1%i==0 and n2%i==0):
        gcd=i
print("GCD of",n1,"and",n2,"is",gcd)
