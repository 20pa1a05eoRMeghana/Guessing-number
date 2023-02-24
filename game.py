import random as r
num=r.randrange(100)
Guess=5
while Guess>=0:
  print("Enter your guess")
  your_guess=int(input())
  def check(x):
    if your_guess==x:
      print("You Win")
      break
    elif your_guess>x:
      print("You are close, keep trying lower")
    else:
      print("you are close, keep trying higher")
  if Guess>1:
    check(num)
  elif Guess==1:
    check(num)
    print("This is your last chance")
  else:
    print("You Loose")
  Guess=Guess-1
