import random
print("welcome To Snake Water Gun Game")
print("RULES:\n snake beats water\n water beats gun \n gun beats snake")
print("press\n 1 for snake \n 2 for water \n 3 for gun ")
choice=int(input("enter your choice "))
if(choice==1):print("you chose snake")
elif(choice==2):print("you chose water")
elif(choice==3):print("you chose gun")
else:
    raise ValueError("invalid choice")

bot=[1,2,3]
choicebot=random.choice(bot)
if(choicebot==1):print("computer chose snake")
elif(choicebot==2):print("computer chose water")
else:print("computer chose gun")

if((choice==1 and choicebot==2)or(choice==3 and choicebot==1)or(choice==2 and choicebot==3) ):
    print("Congratulations you won")
elif(choice==choicebot):
    print("DRAW")
else:
    print("YOU LOSE")


# 1>2
# 3>1
# 2>3
