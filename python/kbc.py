question=["which continent is india in","currency of usa","independence of india was in which year"]
answers=["asia","dollor","1947"]
sum=0
money=[10000,20000,30000]
for i in range(3):
    print(question[i])
    ans=input("enter your answer\n")
    if(ans==answers[i]):
        sum=money[i]
        print("correct answer you win amount ",sum)
    else:
        print("wrong answer")

print("your total winnings are ",sum)

