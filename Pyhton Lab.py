import random
user_choice = input("enter rock,paper or scissors:").lower()
computer_number = random.randint(1,3)
if computer_number == 1:
    computer_choice = "rock"
elif computer_number == 2:
    computer_choice = "paper"
else:
    computer_choice = "scissors"
print(f"computer chose: {computer_choice}")
if user_choice == computer_choice:
    print("it's a tie!")
elif user_choice == "rock" and computer_choice == "scissors":
    print("you win!")
elif user_choice == "paper" and computer_choice == "rock":
    print("you win!")
elif user_choice == "scissors" and computer_choice == "paper":
    print("you win!")
else:
    print("you lose, computer wins!")






    


