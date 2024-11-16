import RPG_sys as RPG
from RPG_items import *

# Create entities and assign them to teams
testEnt1 = RPG.Entity(name="Hero 1", shortName="H1", classList=["friendly"])
testEnt2 = RPG.Entity(name="Hero 2", shortName="H2", classList=["friendly"])
testEnt3 = RPG.Entity(name="Enemy 1", shortName="E1", classList=["enemy"])
testEnt4 = RPG.Entity(name="Enemy 2", shortName='E2', classList=["enemy"])
testPParty = [testEnt1, testEnt2]
testEParty = [testEnt3, testEnt4]

# Create other necessary parts to create an RPG object
testTerrain = RPG.Terrain()
testEncounter = RPG.Encounter(testTerrain, testPParty, testEParty)
testEncounterList = [testEncounter]
testRPG = RPG.RPGMode(testEncounterList, testPParty, testEParty, inventory=[potionA, potionB])

# Set the RPG as an attribute of entities
for p in testPParty:
    p.setRPG(testRPG)
for e in testEParty:
    e.setRPG(testRPG)

# Start the combat
#print(testRPG.loadEncounter())
#print(testRPG.getEntityIndex(testEnt3))
testRPG.combatMenu()