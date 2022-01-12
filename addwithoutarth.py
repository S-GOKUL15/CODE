a=int(input("Enter the Value for a:"))
b=int(input("Enter the Value for b:"))
def add(a,b):
    while b!=0:
        c=a&b
        a=a^b
        b=c<<1
    return a
print(add(a,b))

