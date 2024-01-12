print('''
 \ \ \ \ \ \ \ \ \| |\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \| |\ \ \ \ \ \ \ \ \ 
/ / / / / / / / / | | / / / / / / __  / / / / / / / / | | / / / / / / / / /
 \ \ \ \ \ \ \ \ \| |\ \ \ \ \   /..\  ` ` \ \ \ \ \ \| |\ \ \ \ \ \ \ \ \ 
------------------' `---------- (    ) \|/ -----------' `------------------
 ,------------------------- _\___>  <__//` ------------------------------. 
 |/ / / / / / / / / / / / / >,---.   ,-'  / / / / / / / / / / / / / / / /| 
 | \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ |  . \  \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ | 
 |/ / / / / / / / / / / / / / /  `. `. \   ., / / / / / / / / / / / / / /| 
 | \ \ \ \ \ \ \ \ \ \ \ \ \ \ \  |  `. | \||_ \ \ \ \ \ \ \ \ \ \ \ \ \ | 
 |/ / / / / / / / / / / / / / / / `.  : |__||   / / / / / / / / / / / / /| 
 | \ \ \ \ \ \ \ \ \ \ \ \ \ \ \  __> `.,---'  \ \ \ \ \ \ \ \ \ \ \ \ \ | 
 |/ / / / / / / / / / / / / / /  |.--'\`.\  / / / / / / / / / / / / / / /| 
 `------------------------------ _\\   \`.| -----------------------------' 
------------------. ,------------ /|\ - |:| ----------. ,------------------
 \ \ \ \ \ \ \ \ \| |\ \ \ \ \ \ ' `    |:|  \ \ \ \ \| |\ \ \ \ \ \ \ \ \ 
/ / / / / / / / / | | / / / / / / / / / |:| / / / / / | | / / / / / / / / /
 \ \ \ \ \ \ \ \ \| |\ \ \ \ \ \ \ \ \  |:/  \ \ \ \ \| |\ \ \ \ \ \ \ \ \ 
/ / / / / / / / / | | / /  --.________,-_/  / / / / / | | / / / / / / / / /
 \ \ \ \ \ \ \ \ \| |\ \ \ \ \ ```-----' \ \ \ \ \ \ \| |\ \ \ \ \ \ \ \ \ 
/ / / / / / / / / | | / / / / / / / / / / / / / / / / | | / / / / / / / / /
*******************************************************************************
''')
print("He saw it, and knew it had always been there")
print("And on this morning, Colonel Forbin stepped through the door...") 

direction = input("Passing through the corridor, the path splits. Go L or R?").lower()

if direction == "l":
  decision = input("We see before our eyes a raging river. We can swim it if we try. Swim or Wait?").lower()
  if decision == 'wait':
    door = input("The jester offers three colors of Bathtub Gin. What color, Red, Yellow or Blue?").lower()
    if door == "red":
      print("An asteroid crashed, and YOU burned.\nGame OVER!!!")
    elif door == "yellow":
      print("Congratulations, you have saved Gamehendge from the Evil King Wilson, returned the\nHelping Friendly Book, and married Tela (jewl of Wilson's foul domain)")
    elif door == "blue":
      print("You have been eaten by the MultiBeastTM.\nGame Over")
    else:
      print("Follow the fucking directions asshole - YOU LOSE!")
  else:
    print("Just like Rutheford the Brave, you cant swim in a suit of armor.\nSo you sink and die.\nGAME OVER")
else:
  print("You took the wrong turn and the Evil King Wilson catches you and punches YOU in the eye.\nGAME OVER")



