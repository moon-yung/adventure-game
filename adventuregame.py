import random 

def introduction(name): 
        name = input("\nEnter your name: ").upper()
        about(name)

def about(name):
    print()
    print(f"\nHello {name}, Welcome to the world of Alchemy!")
    print(f"You are the long lost mage who is destined to own the sky stone")
    print(f"This is your chance to discover your skills.")
    print(f"{name}, Your journey will begin today!")
    print(f"So get ready and...........")
    print("\n----W E L C O M E  T O  A D V E N T U R E  G A M E----\n")
    menu(name)

def menu(name):
    while True:
        print("""
                --- MENU ---

                'W'  - West
                'E'  - East
                'Q'  - Quit Game
                                """)

        choice = input("Select Option: ").upper()
        if choice == 'W':
            west(name)
            break
        if choice == 'E':
            east(name)
            break
        if choice == 'Q':
            print("Exiting Game......")
            break
        else:
            print("Invalid Input")
            continue

def west(name):
    print()
    print("You are in the West")
    print("This is the beginning of your journey")
    print("A wild animal wants to eat you")
    
    while True:
        print()
        option1 = input("Do you want to attack? Y/N: ").upper()
        if option1 == 'Y':
            print()
            print("You still lack skills")
            print("You sustained multiple wounds that caused your death")
            gameOver(name, "You got killed by an animal attack")
            break
        
        elif option1 == 'N':
            print()
            print("You hid in the bushes and prevented death")
            print("You found out this place is unsafe.")
            print("You will go back to the main menu")
            menu(name)
            break     
        else:
            print("Enter only Y/N")
            continue

def skyStone(name):
    ent = input("\nPress enter to start >>> ")
    print(f"\nWelcome {name} on the Sky Stone Training")   
    print("The monster had soul shifted to a person")
    print("You need to find that person and defeat him/her to be able to finish the Sky Stone Training.")
    print("You need to randomly choose from these people to find out who the real monster is")
    monster = (
                "0 :  Eunich", 
                "1 :  Maidservant", 
                "2 :  Male Store owner")
    print()
    print(monster)
    a=random.choice(monster)
    input("\nPress Enter to start >>> ")
    print(f"\nYou picked a random choice > {a}")
       
    if a == monster[0]:
        print("\nYou guessed it right!")
        print("You now have the power of the Sky Stone")
        print("Congratulations! You Won the Game!")
        end(name)
    else:
        print("\nThe soul shifter is the Eunich")
        gameOver(name, "You failed to catch the soul shifter and it killed you.")
       

           
def east(name):
    print()
    print(f"{name}, You are in the East")
    print("This is the place to upgrade your mage skills.")
    print("Naksu will train you to become the best mage in the world of Alchemy.")
    print("You now have developed 'Tansu' in this training")
    
    while True:
        print("\nChecking your 'Tansu' power level.......")
        a = random.randrange(6,11)
        print(f"Tansu power level: {a}\n")
        

        if a < 10:
            print()
            input("You need more practice. Try Again >>> ")
            continue
        else:
            print()
            print(f"Perfect! You have reached Tansu level of {a}")
            print("\nGet ready for the next level")
            break
        
    skyStone(name)
        
                
def gameOver(name, reason):
    print(f"\nYou lost the game {name}.")    
    print(f"Reason: {reason}")   
    
    while True:
        option1 = input("\nDo you want to try a new game (Y/N)? >>>  ").upper()
        if option1 == 'Y':
            menu(name)
            break
        
        elif option1 == 'N':
            end(name)
            break     
        else:
            print("Enter only Y/N")
            continue

def end(name):
    print("Exiting game......")

     

    
    
introduction(name = input)









        





    






    

