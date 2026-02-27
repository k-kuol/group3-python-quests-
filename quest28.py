def start():
    print("You stand at a crossroads.")
    choice = input("Go left or right? ")
    if choice == "left":
        forest()
    elif choice == "right":
        cave()
    else:
        print("Invalid choice!")

def forest():
    print("You enter a dark forest and find treasure!")
    print("YOU WIN!")

def cave():
    print("You enter a cave and encounter a dragon!")
    choice = input("Fight or flee? ")
    if choice == "fight":
        print("The dragon defeats you. GAME OVER!")
    elif choice == "flee":
        print("You escape safely. YOU WIN!")
    else:
        print("Invalid choice!")

start() 
