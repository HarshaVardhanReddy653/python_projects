import random
while True:
choice=input('Roll the Dice (yes/No)')
if choice=="yes":
  die1=random.randint(1,6)
  die2=random.randint(1,6)
  print(f'{die1},{die2}')
elif choice=="No":
  print(f'Thank u for playing')
  break
else:
  print('innvalid choce!')
