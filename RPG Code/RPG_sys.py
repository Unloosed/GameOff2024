'''
File for creating the fundamental RPG system

RPGMode(encounterList, playerParty, enemyParty, inventory=[])
Encounter(board, playerParty, enemyParty)
Terrain(friendlyTerrain=4, enemyTerrain=4, friendlyCondition=[None, None, None, None], enemyCondition=[None, None, None, None])
Entity(name='test name', shortName="ET", maxhp=5, hp=5, maxmp=5, mp=5, atk=2, defense=1, spe=1, luck=1, classList=[])

RPGMode can access terrin through encounterlist[i].board
'''

# Class that manages the rpg game state
#   turn structure, references to characters and enemies, reference to the board
class RPGMode():
    # encounterList     : a list of encounters. encounters contain the initial board state (enemies and terrain)
    #   encounter           : contains the board and initial parties
    #       board               : a 2d array
    #                            [0]   : identifies a tile as friendly terrain or enemy terrain
    #                            [1]   : condition of the tile
    #                            [2]   : the entity occupying the tile
    # playerParty       : a list of the player's party members
    # inventory         : a container class holding all of the players items
    # encounterIndex    : an integer corresponding to which item in the encounter list is current
    def __init__(self, encounterList, playerParty, enemyParty, inventory=[]):
        self.encounterList = encounterList
        self.playerParty = playerParty
        self.enemyParty = enemyParty
        self.inventory = inventory
        self.encounterIndex = 0

    # load the current encounter
    def printEncounter(self):
        encounterString = "Encounter Field:\n"
        boardIndex = 0
        ind = 0
        for tile in self.encounterList[self.encounterIndex].board:
            if tile[2] is not None:
                encounterString += tile[2].shortName
                tile[2].boardIndex = boardIndex
            else:
                encounterString += "_"
            encounterString += "  "
            boardIndex += 1

            ind += 1
            # split the player and enemy sides
            if self.encounterList[self.encounterIndex].terrain.friendlyTerrain == ind:
                encounterString += "|  "
        return encounterString

    def printEntities(self):
        entityList = self.playerParty + self.enemyParty
        validIndexes = []
        for i in range(len(entityList)):
            if entityList[i].hp > 0:
                print(f"{i+1}: {entityList[i].name}")
                print(f"    HP: {entityList[i].hp}/{entityList[i].maxhp}")
                print(f"    MP: {entityList[i].mp}/{entityList[i].maxmp}")
                validIndexes.append(i)
        return validIndexes


    # Return the index on the board that a given entity occupies
    def getEntityIndex(self, entity):
        board = self.encounterList[self.encounterIndex].board
        i = 0
        counter = 0
        for tile in board:
            if tile[2] == entity:
                i = counter
            counter += 1
        return i

    def printInventory(self):
        validInput = []
        print("Inventory Contents:")
        for i in range(len(self.inventory)):
            print(f"  {i+1}. {self.inventory[i].name}\n"
                  f"  {self.inventory[i].description}")
            validInput.append(i)
        return validInput

    # move a entity one space toward the center
    # swap with a potential occupant of that tile
    # does nothing when used at the front
    def swapInward(self, entIndex):
        board = self.encounterList[self.encounterIndex].board
        friendlyTiles = self.encounterList[self.encounterIndex].terrain.friendlyTerrain
        enemyTiles = self.encounterList[self.encounterIndex].terrain.enemyTerrain
        entity = board[entIndex][2]
        if "friendly" in entity.classList:
            # attempt to increment position
            if entIndex >= friendlyTiles-1:
                # cant move forward
                print("Cannot enter enemy territory.")
            else:
                # swap ents at entIndex and space ahead
                board[entIndex][2], board[entIndex+1][2] = board[entIndex+1][2], board[entIndex][2]
                if board[entIndex][2] == None:
                    print(f"{entity.name} advances one space.")
                else:
                    print(f"{entity.name} moves forward and swaps places with {board[entIndex][2].name}.")
        elif "enemy" in entity.classList:
            # attempt to decrement position
            pass
        return


    def swapOutward(self, entIndex):
        board = self.encounterList[self.encounterIndex].board
        friendlyTiles = self.encounterList[self.encounterIndex].terrain.friendlyTerrain
        enemyTiles = self.encounterList[self.encounterIndex].terrain.enemyTerrain
        entity = board[entIndex][2]
        if "friendly" in entity.classList:
            # attempt to decrement position
            if entIndex < 1:
                # cant move forward
                print("Theres no room to the left.")
            else:
                # swap ents at entIndex and space behind
                board[entIndex][2], board[entIndex-1][2] = board[entIndex-1][2], board[entIndex][2]
                if board[entIndex][2] == None:
                    print(f"{entity.name} retreats one space.")
                else:
                    print(f"{entity.name} moves back and swaps places with {board[entIndex][2].name}.")
        elif "enemy" in entity.classList:
            # attempt to decrement position
            pass
        return


    # battle ui logic and basic menu
    def combatMenu(self):
        turn = 1
        livingPlayers = len(self.playerParty)
        livingEnemies = len(self.enemyParty)
        menu = "1. Attack\n2. Move\n3. Item\n4. Skill"
        validOptions = [1, 2, 3, 4]
        choice = 0

        # give every hero a turn to attack
        # TODO: make attacks execute in speed order
        # TODO: make the entity list update dynamically
        # TODO: add enemy attacks
        while livingEnemies > 0 and livingPlayers > 0:
            print("--------------------------------------------------------")
            print(f"Start turn {turn}")
            for hero in self.playerParty:
                print("")
                print(self.printEncounter())
                print("")
                print(f"What will {hero.name} do?")
                print(menu)
                # loop selection menu until a valid choice is made
                while choice not in validOptions:
                    choice = int(input("Selection: "))

                if choice == 1: # attack
                    targetIndex = -1
                    # choose who to attack, loop if bad input
                    print("Choose a target to attack:")
                    validEntIndexes = self.printEntities()
                    entityList = self.playerParty + self.enemyParty
                    while not targetIndex in validEntIndexes and entityList[targetIndex].hp > 0:
                        targetIndex = int(input("Target: ")) - 1

                    # target selected, deal damage
                    hero.dealDamage(entityList[targetIndex], hero.atk)
                    if entityList[targetIndex].hp < 1:
                        livingEnemies -= 1
                        if livingEnemies < 1:
                            break

                elif choice == 2: # move
                    choice2 = 0
                    print("Move where?")
                    print("1. Forward\n2. Backward")
                    while choice2 not in [1, 2]:
                        choice2 = int(input("Selection: "))
                    # move forward
                    if choice2 == 1:
                        self.swapInward(hero.boardIndex)
                    elif choice2 == 2:
                        self.swapOutward(hero.boardIndex)
                    choice2 = 0

                elif choice == 3: # inventory
                    if len(self.inventory) > 0:
                        choice2 = -1
                        validInvIndexes = self.printInventory()
                        while not choice2 in validInvIndexes:
                            choice2 = int(input("Selection: ")) - 1
                        validEntIndexes = self.printEntities()
                        targetIndex = -1
                        while not targetIndex in validEntIndexes:
                            targetIndex = int(input("Use on who?: ")) -1
                        self.inventory[choice2].use(entityList[targetIndex])



                # reset choice
                choice = 0
            turn += 1

        if livingPlayers > 1:
            print("Combat success!")
            self.encounterIndex += 1 # advance to next encounter
        else:
            print("Combat failure.")
        return



