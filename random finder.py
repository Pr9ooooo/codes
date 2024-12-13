import random 
a=int(input("Enter a Number from 10-20: "))
b=random.randint(10,20)
playing=True
while playing:
 if a==b:
  print("Correct!")
  break
 else:
  print("wrong choice :(")
  break

  
