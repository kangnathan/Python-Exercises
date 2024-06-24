print("TOOTHPICK GAME")

player_one = input("Enter player one's name: ")
player_two = input("Enter player two's name: ")
print(" ")

counter = 13
toothpicks = "| " * counter
print(toothpicks)

print(f"There are {counter} toothpicks left")

while counter != 0:
    move = int(input(f"How many would you like to take {player_one}? \n"))
    
    while move > 3:
        move = int(input("You can only take 1, 2, or 3 \n"))

    counter = counter - move
    toothpicks = "| " * counter
    print(" ")
    print(toothpicks)
    print(f"There are {counter} toothpicks left")
    

    if counter == 0:
        print(f"{player_one} wins!!! \nGAME OVER!!")
        break

    move = int(input(f"How many would you like to take {player_two}? \n"))
    
    while move > 3:
        move = int(input("You can only take 1, 2, or 3 \n"))

    counter = counter - move
    toothpicks = "| " * counter
    print(" ")
    print(toothpicks)
    print(f"There are {counter} toothpicks left")
    

    if counter == 0:
        print(f"{player_two} wins!!! \nGAME OVER!!")
        break
