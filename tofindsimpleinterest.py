#python program to find simple interest
principle=float(input("Enter the Priniciple Amount:"))
time=int(input("Enter the time(years):"))
rate=float(input("Enter the rate:"))
simple_interest=(principle*time*rate)/100
print("The Simple Interest is:",simple_interest)
