print("BEERS ON THE WALL")

beer = 100

while beer >= 2:
    if beer:
        print(f"{beer} bottles of beer on the wall")
        print(f"{beer} bottles of beer")
        print(f"Take down one, pass it around, {beer - 1} bottles of beer on the wall")
        beer -= 1
        if beer < 2:
            print("1 bottle of beer on the wall")
            print("1 bottle of beer")
            print("Take down one, pass it around, no more bottles of beer on the wall")
    else:
        print("More Beers")
