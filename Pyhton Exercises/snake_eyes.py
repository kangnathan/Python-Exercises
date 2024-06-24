from random import randint
dice_one = randint(1, 6)
dice_two = randint(1, 6)
roll_count = 1

while dice_one != 1 or dice_two != 1:
    print(f"{dice_one} and {dice_two} is not SNAKE EYES")
    dice_one = randint(1, 6)
    dice_two = randint(1, 6)
    roll_count += 1
print(f"{dice_one} and {dice_two}")
print("SNAKE EYES")
print(f"IT TOOK {roll_count} ROLLS")
