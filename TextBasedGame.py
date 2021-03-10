# Adam Ebersole IT-140 Final Project Text Based Game

# import section
import time

# the dictionary links a room to other rooms.
rooms = {
    'Starboard Nacelle': {'West': 'Mess Hall',
                          'item': 'Helmet',
                          'flavor': 'A blue glow from the warp cell fills this room. \nThe lights flicker '
                                    'as sparks pop and jump from nearby panels. \nThe engine hums as the'
                                    ' Defiance races towards enemy lines. \nYou see an exit to the West.'},
    'Mess Hall': {'South': 'Central Promenade',
                  'East': 'Starboard Nacelle',
                  'item': 'Chest Plate',
                  'flavor': 'It seems the fierce battle that started on the Promenade spilled into the mess hall.\n'
                            'Food trays and their contents lie scattered amongst the bodies of the fallen.\n'
                            'You can see exits to the South and East.'},
    'Central Promenade': {'South': 'Passenger Lounge',
                          'North': 'Mess Hall',
                          'East': 'Barracks',
                          'West': 'Bridge',
                          'flavor': 'A grizzly scene of battle lay all around you. \nThe beauty of the '
                                    'Promenade has been shattered by blaster fire and explosions.'
                                    '\nSmoke still hangs thick in the air. \nYou see exits to the '
                                    'North, South, and East. \nYou will need a Key Card to access the Bridge '
                                    'to the West.\n'},
    'Bridge': {'East': 'Central Promenade',
               'flavor': 'If you see this, something broke. Please Restart'},  # villain room
    'Barracks': {'West': 'Central Promenade',
                 'North': 'Captain\'s Quarters',
                 'item': 'Blaster Pistol',
                 'flavor': 'The lights flicker and dim, casting eerie shadows across the walls. \n'
                           'Clothes and bedding lie scattered across the floor. \nHolo-zines and personal items'
                           ' from the crew tossed in their rush to defend the ship. \nYou see exits to the'
                           ' North and West'},
    'Captain\'s Quarters': {'South': 'Barracks',
                            'item': 'Key Card',
                            'flavor': 'The Captain\'s Quarters remain largely untouched. \nThe Captain\'s coffee'
                                      ', still hot, is sitting on his desk where he left it. \n'
                                      'A chair, toppled in his rush out of the room, lies on the floor. \nYou see'
                                      ' an exit to the South.'},
    'Passenger Lounge': {'North': 'Central Promenade',
                         'East': 'Port Nacelle',
                         'item': 'pair of Pants',
                         'flavor': 'The first thing that hits you is the smell. \nAt some point during the battle'
                                   ' the passenger lounge caught fire. \nThe fire suppression system did it\'s'
                                   ' job, but not before the fire had it\'s way with the Aliens that fell here.'
                                   '\nCharred remains mingle with the burnt out furniture. \nYou see exits to'
                                   ' the North and East.'},
    'Port Nacelle': {'West': 'Passenger Lounge',
                     'item': 'pair of Boots',
                     'flavor': 'The blue glow of the warp cells that usually light this area is gone. \nThe warp'
                               ' coils are shattered and dark. \nYou see only glimpses of the room in the flickering'
                               ' light. \nThe Defiant is limping along on one engine,'
                               ' you still have time. \nYou see an exit to the West.'}
}

# list for valid directions check
directions = ['North', 'South', 'East', 'West']


# Welcome and introduction
def welcome():
    print('\nYou wake up in the Central Promenade of the ISS Defiance. \nThe Battle that knocked you unconscious'
          ' was fierce and it\'s remnants are displayed around the room. \nAliens have attacked the'
          ' ship and one has taken control of the Bridge. \nYou are the last one left that can save the Defiance. '
          '\nYou need to gather five items from around the ship as well as the Captain\'s Key Card. \nGain'
          ' access to the Bridge to defeat the Alien and save the ship. Good luck Solider.')
    time.sleep(2)


