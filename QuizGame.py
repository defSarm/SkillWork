# valorant quiz

points = 0

user = ""
def question(user,question,answer,lower=False):
    global points
    while len(user)==0:
        print(question)
        user = input("> ")
    
    if lower:
        user = user.lower()

    if user == answer:
        points+=1
        print("Correct!")
    else:
        print("Incorrect :(")

question(user,"How many rounds are in standard?","24")
question(user,"What type of agent is Sova?","initiator",True)
question(user,"Who was the first agent of VALORANT lore?", "viper",True)
question(user,"What company created VALORANT?","riot games",True)
question(user,"How many agents are there currently?","22")
question(user,"How much is the VALORANT operator?","4700")
question(user,"How many bullets are in 1 mag of a ghost?","15")

print(f"You got {points}/7")
if points>5:
    print("Thats pretty good!")
else:
    print("Better luck next time :(")
