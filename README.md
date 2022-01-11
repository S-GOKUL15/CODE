# CODE
#PYTHON PROGRAM TO REVERSE A GIVEN NUMBER
g=int(input("Enter the Number to be Reversed"))
reverse=0
while g!=0:
  reverse=reverse*10+g%10
  g=g//10
print("After Reversing: ",reverse)
