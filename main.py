
class Place:
    def __init__(self, name, description, items=None, enemies=None, locked=False, key=None):
        self.name = name
        self.description = description
        self.items = items if items else []
        self.enemies = enemies if enemies else []
        self.locked = locked
        self.key = key
        self.connections = {}
        self.has_visited = False

    def connect(self, place, direction):
        self.connections[direction] = place

    #creating a dictionary, where the key is the direstion, and the value is the place

    def describe(self):
        print(f"You are now in {self.name}.\n{self.description}")
        if self.items:
            print(f"The items here are: {', '.join(self.items)}")
        if self.enemies:
            print(f"The enemies here are: {', '.join(self.enemies)}")
        print(f"You can exit from: {', '.join(self.connections.keys())}")
      #  if self.locked:
       #     print("This place is locked and requires a specific item to enter.")

        

class Meadow(Place):
    
    def describe(self,player):
        print(f"You are now in {self.name}")
        print("You stumble upon some magical berries!")
        pickup = input("Press 'enter' to pick up the magical berries")
        if not pickup:
            player.pick_up('magical berries')
        answer = input("""The talking rabbit has come to tell you something: 'Eat all the food you can get. This will increase your strength and energy'.
                        Would you like to eat all or some of the magical berries? Choose wisely! all/some?   """)
        if answer.lower() == 'all':
            player.energy +=50
            player.strength +=40
            print("Great! Your strength and energy has increased")
            player.remove_item('magical berries')

        elif answer.lower()== 'some':
            player.strength += 20
            player.strength += 30
            print("Great! Your strength and energy has increased, and you still have some food for later!")


class Market(Place):
    def describe(self, player):
        if not self.has_visited:
            print(f"You are now in {self.name}")
            if 'magical berries' in player.rucksack:
                reply = input("""You need Gold.
                               Sell your leftover magical berries in the market!
                               Press 'enter' to do so""")
                if not reply:
                    player.rucksack.remove('magical berries')
                    player.gold += 20

                opt = input("""You can now buy something, but only one item will be of use.Choose Wisely!
                             Either: 1) New Shoes - 10 gold coins  2) Lantern - 10 gold coins  3)  Bucket - 15 gold coins.
                             (Hint: The next location is very dark!)""")
                if opt == '1':
                    if (player.gold-10)>0:
                        player.pick_up('new shoes')
                        print("You have bought new shoes!. They have been added to your rucksack")
                        player.gold -= 10
                        print(f"You have {player.gold} gold coins remaining")
                    else:
                        print(f"You only have {player.gold} gold coins!")
                elif opt == '2':
                    if (player.gold-10)>0:
                        player.pick_up('lantern')
                        print("You have bought a lantern!. It has been added to your rucksack")
                        player.gold -= 10
                        print(f"You have {player.gold} gold coins remaining")
                    else:
                         print(f"You only have {player.gold} gold coins!")
                elif opt == '3':
                    if (player.gold-15)<0:
                        player.pick_up('bucket')
                        print("You have bought a bucket!. It has been added to your rucksack")
                        player.gold -= 15
                        print(f"You have {player.gold} gold coins remaining")
                    else:
                        print(f"You only have {player.gold} golden coins")
            else:
                direction = input(""" You need Gold to buy your next item. But you should not have listened to the talking rabbit!
                      Now you have nothing to sell. You can return to the meadow to collect more fruits and nuts. Be wiser next time!
                    Which direction would you like to move in? """)
                player.move(direction)
            self.has_visited=True
        else:
            print('Welcome back')
            choice = input("""You can now buy something, but only one item will be of use.Choose Wisely!
                             Either: 1) New Shoes - 10 gold coins  2) Lantern - 25 gold coins  3)  Bucket.
                             (Hint: The next location is very dark!)""")
            if choice == '1':
                if (player.gold-10)>0:
                    player.pick_up('new shoes')
                    print("You have bought new shoes!. They have been added to your rucksack")
                    player.gold -= 10
                    print(f"You have {playr.gold} gold coins remaining")
                else:
                    print(f"You only have {player.gold} gold coins!")
            elif choice == '2':
                if (player.gold-10)>0:
                    player.pick_up('lantern')
                    print("You have bought a lantern!. It has been added to your rucksack")
                    player.gold -= 10
                    print(f"You have {player.gold} gold coins remaining")
                else:
                     print(f"You only have {player.gold} gold coins!")
            elif choice == '3':
                if (player.gold-15)<0:
                    player.pick_up('bucket')
                    print("You have bought a bucket!. It has been added to your rucksack")
                    player.gold -= 15
                    print(f"You have {player.gold} gold coins remaining")
                else:
                    print(f"You only have {player.gold} golden coins")
           


