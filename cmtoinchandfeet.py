#python program to get height in centimeters and then convert the height to feet and inches.
cm=int(input("Enter the height in centimeters:"))
inches=0.394*cm
feet=0.0328*cm
print("The length in inches",round(inches,2))
print('The length in feet',round(feet,2))
