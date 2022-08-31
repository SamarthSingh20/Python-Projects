import random
choices = ["Rock", "Paper", "Scissors"]
computer = random.choice(choices)
player = input("Rock,Paper or Scissors? ").capitalize()
if player == computer:
    print("Tie!")
elif player == "Rock":
    if computer == "Paper":
        print("You lose!", computer, "covers", player)
    else:
        print("You win!", player, "smashes", computer)
elif player == "Paper":
    if computer == "Scissors":
        print("You lose!", computer, "cut", player)
    else:
        print("You win!", player, "covers", computer)
elif player == "Scissors":
    if computer == "Rock":
        print("You lose...", computer, "smashes", player)
    else:
        print("You win!", player, "cut", computer)
else:
    print(f"That's not a Correct Move")
