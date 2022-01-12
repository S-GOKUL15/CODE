fname=input("enter file name")
num_words=0
with open(fname,'r')as f:
        for line in f:
            words=line.split()
            num_words+=len(words)
print("the word count is")
print(num_words)
