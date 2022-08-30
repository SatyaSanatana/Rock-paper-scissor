#game_images[rock,paper,scissors]
user_choice=(int(input("type a number if rock type 0, if paper type 1, if scissors type 2 :")))
print(f"your choice is:{user_choice}")

import random as r


computer_choice=r.randint(0,2)
print(f"computer choice is: {computer_choice}")
if user_choice>=3 or user_choice<0:
    print("you typed an invalid number...sorry, you lose!!!")
elif user_choice>computer_choice:
    print("you win !!!!!")
elif computer_choice>user_choice:
    print("you lose!!!!!")
elif computer_choice==0 and user_choice==2:
    print("you lose!!!!")
elif computer_choice==2 and user_choice==0:
    print("you win!!!!")
else:
    print("draw")
        
    