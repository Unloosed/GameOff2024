import RPG_sys as RPG

testEnt1 = RPG.Entity(name="Hero 1")
testEnt2 = RPG.Entity(name="Hero 2")
testEnt3 = RPG.Entity(name="Enemy 1")
testEnt4 = RPG.Entity(name="Enemy 2")
testPParty = [testEnt1, testEnt2]
testEParty = [testEnt3, testEnt4]
testTerrain = RPG.Terrain()
testEncounter = RPG.Encounter(testTerrain.createBoard(), testPParty, testEParty)
testEncounterList = [testEncounter]
testRPG = RPG.RPGMode(testEncounterList, testPParty, testEParty)
print(testRPG.loadEncounter())
testRPG.combatMenu()