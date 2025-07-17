import os
curr_dir=os.getcwd()
# print(curr_dir)
change_dir=os.chdir("D:/python/directory")
dir=os.getcwd()
print(dir)
list_dir=os.listdir(dir)
print(list_dir)
i=1
j=1
t=1

for words in list_dir:
    if(words[-3:]=="png"):
        os.rename(words,f"{i}.png")
        i+=1
    elif(words[-3:]=="pdf"):
        os.rename(words,f"pdf{j}.pdf")
        j+=1
    elif(words[-3:]=="txt"):
        os.rename(words,f"notepad{t}.txt")
        t+=1
# list_dir2=os.listdir(dir)
# print(list_dir2)

