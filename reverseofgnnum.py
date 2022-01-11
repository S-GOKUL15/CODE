n=int(input("Enter the Number to be Reversed:   "))
reverse=0
while n!=0:
    reverse=reverse*10+n%10
    n=n//10
print("Reversed Number is:   ",reverse)
