#python program to find LCM of two numbers
x=int(input("Enter the First Number:  "))
y=int(input("Enter the Second Number:   "))
if x>y:
    z=a
else:
    z=x
    while(True):
        if((z%x==0) and (z%y==0)):
            lcm=z
            break
        z+=1
print("The LCM of",x,"and",y,"is",lcm)
