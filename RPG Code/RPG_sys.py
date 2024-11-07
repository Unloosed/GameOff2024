'''
File for creating the fundamental RPG system
'''



# Class that manages the rpg game state
#   turn structure, references to characters and enemies, reference to the board
class RPGMode():
    # encounterList     : a list of encounters. encounters contain the initial board state (enemies and terrain)
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
    def loadEncounter(self):
        encounterString = "Encounter Field:\n"
        for tile in self.encounterList[self.encounterIndex].board:
            if tile[2] is not None:
                encounterString += "0"
            else:
                encounterString += "_"
            encounterString += "  "
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
        print(f"Start turn {turn}")
        for hero in self.playerParty:
            while livingEnemies > 0 and livingPlayers > 0:
                print(menu)
                # loop selection menu until a valid choice is made
                while choice not in validOptions:
                    choice = int(input("Selection: "))
                # attack
                if choice == 1:
                    targetIndex = -1
                    # choose who to attack, loop if bad input
                    print("Choose a target to attack:")
                    validEntIndexes = self.printEntities()
                    entityList = self.playerParty + self.enemyParty
                    while not targetIndex in validEntIndexes and entityList[targetIndex].hp > 0:
                        targetIndex = int(input("Target: ")) - 1

                    # target selected, deal damage
                    hero.dealDamage(entityList[targetIndex], hero.atk)

                # reset choice
                choice = 0

        return



# Class for an individual encounter
class Encounter():
    def __init__(self, board, playerParty, enemyParty):
        self.board = board
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
        self.board = self.createBoard()

    # the board is a list of each tile
    # the tiles are each represented by a list
    # [0]   : friendly tile or enemy tile
    # [1]   : condition of the tile
    # [2]   : the entity occupying the tile
    def createBoard(self):
        board = []
        for i in range(self.friendlyTerrain):
            board.append(["friendly tile", self.friendlyCondition[i], None])
        for i in range(self.enemyTerrain):
            board.append(["enemy tile", self.enemyCondition[i], None])
        return board


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
    def __init__(self, name='test name', maxhp=5, hp=5, maxmp=5, mp=5, atk=2, defense=1, spe=1, luck=1, classList=[]):
        self.name = name
        self.maxhp = maxhp
        self.hp = hp
        self.maxmp = maxmp
        self.mp = mp
        self.atk = atk
        self.defense = defense
        self.spe = spe
        self.luck = luck
        self.classList = classList

    # reduce hp when taking damage
    # print how much damage was taken and if the amount was fatal
    def takeDamage(self, attacker, amount):
        self.hp = self.hp - amount
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


# Class for inventory

# Class for skills


# testing variables