#python program to count the number of Vowels.
string=input("Enter a String: ")
count=0
for i in string:
    if i in 'aeiouAEIOU':
        count+=1
print("The Number of Vowels in",string,"is:  ",count)
