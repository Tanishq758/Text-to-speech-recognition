import time
inputTime=time.strftime('%H:%M:%S')

print(inputTime)
if(inputTime<'12:00:00'):
    print("Good Morning")
elif(inputTime>='12:00:00' and inputTime<'16:00:00'):
    print("Good Evening")
else:
    print("Good Night")

for i in range(10, 0, -1):
  print(i)