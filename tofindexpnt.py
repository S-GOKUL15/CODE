#python program to find the exponentiation of a given number.
num=int(input("Enter the number: "))
exponent=int(input("Enter the Exponent: "))
Result=num
for i in range(1,exponent):
    Result=num *Result
print(Result)