# Class for an individual encounter
class Encounter():
    def __init__(self, terrain, playerParty, enemyParty):
        self.board = self.createBoard(terrain)
        self.terrain = terrain
        self.playerParty = playerParty
        self.enemyParty = enemyParty
        self.populateBoard()

    # add players and enemies to the board tiles
    # populates from the outside in
    def populateBoard(self):
        pPartySize = len(self.playerParty)
        ePartySize = len(self.enemyParty)

        for i in range(len(self.board)):
            if i < pPartySize and self.board[i][0] == "friendly tile":
                self.board[i][2] = self.playerParty[i]

        counter = 0
        for i in range(len(self.board)-1, 0, -1):
            if counter < ePartySize and self.board[i][0] == "enemy tile":
                self.board[i][2] = self.enemyParty[counter]
            counter += 1
        return

    # the board is a list of each tile
    # the tiles are each represented by a list
    # [0]   : friendly tile or enemy tile
    # [1]   : condition of the tile
    # [2]   : the entity occupying the tile
    def createBoard(self, terrain):
        board = []
        for i in range(terrain.friendlyTerrain):
            board.append(["friendly tile", terrain.friendlyCondition[i], None])
        for i in range(terrain.enemyTerrain):
            board.append(["enemy tile", terrain.enemyCondition[i], None])
        return board



# Class for the terrain
class Terrain():
    # friendlyTerrain       : the number of friendly terrain tiles
    # enemyTerrain          : the number of enemy terrain tiles
    # friendlyCondition     : a list with a len matching friendlyTerrain. each item in the list is the condition of that terrain tile
    # enemyCondition        : a list with a len matching enemyTerrain. each item in the list is the condition of that terrain tile
    def __init__(self, friendlyTerrain=4, enemyTerrain=4, friendlyCondition=[None, None, None, None], enemyCondition=[None, None, None, None]):
        self.friendlyTerrain = friendlyTerrain
        self.enemyTerrain = enemyTerrain
        self.friendlyCondition = friendlyCondition
        self.enemyCondition = enemyCondition




# Class for entities

class Entity():
    # name              :
    # maxhp             : maximum hp value
    # hp                : current hp value
    # maxmp             : maximum mana value
    # mp                : current mana value
    # atk               :
    # defense           :
    # spe               : speed. calculates turn order
    # luck              : luck. not sure what this will do yet
    # classList         : list of the classes that an entity belongs to. classes are just strings
    def __init__(self, name='test name', shortName="ET", maxhp=5, hp=5, maxmp=5, mp=5, atk=2, defense=1, spe=1, luck=1, classList=[]):
        self.name = name
        self.shortName = shortName
        self.maxhp = maxhp
        self.hp = hp
        self.maxmp = maxmp
        self.mp = mp
        self.atk = atk
        self.defense = defense
        self.spe = spe
        self.luck = luck
        self.classList = classList
        self.boardIndex = -1
        self.RPG = None

    # reduce hp when taking damage
    # print how much damage was taken and if the amount was fatal
    def takeDamage(self, attacker, amount):
        self.hp = self.hp - (amount - self.defense)
        if self.hp < 0:
            self.hp = 0
        message = f"{self.name} has taken {amount} damage."
        if self.hp == 0:
            message += f"\n{self.name} has died!"
        print(message)
        return

    def dealDamage(self, target, amount):
        message = f"{self.name} attacks {target.name}."
        print(message)
        target.takeDamage(self, amount)
        return

    # Gives the entity a way to access to the RPG manager
    def setRPG(self, RPG):
        self.RPG = RPG
        return


# Class for inventory

# Generic parent class for items
class Item():
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def use(self):
        print("Item use function")
        return



# Class for skills


# testing variables