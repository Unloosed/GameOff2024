import RPG_sys as RPG

testEnt1 = RPG.Entity(name="Hero 1", shortName="H1", classList=["friendly"])
testEnt2 = RPG.Entity(name="Hero 2", shortName="H2", classList=["friendly"])
testEnt3 = RPG.Entity(name="Enemy 1", shortName="E1", classList=["enemy"])
testEnt4 = RPG.Entity(name="Enemy 2", shortName='E2', classList=["enemy"])
testPParty = [testEnt1, testEnt2]
testEParty = [testEnt3, testEnt4]
testTerrain = RPG.Terrain()
testEncounter = RPG.Encounter(testTerrain.createBoard(), testPParty, testEParty)
testEncounterList = [testEncounter]
testRPG = RPG.RPGMode(testEncounterList, testPParty, testEParty)
print(testRPG.loadEncounter())
testRPG.combatMenu()