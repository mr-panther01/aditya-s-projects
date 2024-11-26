Name = input("What is your name:")
print("Welcome",Name,"to this adventur game!")

answer = input("You are on a dirt road.It has come to an end and you can you can go left or right.Which way would you like to go? ").lower()

if answer == "left":
    answer = input("You come to a river, you can walk around it or you can swim across.Type walk to walk around or swim to swim across: ")
    if answer == "swim":
        print("You swam across and got eaten by an alligator.")
    elif answer == "walk":
        print("You walked for many miles ran out of water and lost the game. ")
    else:
        print("Not a valid option. You lose.")
elif answer == "right":
    answer = print("You come to a bridge, it looks wobbly, do you want to cross or head back(cross/back): ")
    if answer == "back":
        print("You go back and lose.")
    elif answer == "cross":
        input("You cross the bridge and meet the stranger. Do you want to talk to them(yes/no): ")
        if answer == "yes":
            print("You talk to the stranger and they give you gold. You WIN!")
        elif answer == "no":
            print("You ignore the stranger and they are offended and you lose.")
        else:
            print("Not a valid option you lose.")
else:
    print("Not a valid answer, you lose.")

    print("Thank you for trying", Name)