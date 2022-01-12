n=int(input("Enter the Number:"))
reverse,temp=0,n
while temp!=0:
    reverse=reverse*10+temp%10
    temp=temp//10
if reverse==n:
    print("Palindrome")
else:
    print("Not Palindrome")
