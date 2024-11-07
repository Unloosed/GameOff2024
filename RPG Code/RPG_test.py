import RPG_sys as RPG

testEnt = RPG.Entity()
testPParty = [testEnt, testEnt]
testEParty = [testEnt, testEnt]
testTerrain = RPG.Terrain()
testEncounter = RPG.Encounter(testTerrain.createBoard(), testPParty, testEParty)
testEncounterList = [testEncounter]
testRPG = RPG.RPGMode(testEncounterList, testPParty, testEParty)
print(testRPG.loadEncounter())
testRPG.combatMenu()