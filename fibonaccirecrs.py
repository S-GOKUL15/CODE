first=0
second=1
n=int(input("How many steps did you want to execute?"))
def  fibonacci(num):
    if num==0:
        return 0
    elif num==1:
        return 1
    else:
        return fibonacci(num-1)+fibonacci(num-2)
print("Fibonacci Series are")
for i in range(0,n):
    print(fibonacci(i))
