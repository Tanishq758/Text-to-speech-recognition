import random
import string

# word=''.join(random.choices(string.ascii_lowercase,k=3))
print("Enter 1 to encrypt\n press 0 to decrpyt")
choice=int(input("Enter your choice"))
if(choice==1):
    nwords=[]
    text=input("enter your message :\n")
    words=text.split(" ")
    for word in words:
        if(len(word)>=3):
            newword=''.join(random.choices(string.ascii_lowercase,k=3))+word[1:]+word[0]+''.join(random.choices(string.ascii_lowercase,k=3))
            nwords.append(newword)
        else:
            nwords.append(word[::-1])
    print(' '.join(nwords))
else:
    nwords=[]
    text=input("Enter tour message")
    words=text.split(' ')
    for word in words:
        if(len(word)>=3):
            newword=word[3:-3]
            original=newword[-1]+newword[0:-1]
            nwords.append(original)
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))


