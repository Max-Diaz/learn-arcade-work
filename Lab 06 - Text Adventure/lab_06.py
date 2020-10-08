
  
"""
This is a text adventure game that takes you around a vault in the Fallout Universe
"""
# Vault Room descriptions
room_list = []
room = ["This area where you begin is the known as the entrance of the Vault 101. You see two doors: "
        "\none to your left and the other down the room. Enjoy the Tour!", None, None, 5, 1]
room_list.append(room)
room = ["You are in the main hallway of the Vault 101"
        "\nThis is where majority of the traffic happens day to day in the vault.", None, 0, 4, 2]
room_list.append(room)
room = ["You are in Science Department brought to you by Vault-tec"
        "\nIn this place is where our scientist find create innovated ways to survive in the Nuclear Wasteland."
        "\nYou see two doors, one on the south and the other one in the west.", None, 1, 3, None]
room_list.append(room)
room = ["You are in Sleeping Quarters, the comfiest place in this Vault-tec facility. "
        "\nThis place can house up to 100 vault dweller in the most modern yet comfortable living space."
        "\nYou see two doors, one on the south and the other one in the west.", 2, 4, 6, None]
room_list.append(room)
room = ["You are in the Workshop area in Vault-tec."
        "\nThis is where the explorers bring their items from wasteland for. "
        "\nOur thinkers are able to convert these items into something of use like Pipe guns, traps, body armor, etc. "
        "You see four different doors around you.", 1, 5, 7, 3]
room_list.append(room)
room = ["You are in the Power and water purification station  "
        "\nWithout this room, our vault would have died a long time ago. It's a maximum priority to maintain it. "
        "\nYou see two doors; one will take you to the entrance of the vault and the other to different place. ",
        0, None, None, 4]
room_list.append(room)
room = ["Your are in the Medical Bay. "
        "\n Any recent injury, have a bad stomach, or you're curious about your health overall."
        "\nDr.Craven is willing to take a look at anyone for the price of few caps.", 3, 7, None, None]
room_list.append(room)
room = ["You in the Greenhouse sponsored by Vault-tec "
        "\nThis is where we are able to grow food in a controlled environment since the land outside is glassed."
        "\nWe grow Corn,Squash,Tomatoes,Beans,Chile, and many more plants. ", 4, 8, None, 6]
room_list.append(room)
room = ["You are in the Dinning Hall "
        "\nThis is where our vault dwellers come and eat every breakfast, lunch, and dinner."
        "\nThat concludes our tour of our beautiful Vault."
        "\nSee you again soon! ", None, 9, None, 7]
room_list.append(room)
room = ["Thank you for coming to our tour and please on the way out stop by the gift shop."
        "\nPlease enter the command 'Quit' to take your VR headset off.", None, None, None, None]
room_list.append(room)

current_room = 0
# Instructions
print('Welcome traveler to our special tour of Vault 101')
print('Enter one of the following commands and enjoy the tour:')
print("- North")
print("- South")
print("- West")
print("- East")
print("- Quit")

done = False
while not done:
    print()
    print(room_list[current_room][0])
    user_input = input("Where do you want to go now?: ")

    if user_input.upper() == "Quit" or user_input.upper() == "Q":
        done = True

    elif user_input.upper() == "North" or user_input.upper() == "N":
        next_room = room_list[current_room][1]
        if next_room is None:
            print("You can't go that way!")
        if next_room is not None:
            current_room = next_room

    elif user_input.upper() == "East" or user_input.upper() == "E":
        next_room = room_list[current_room][2]
        if next_room is None:
            print("You can't go that way!")
        if next_room is not None:
            current_room = next_room

    elif user_input.upper() == "South" or user_input.upper() == "S":
        next_room = room_list[current_room][3]
        if next_room is None:
            print("You can't go that way!")
        if next_room is not None:
            current_room = next_room

    elif user_input.upper() == "West" or user_input.upper() == "W":
        next_room = room_list[current_room][4]
        if next_room is None:
            print("You can't go that way!")
        if next_room is not None:
            current_room = next_room

    else:
        print("Wrong command, please try again.")