class Cave(Place):
    def describe(self,player):
        while'lantern' not in player.rucksack:
            direction = input("""Oh no! This cave is very dark and we can't see.
            Which direction would you like to move, in order to go back to the market and buy a lantern """)
            player.move(direction)


        opt = input(f"""You are now in {self.name}
        Luckily, you picked up a lantern ealier
        Oh no! A goblin guards the next item, enter "x" to defeat the goblin and retrieve the item""")
        if opt == 'x':
            opt2=input("""You have defeated the goblin
                  The item is armour. Press 'enter' to pick it up""")
            if not opt2:
                player.pick_up('armour')

class Village(Place):
    def describe(self,player):
        print(f"""You are now in {self.name}
        Here you can buy enchanted items from villagers""")
        opt = input("""What would you like to buy: 1) A Mystery item - 20 gold coins  2) A Money Multiplier - 20 gold coins 3) A Magical Wish - 15 gold coins""")
        if opt == '1':
            remaining = player.gold - 20
            if remaining<0:
                print(f"You only have {player.gold} gold coins")
            else:
                print(f"""You have bought the Mystery Item! It has been added to you backpack.
                You have {remaining} gold coing remaining""")
                player.pick_up('mystery item')
        elif opt == '2':
            remaining = player.gold - 20
            if remaining<0:
                print(f"You only have {player.gold} gold coins")
            else:
                player.gold = player.gold*2
                print(f"""You have bought the Money Multiplier! It has been added to you backpack.
                Congratulations! You went from now have {player.gold} gold coins!""")
        elif opt == '3':
            remaining = player.gold-15
            if remaining<0:
                print(f"You only have {player.gold} gold coins!")      
            else:
                choice = input("You have bought the Magical wish. You can either have 1)100 coins  2)A Lucky Prize")  
                if choice == '1':
                    print(f"Congratulations! You hve been granted 00 gold coins.
                    You now have {player.gold} gold coins")
                elif choice == '2':
                    print("""You have been granted Lucky Prize
                    
                    Congratulations! You have found the Enchanted Treasure and completed the quest!""")
                    exit()


class Castle(Place):
    def describe(self,player):
        print(f"You are now in {self.name}")
        opt = input("""Here you need to be as quick as possible to steal something very special...The crown jewels!
            Press 'enter' to pick them up""")
        if not opt:
            player.pick_up('crown')
        print("Oh no! You've set off an alarm. A huge army is apporoaching to capure you")
        if 'mystery item' in player.rucksack:
            opt1 = input(""" Wait! Luckily you chose the Mystery Item. Press 'enter' to use it if you want to save yourelf!""")
            if not opt1:
                direction = 'east'
                player.move(direction)
        else:
            opt2 = input("""Quick! Go back to the village and find something to defend yourself with. Try to buy something else this time.
             Which direction would you like to move in""")
            player.move(opt2)







    


            

    

#but your strength has greatly reduced. Hurry on to the next level to get better")
            


class Player:
    def __init__(self, name, capacity=5):
        self.name = name
        self.health = 100
        self.strength = 10
        self.energy = 10
        self.gold = 30
        self.rucksack = []
        self.capacity = capacity
        self.current_place = None

    def move(self, direction):
        if direction in self.current_place.connections:
            next_place = self.current_place.connections[direction]
            if next_place.locked:
                if next_place.key in self.rucksack:
                    print(f"You use {next_place.key} to unlock the place!")
                    next_place.locked = False
                else:
                    print("This place is locked. You need a key!")
                    return
            self.current_place = next_place
            self.current_place.describe(self)
        else:
            print("You cannot go that way!")

    def pick_up(self, item):
        if len(self.rucksack)<10:
            self.rucksack.append(item)
            print(f"You have picked up {item}")
        else:
            print("Your rucksack is full!")

    

    def remove_item(self,item):
        self.rucksack.remove(item)
        print(f"You have used the {item} and it is no longer in your rucksack")
       


    def fight(self, enemy):
        if enemy in self.current_place.enemies:
            print(f"You fight {enemy}!")
            if "Sword" in self.rucksack:
                print(f"You defeat {enemy} using the Sword!")
                self.current_place.enemies.remove(enemy)
            else:
                print(f"You were defeated by {enemy}! Game over!")
                self.health = 0
        else:
            print("That enemy is not here.")

    def view_rucksack(self):
        print(f"Rucksack contents: {', '.join(self.rucksack)}")

    def check_map(self):
        print("You check the map. The map shows pathways between places, but it doesn't reveal everything.")

    def solve_puzzle(self):
        print("You attempt to solve the puzzle. Solve this to win!")
        answer = input("What is the sum of 15 and 27? ")
        if answer == "42":
            print("Congratulations! You solved the puzzle and found the Enchanted Treasure!")
            print("You win!")
            self.health = 0
        else:
            print("Incorrect answer. Try again later.")

class Game:
    def __init__(self):
        self.name = input("Enter your name: ")
        self.player = Player(self.name)
        self.setup_world()
        

    def setup_world(self):
        # Create places
        meadow = Meadow("The Meadow", "This is a sunny and safe meadow where no harm can be done.", items=["magical berries"]) 
        market = Market("The Trading Market", "Here you can sell any goods you have in exchange for gold coins", items = ['lantern'])
        cave = Cave("Dark Cave", "This cave is completely dark, and a blind goblin guards the sword you need", items=["armour"], enemies=["goblin"])
        village = Village("The Mystic Village", "Here, you can buy items from the friendly villagers", items=['mystery item'])
        castle = Place("The Ancient Castle", "This castle is guarded by a fierce army", items=["crown"], enemies=["army"], locked=True, key="sword")
        temple = Place("The Temple", "This temple is crucial to your future in the game. Make wise choices!", items=['golden relic'], enemies=["shooting arrows"], locked=True, key=["armour"])
        woods = Place('The Woods', 'You have chosen the wrong destination. This will lead to you doom! There is giant beast here that no man is strong enough to defeat. The only chance for your survival is to take a portal back to the canopy' )
        arctic_desert = Place('The Arctic Desert', 'Here you will find an enchanted rowing boat that will take you to your final destination')
        lost_island = Place('The Lost Island', 'Congratulations! You have found the treasure and made it to the final level')

        

        # Connect places
        market.connect(meadow, "east")
        meadow.connect(market, "west")
        cave.connect(market, "south")
        market.connect(cave, "north")
        village.connect(cave, "east")
        cave.connect(village, "west")
        castle.connect(cave, "south")
        cave.connect(castle, "north")
        temple.connect(castle, "west")
        castle.connect(temple, "east")
        temple.connect(woods, 'east')
        arctic_desert.connect(temple, 'north')
        temple.connect(arctic_desert, 'south')
        lost_island.connect(arctic_desert, 'north')
        arctic_desert.connect(lost_island, 'south')
        
        

        # Set the player's starting place
        self.player.current_place = meadow

        # Store all places    
        self.places = [meadow, market, cave, village, castle, temple, woods, arctic_desert, lost_island]


    def start(self):
        print(f"""\nWelcome {self.player.name} to 'The Quest for the Enchanted Treasure'!
        
        Explore the Land of Eldoria, collect items, fight enemies, and uncover hidden treasures!
        
        Type 'help' for a list of commands.""")

        self.player.current_place.describe(self.player)

        while self.player.health > 0:
            command = input("\nWhat would you like to do? ").strip().lower()

            if command.startswith("move"):
                direction = command.split(" ")[1]
                self.player.move(direction)

            elif command.startswith("pick up"):
                item = command[8:]
                self.player.pick_up(item)

            elif command.startswith("fight"):
                enemy = command[6:]
                self.player.fight(enemy)

            elif command == "view rucksack":
                self.player.view_rucksack()

            elif command == "check map":
                self.player.check_map()

            elif command == "solve puzzle":
                self.player.solve_puzzle()

            elif command == "help":
                print("\nCommands:")
                print("  move [direction] - Move to a new place (north, south, east, west).")
                print("  pick up [item] - Pick up an item in the current place.")
                print("  fight [enemy] - Fight an enemy in the current place.")
                print("  view rucksack - View items in your rucksack.")
                print("  check map - Look at the map for guidance.")
                print("  solve puzzle - Attempt to solve the puzzle if available.")
                print("  exit - Quit the game.")

            elif command == "exit":
                print("Goodbye! Thanks for playing!")
                break

            else:
                print("Invalid command. Type 'help' to see the available commands.")

        print("Game over!")

# Start the game
if __name__ == "__main__":
    game = Game()  
    game.start()