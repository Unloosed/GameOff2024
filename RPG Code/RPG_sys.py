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
        amount = self.atk # TODO: the amount should be calculated outside the funt call
        message = f"{self.name} attacks {target.name}."
        print(message)
        target.takeDamage(self, amount)
        return


# Class for inventory

# Class for skills


# testing variables