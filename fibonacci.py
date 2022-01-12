first,second=0,1
n=int(input("How many Steps do you want to Exucute"))
print("Fibonacci Series")
for i in range(0,n):
    if i<=1:
        result=i
    else:
        result=first+second
        first=second
        second=result
    print(result)