# help file
def game_help():
    print('\nYou can type \'North\', \'South\', \'East\', and \'West\' to navigate.\n' 
          'Type \'Inventory\' to display your inventory.\n'
          'Type \'Get Item\' to pick up an item.\n'
          'Type \'Exit\' to quit.\n'
          'Type \'Help\' to repeat these instructions.\n'
          'Remember: Instructions are case sensitive!')
    time.sleep(1)


# function to print current room name
def get_key(val):
    for key, value in rooms.items():
        if val == value:
            return key


# function to unlock the bridge with the key card item
def key_card():
    if 'Key Card' not in inventory:
        print('\nYou need the Key Card to enter the Bridge!')
        time.sleep(.5)
    else:
        bridge_choice = input('\nWould you like to use the Key Card and face the alien? Yes/No \n> ')
        if bridge_choice == 'Yes':
            print('You have unlocked the bridge.\n')
            time.sleep(.5)
            return True
        else:
            print('You put the Key Card away.')


# function for final battle and w/l condition
def alien_battle():
    if len(inventory) == 6:
        print('Your armor absorbs the alien\'s toxic radiation.\n'
              'You fire your blaster before the alien notices you.\n'
              'The Alien bellows in pain and shock as your blaster bolt begins to de-atomize him.\n'
              'His scream fades as you watch him slowly disintegrate.\n'
              'Justice has been done.\n'
              'You have gained control of the Defiance, Congratulations Solider!')
        quit()
    else:
        print('Without the proper armor and weapons the Alien\'s toxic radiation melts the flesh from your bones! \n'
              'You have died, better luck next time!')
        quit()


# player inventory
inventory = []

# sets the current room
current_room = rooms['Central Promenade']

# game introductions and game start check loop
welcome()
while True:
    game_begin = input('\nWould you like to start the game? Type Yes/No \n> ')
    if game_begin == 'Yes':
        # prints directions to the console and begins the game
        game_help()
        time.sleep(1)
        break
    elif game_begin == 'No':
        print('\nSee You, Space Cowboy.')
        quit()
    else:
        print('\nInvalid entry, please try again.')
        time.sleep(.75)

# game loop
while True:
    # prints your current location, item reveal, and flavor text
    print('\nYou are in the {}.\n'.format(get_key(current_room)))
    time.sleep(.5)
    print(current_room['flavor'])
    time.sleep(.5)
    if 'item' in current_room:
        print('You see a {}.\n'.format(current_room['item']))
    time.sleep(.5)
    # user input section
    user_input = input('What would you like to do? \n> ')
    # section for key card check to keep bridge locked until player gets item
    if get_key(current_room) == 'Central Promenade' and user_input == 'West':
        if key_card() is True:
            print('You step onto the Bridge to face the Alien!\n')
            time.sleep(.5)
            alien_battle()
        else:
            current_room = rooms['Central Promenade']
            print('\nYou are in the {}.'.format(get_key(current_room)))
            time.sleep(.5)
            user_input = input('What would you like to do? \n> ')
    # compares input with dictionary for movement
    if user_input in directions:
        if user_input in current_room:
            current_room = rooms[current_room[user_input]]
        # for direction with no value
        else:
            print('\nThere is nothing in that direction.')
            time.sleep(.75)
    # item acquisition section
    elif user_input == 'Get Item':
        if 'item' in current_room:
            print('You get the {}'.format(current_room['item']))
            inventory.append(current_room['item'])
            current_room.pop('item')
        else:
            print('\nThere is nothing here to get.')
            time.sleep(.75)
    # displays player inventory
    elif user_input == 'Inventory':
        print('\nYou are currently carrying: \n{}'.format(inventory))
    # prints the help file in case user gets stuck
    elif user_input == 'Help':
        game_help()
    # allows the user to quit the game
    elif user_input == 'Exit':
        print('\nThanks for playing! Come back soon!')
        quit()
    # for bad input
    else:
        print('\nInvalid entry please try again.')
        time.sleep(.75)
