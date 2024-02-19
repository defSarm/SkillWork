# password manager 
from time import sleep


leave = False


while not(leave):
    print("""
    [Welcome to YOUR password manager]
      
      > View existing password(s)
         - use VIEW
      > Add a new password
         - use ADD
      > Leave password manager
         - use LEAVE
    """)

    mode = input("> ").lower()
    if mode == "view":
        with open("passwords.txt","r") as f:
            print(f.read()+"\n")
        
        print("q to go back ")
        close = input("> ")
        while close!="q":
            close = input("> ")
            if close == "q":
                break
    
    if mode == "add":
        name = input("Name: ")
        passwrd = input("Password: ")

        with open("passwords.txt","a") as f:
            f.write(f"{name} | {passwrd}"+"\n")


        print(f"ADDED - {name} | {'*'*len(passwrd)}")
        sleep(3)

    if mode == "leave":
        leave = True