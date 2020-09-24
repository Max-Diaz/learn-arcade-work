import random

# Introduction
print("Welcome to Fallout!")
print("You have stolen a Brahimm to make your way across the Mojave Desert to reach the nearest NCR Post in New Vegas.")
print("The Raiders want their Brahimm back and are chasing you down! Survive Courier 66.")
print("Survive this endeavour and out run the raiders.")
print("There's alot of good buyers in New Vegas waiting to buy that prized Brahimm, Good luck.")
print()

# initiate variables
done = False
milesTraveled = 0
raidersTraveled = -20
brahimmTiredness = 0
heals = 0
stimpack = 3
post = -1
# Game loop
while not done:

    # options
    print("A. Get a heal from a Stimpack.")
    print("B. Ahead moderate speed.")
    print("C. Ahead full speed.")
    print("D. Stop for the night and set up camp.")
    print("E. Check your Pip-boy for status.")
    print("Q. Quit.")
    print()

    # Take user's input
    userInput = input("What will you do? ")

    # Check if they want to quit
    if userInput.upper() == "Q":
        done = True
    # Pip-Boy Status update
    elif userInput.upper() == "E":
        print("Miles traveled:", milesTraveled)
        print("Heals left in your stimpack:", stimpack)
        print("The raiders are", milesTraveled - raidersTraveled, "miles behind you.")
        print()
    # stop for the night
    elif userInput.upper() == "D":
        print("You stop for the night and set up camp.")
        print("Your Brahimm has rested and is ready for what the day brings.")
        print("The raiders don't stop.")
        print()
        brahimmTiredness = 0
        raidersTraveled += random.randrange(7, 15)
    # full speed ahead
    elif userInput.upper() == "C":
        miles = random.randrange(10, 21)
        milesTraveled += miles
        heals += 1
        brahimmTiredness += random.randrange(1, 4)
        raidersTraveled += random.randrange(7, 15)
        post = random.randrange(20)
        if post == 10:
            heals = 0
            brahimmTiredness = 0
            stimpack = 3
            print("As you travel you happen to encounter a general store post in the middle of the desert!")
            print("You bought 3 more Stimpacks and you ate some delicious Deathclaw Meat to, and")
            print("Your Brahimm has rested and gain full strength!")
            print("The raiders continue the chase.")
            print()
        else:
            print("You push onward at full speed, moving a total of", miles, "miles")
            print("Your desire for a heal increases.")
            print("The raiders continue the chase.")
            print()
    # mid-speed ahead
    elif userInput.upper() == "B":
        miles = random.randrange(5, 13)
        milesTraveled += miles
        heals += 1
        brahimmTiredness += 1
        raidersTraveled += random.randrange(7, 15)
        post = random.randrange(20)
        if post == 10:
            heals = 0
            brahimmTiredness = 0
            canteen = 3
            print("Alas you happen to found a small general store outpost in the middle of the Mojave!")
            print("After a hard bargain, you are able to buy 3 more stimpack and enjoy some Deathclaw meat, and")
            print("Your Brahimm is rested!")
            print("The raiders continue the chase.")
            print()
        else:
            print("You move forward, moving a total of", miles, "miles")
            print("Your desire for a heal increases.")
            print("The raiders continue the chase.")
            print()
    # Drink from canteen
    elif userInput.upper() == "A":
        if stimpack > 0:
            stimpack -= 1
            heals = 0
            print("You take a Stimpack")
        else:
            print("You have run out Stimpacks. And you are unable to heal from now, watch out for Radioscorpions.")

    # Status updates
    # Thirst
    if heals > 5:
        print("You have been stunged by Radioscorpion and was unable to heal!")
        print("You have succumb to Radioscorpion's venom.")
        print("Your body was never found.")
        print("Game Over.")
        print()
        done = True
    elif heals > 4:
        print("You need another heal to gain strength!")
    # Distance traveled / win check
    if milesTraveled >= 200:
        print("Congratulations! You have arrived at the New California Republic's outpost in New Vegas.")
        print("Raiders return back to their hideout due to the NCR's presence.")
        print("You were able to sell that prized Brahimm to the highest bidder.")
        print("Mr.House bought your Brahimm for 40,000 caps at the auction.")
        print("You win!")
        print()
        done = True
    # Camel's tiredness
    if brahimmTiredness > 8:
        print("Your Brahimm died of exhaustion!")
        print("With no means of transportation, the raiders catch up to you and crucify you")
        print("on the spot.")
        print("Your death serves as warning to any adventurer not to steal from raider clans.")
        print("Game Over.")
        print()
        done = True
    elif brahimmTiredness > 5:
        print("Your Brahimm is tired.")
        print()
    # Natives distance from you
    if milesTraveled - raidersTraveled <= 0:
        print("The raiders have caught up with you!")
        print("They kill you with laser pistol on the spot, and take back their prized Brahimm.")
        print("Game Over.")
        print()
        done = True
    elif milesTraveled - raidersTraveled < 15:
        print("You see faint shapes on the horizon behind you and hear the thunderous noise from their war drums!")
        print("The raiders are getting close!")
        print()

# Exit message
print("Exiting Game. Goodbye.")