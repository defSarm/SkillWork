from random import choice
playing = True

options = ["rock","paper","scissors"]

user = ""

def condition(opt1, opt2):
    global user, bot, playing
    if user == opt1 and bot == opt2:
        print("You Lose!")
        print(f"You:{user} | Bot:{bot}" )
    if user == opt2 and bot == opt1:
        print("You Win!")
        print(f"You:{user} | Bot:{bot}" )

while playing:
    print("Rock, Paper, or Scissors?")
    user = input("> ").lower()
    bot = choice(options)

    if user == bot:
        print("Tie!")
        print(f"You:{user} | Bot:{bot}" )

    condition("rock","paper")
    condition("scissors","rock")
    condition("paper","scissors")

    again = input("Play again? (y/n): ").lower()
    if again == "y":
        playing=True
    if again == "n":
        playing=False
