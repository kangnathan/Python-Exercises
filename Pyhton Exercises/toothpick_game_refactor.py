print("TOOTHPICK GAME")

player_one = input("Enter player one's name: ")
player_two = input("Enter player two's name: ")
current_player = player_one
print(" ")

counter = 13

while True:
    print("| " * counter)
    print(f"There are {counter} toothpicks left")
    move = int(input(f"How many would you like to take {current_player}? \n"))
    print(" ")
    
    while move > 3:
        move = int(input("You can only take 1, 2, or 3 \n"))
        print(" ")

    counter -= move

    if counter <=0:
        print(f"{current_player} wins!!")
        break
    
    if current_player == player_one:
        current_player = player_two
    else:
        current_player = player_one

print("GAME OVER")    
    
    

