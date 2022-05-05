import random

my_choice=input("Choose 'r' for rock, 'p' for paper, 's' for scissor : ")
computer_choice=random.choice(["r","p","s"])
print("computer_choice", computer_choice)

def play(): 
    if my_choice==computer_choice:
        return "Tie!"
    elif(invalid_user_choice()):
        return "Enter either r or p or s"
    elif(is_win()):
        return "U Won!"
    return "U Lost!"

def is_win():
    if((my_choice=="r" and computer_choice=="p") or (my_choice=="p" and computer_choice=="s")
        or (my_choice=="s" and computer_choice=="r")):
        return True

def invalid_user_choice():
    if(my_choice=="r" or my_choice=="p" or my_choice=="s"):
        return False
    return True

print(play())