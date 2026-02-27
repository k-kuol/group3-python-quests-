go = str(input("Where are you going?(left or right)"))
if go == "left":
    swim = str(input("can you swim?(swim or wait)"))
    if swim == "swim":
        print("You found the treasure!")
    else:
        print("No treasure found!")
else:
    print("You lost!")