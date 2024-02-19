import random
mode = None
tries=0

print("What difficulty would you like to play on? (1-3)")
difficulty = input("> ").lower()

if difficulty == "1":
    numberEasy = random.randint(1,10)
    mode=numberEasy
if difficulty == "2":
    numberMedium = random.randint(1,50)
    mode=numberMedium
if difficulty == "3":
    numberHard = random.randint(1,100)
    mode=numberHard

print("Guess the number!")
user=0
while user != str(mode):
    user = input("> ")
    if user > str(mode):
        print("Try lower...")
        tries+=1
    if user < str(mode):
        print("Try higher...")
        tries+=1
    if not(user.isdigit()):
        print("Try to guess a number...")
        continue

print(f"Correct! Tries: {tries}")


