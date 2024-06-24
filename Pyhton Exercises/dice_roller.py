from random import randint

dice_num = int(input("How many dice are we rolling: "))
dice_sides = int(input("How many sides on each dice: "))
dice = randint(1, dice_num)

while True:
