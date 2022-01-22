name=input("Enter your name:   ")
letter=name.split()
letter.reverse()
print("Reversed Name:",end=' ')
for i in letter:
    print(i,end=' ')
