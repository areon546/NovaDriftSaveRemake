###############################
# this file handles all of the
# writing to the save file
# 
# 
###############################

import dics as di




# write save collates all of the dictionaries and
def writeSave(settings=di.getSettings(), 
        gameMods=di.getGameMods(), acc=di.getAcc(), 
        highscores=di.getHigh(), 
        scoreStats=di.getScoreStatsA()):
    # keys
    # settings
    # gameMods
    # acc
    # highscores
    # scoreStats

    with open("save.ini", "a") as saveF:
        saveF.write("Hi. ")

def resetSave():
    with open("save.ini", "w") as saveF:
        saveF.write("")

def buildHighScores(s1, s2, s3, s4, s5, s6, s7, s8, s9, s10): # these are the dictionaries
    # bubble or insertion sort    
    # get scores into an array
    scores = di.getHigh()
    scoresA = [s1, s2, s3, s4, s5, s6, s7, s8, s9, s10]
    
    # sort array, desc, high to low. if curr smaller, swap

    for i in range(0,10):
        for j in range(i,9):
            # check if j+1 < j
            print("j " + scoresA[j]["score"])
            print("j+1 " + scoresA[j+1]["score"]) # TODO figure out a away to convert numbers into floats
            print((scoresA[j+1]["score"] < scoresA[j]["score"]))
            if (scoresA[j+1]["score"] < scoresA[j]["score"]):
                # swap
                temp = scoresA[j+1]
                scoresA[j+1] = scoresA[j]
                scoresA[j] = temp

    # write to the highscores 
    for i in range(1, 11):
        scores[f"score{i}"] = scoresA[i]["score"]

    return scores               




def writeDictionary(file="save.ini", rw="w", dictionary={}, style=""):
    keys = dictionary.getKeys()
    values = dictionary.getValues()
    maxI = keys.length()
    i=0

    with open(file, rw) as f:
        # while loop here to loop through all of the keys and values in 'dictionary'
        while i<maxI:
            f.write(keys[i])

            if(values[i].type()!=str):
                f.write(f"{values[i]}")
            else:
                f.write(values[i])
            i+=1
            # ok but now the titles. this is enought to be able to write most of it but the titles
            # wait dont i already have this infrastructure somewhere?
            # at i=0 i wanna write the title
            # at every other i value i wanna write keys[i] = values[i]
            # at the last i value (iMax-1) i wanna write \n





def emptySave(): # creates a 'clean' save
    with open("save.ini", "w") as eSave:
        # custom keys (default wasd keybinds)
        eSave.write("""[customKeys]
formationKey="9.000000"
construct5Key="53.000000"
construct4Key="52.000000"
construct3Key="51.000000"
construct2Key="50.000000"
construct1Key="49.000000"
strafeRightKey="69.000000"
strafeLeftKey="81.000000"
strafeKey="16.000000"
banishKey="16.000000"
rerollKey="82.000000"
upgradeKey="13.000000"
thrustKey2="1.000000"
thrustKey="87.000000"
fireKey2="2.000000"
fireKey="32.000000"
upKey="87.000000"
downKey="65.000000"
rightKey="65.000000"
leftKey="65.000000" \n""")
        # settings
        eSave.write("""[settings]
gamepadSteeringLeftStick="1.000000"
disableMouseAim="1.000000"
customGamepadControls="0.000000"
customControls="0.000000"
reduceVFX="0.000000"
backgroundDetail="3.000000"
disableFlash="0.000000"
disableShake="0.000000"
borderedAiming="1.000000"
windowYPos="0.000000"
windowXPos="0.000000"
windowedHeightAspect="1080.000000"
windowedWidthAspect="1920.000000"
enableVSync="0.000000"
borderlessWindow="1.000000"
windowedMode="0.000000"
showSelfDamageNumbers="0.000000"
showHealingNumbers="0.000000"
showDamageNumbers="0.000000"
displayEnemyHull="1.000000"
autoTurret="0.000000"
autoMine="0.000000"
autoDrone="0.000000"
disableUpgradeChaining="0.000000"
assistMode="0.000000"
speedrunMode="0.000000"
showControls="1.000000"
directionalControlScheme="0.000000"
controlScheme="0.000000"
mute="0.000000"
volumeMusic="10.000000"
volumeSFX="10.000000"
volume="10.000000"
largeText="0.000000"
languageOverride="0.000000"\n""")
        # game mods
        eSave.write("""[gameMods]
practice="0.000000"
endless="1.000000"
dangerZone="1.000000"
enemyTerritory="0.000000"
hostileUniverse="0.000000"
eliteEnemy="0.000000"
nemesis="0.000000"
mayhem="0.000000"
annihilation="0.000000"
wildMetamorphosis="0.000000"
draft="0.000000"\n""")
        # account info
        eSave.write("""[account]
accountEXP="0.000000"
levelEXP="0.0"
accountLevel="0.000000"
lifetimeScore="0.000000"\n""")
        # highscores
        eSave.write("""[highscores]
score1="0.000000"
score2="0.000000"
score3="0.000000"
score4="0.000000"
score5="0.000000"
score6="0.000000"
score7="0.000000"
score8="0.000000"
score9="0.000000"
score10="0.000000"\n""")
        # run scores
        for i in range(1,11):
            # score stat list
            eSave.write(f"""[scoreStats{i}]
gameModeDailyChallenge="0.000000"
gameModeBossRush="0.000000"
gameModeDraft="0.000000"
gameModeWildMetamorphosis="0.000000"
gameModeEndless="0.000000"
gameModeAnnihilation="0.000000"
gameModeMayhem="0.000000"
gameModeNemesis="0.000000"
gameModeEliteEnemy="0.000000"
gameModeHostileUniverse="0.000000"
gameModeDangerZone="0.000000"
gameModeEnemyTerritory="0.000000"
level="0.000000"
wave="0.000000"
totalDamage="0.000000"
highestDamage="0.000000"
averageDamage="0.000000"
distance="0.000000"
score="0.000000"\n""")
    print("Default Written. ")

