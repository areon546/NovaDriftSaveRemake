################
# this file contains all of the
# dictionaries that are used elsewhere
# 
##############



def getCustKey():
    return customKeys
def getSettings():
    return settings
def getGameMods():
    return gameMods
def getAcc():
    return account
def getHigh():
    return highscores

def setHigh(scores):
    highscores = scores

def getScoreStatsA():
    return scoresA

def setScoresStatsA(nScores):
    scoresA = nScores




# TODO make the adding builds functionality one based on classes
"""
class Highscore:
    scoresA = [scoreStats1, scoreStats2,
                scoreStats3, scoreStats4, 
                scoreStats5, scoreStats6, 
                scoreStats7, scoreStats8, 
                scoreStats9, scoreStats10]
    
    minScore = 0 # this contains the minimum score here
    numScores = 0 # this is the next index of scoresA

    def addScore(score):
        # this method will add a 
        this.scoresA[this.numScores] = score
"""    







############################################################################

customKeys = {
"formationKey" : 9.00000,
"construct5Key" : 53.00000,
"construct4Key" : 52.00000,
"construct3Key" : 51.00000,
"construct2Key" : 50.00000,
"construct1Key" : 49.00000,
"strafeRightKey" : 69.00000,
"strafeLeftKey" : 81.00000,
"strafeKey" : 16.00000,
"banishKey" : 16.00000,
"rerollKey" : 82.00000,
"upgradeKey" : 13.00000,
"thrustKey2" : 1.00000,
"thrustKey" : 87.00000,
"fireKey2" : 2.00000,
"fireKey" : 32.00000,
"upKey" : 87.00000,
"downKey" : 65.00000,
"rightKey" : 65.00000,
"leftKey" : 65.00000
}
settings = {
"gamepadSteeringLeftStick" : 1.00000,
"disableMouseAim" : 1.00000,
"customGamepadControls" : 0.00000,
"customControls" : 0.00000,
"reduceVFX" : 0.00000,
"backgroundDetail" : 3.00000,
"disableFlash" : 0.00000,
"disableShake" : 0.00000,
"borderedAiming" : 1.00000,
"windowYPos" : 0.00000,
"windowXPos" : 0.00000,
"windowedHeightAspect" : 1080.00000,
"windowedWidthAspect" : 1920.00000,
"enableVSync" : 0.00000,
"borderlessWindow" : 1.00000,
"windowedMode" : 0.00000,
"showSelfDamageNumbers" : 0.00000,
"showHealingNumbers" : 0.00000,
"showDamageNumbers" : 0.00000,
"displayEnemyHull" : 1.00000,
"autoTurret" : 0.00000,
"autoMine" : 0.00000,
"autoDrone" : 0.00000,
"disableUpgradeChaining" : 0.00000,
"assistMode" : 0.00000,
"speedrunMode" : 0.00000,
"showControls" : 1.00000,
"directionalControlScheme" : 0.00000,
"controlScheme" : 0.00000,
"mute" : 0.00000,
"volumeMusic" : 10.00000,
"volumeSFX" : 10.00000,
"volume" : 10.00000,
"largeText" : 0.00000,
"languageOverride" : 0.00000
}
gameMods = {
"practice" : 0.00000,
"endless" : 1.00000,
"dangerZone" : 0.00000,
"enemyTerritory" : 0.00000,
"hostileUniverse" : 0.00000,
"eliteEnemy" : 0.00000,
"nemesis" : 0.00000,
"mayhem" : 0.00000,
"annihilation" : 0.00000,
"wildMetamorphosis" : 0.00000,
"draft" : 0.00000
}
account = {
"accountEXP" : 0.00000,
"levelEXP" : 0.,
"accountLevel" : 0.00000,
"lifetimeScore" : 0.00000
}
highscores = {
"score1" : 0.00000,
"score2" : 0.00000,
"score3" : 0.00000,
"score4" : 0.00000,
"score5" : 0.00000,
"score6" : 0.00000,
"score7" : 0.00000,
"score8" : 0.00000,
"score9" : 0.00000,
"score10" : 0.00000
}
scoreStats1 = {
"gameModeDailyChallenge" : 0.00000,
"gameModeBossRush" : 0.00000,
"gameModeDraft" : 0.00000,
"gameModeWildMetamorphosis" : 0.00000,
"gameModeEndless" : 0.00000,
"gameModeAnnihilation" : 0.00000,
"gameModeMayhem" : 0.00000,
"gameModeNemesis" : 0.00000,
"gameModeEliteEnemy" : 0.00000,
"gameModeHostileUniverse" : 0.00000,
"gameModeDangerZone" : 0.00000,
"gameModeEnemyTerritory" : 0.00000,
"level" : 0.00000,
"wave" : 0.00000,
"totalDamage" : 0.00000,
"highestDamage" : 0.00000,
"averageDamage" : 0.00000,
"distance" : 0.00000,
"score" : 0.00000
}
scoreStats2 = {
"gameModeDailyChallenge" : 0.00000,
"gameModeBossRush" : 0.00000,
"gameModeDraft" : 0.00000,
"gameModeWildMetamorphosis" : 0.00000,
"gameModeEndless" : 0.00000,
"gameModeAnnihilation" : 0.00000,
"gameModeMayhem" : 0.00000,
"gameModeNemesis" : 0.00000,
"gameModeEliteEnemy" : 0.00000,
"gameModeHostileUniverse" : 0.00000,
"gameModeDangerZone" : 0.00000,
"gameModeEnemyTerritory" : 0.00000,
"level" : 0.00000,
"wave" : 0.00000,
"totalDamage" : 0.00000,
"highestDamage" : 0.00000,
"averageDamage" : 0.00000,
"distance" : 0.00000,
"score" : 0.00000
}
scoreStats3 = {
"gameModeDailyChallenge" : 0.00000,
"gameModeBossRush" : 0.00000,
"gameModeDraft" : 0.00000,
"gameModeWildMetamorphosis" : 0.00000,
"gameModeEndless" : 0.00000,
"gameModeAnnihilation" : 0.00000,
"gameModeMayhem" : 0.00000,
"gameModeNemesis" : 0.00000,
"gameModeEliteEnemy" : 0.00000,
"gameModeHostileUniverse" : 0.00000,
"gameModeDangerZone" : 0.00000,
"gameModeEnemyTerritory" : 0.00000,
"level" : 0.00000,
"wave" : 0.00000,
"totalDamage" : 0.00000,
"highestDamage" : 0.00000,
"averageDamage" : 0.00000,
"distance" : 0.00000,
"score" : 0.00000
}
scoreStats4 = {
"gameModeDailyChallenge" : 0.00000,
"gameModeBossRush" : 0.00000,
"gameModeDraft" : 0.00000,
"gameModeWildMetamorphosis" : 0.00000,
"gameModeEndless" : 0.00000,
"gameModeAnnihilation" : 0.00000,
"gameModeMayhem" : 0.00000,
"gameModeNemesis" : 0.00000,
"gameModeEliteEnemy" : 0.00000,
"gameModeHostileUniverse" : 0.00000,
"gameModeDangerZone" : 0.00000,
"gameModeEnemyTerritory" : 0.00000,
"level" : 0.00000,
"wave" : 0.00000,
"totalDamage" : 0.00000,
"highestDamage" : 0.00000,
"averageDamage" : 0.00000,
"distance" : 0.00000,
"score" : 0.00000
}
scoreStats5 = {
"gameModeDailyChallenge" : 0.00000,
"gameModeBossRush" : 0.00000,
"gameModeDraft" : 0.00000,
"gameModeWildMetamorphosis" : 0.00000,
"gameModeEndless" : 0.00000,
"gameModeAnnihilation" : 0.00000,
"gameModeMayhem" : 0.00000,
"gameModeNemesis" : 0.00000,
"gameModeEliteEnemy" : 0.00000,
"gameModeHostileUniverse" : 0.00000,
"gameModeDangerZone" : 0.00000,
"gameModeEnemyTerritory" : 0.00000,
"level" : 0.00000,
"wave" : 0.00000,
"totalDamage" : 0.00000,
"highestDamage" : 0.00000,
"averageDamage" : 0.00000,
"distance" : 0.00000,
"score" : 0.00000
}
scoreStats6 = {
"gameModeDailyChallenge" : 0.00000,
"gameModeBossRush" : 0.00000,
"gameModeDraft" : 0.00000,
"gameModeWildMetamorphosis" : 0.00000,
"gameModeEndless" : 0.00000,
"gameModeAnnihilation" : 0.00000,
"gameModeMayhem" : 0.00000,
"gameModeNemesis" : 0.00000,
"gameModeEliteEnemy" : 0.00000,
"gameModeHostileUniverse" : 0.00000,
"gameModeDangerZone" : 0.00000,
"gameModeEnemyTerritory" : 0.00000,
"level" : 0.00000,
"wave" : 0.00000,
"totalDamage" : 0.00000,
"highestDamage" : 0.00000,
"averageDamage" : 0.00000,
"distance" : 0.00000,
"score" : 0.00000
}
scoreStats7 = {
"gameModeDailyChallenge" : 0.00000,
"gameModeBossRush" : 0.00000,
"gameModeDraft" : 0.00000,
"gameModeWildMetamorphosis" : 0.00000,
"gameModeEndless" : 0.00000,
"gameModeAnnihilation" : 0.00000,
"gameModeMayhem" : 0.00000,
"gameModeNemesis" : 0.00000,
"gameModeEliteEnemy" : 0.00000,
"gameModeHostileUniverse" : 0.00000,
"gameModeDangerZone" : 0.00000,
"gameModeEnemyTerritory" : 0.00000,
"level" : 0.00000,
"wave" : 0.00000,
"totalDamage" : 0.00000,
"highestDamage" : 0.00000,
"averageDamage" : 0.00000,
"distance" : 0.00000,
"score" : 0.00000
}
scoreStats8 = {
"gameModeDailyChallenge" : 0.00000,
"gameModeBossRush" : 0.00000,
"gameModeDraft" : 0.00000,
"gameModeWildMetamorphosis" : 0.00000,
"gameModeEndless" : 0.00000,
"gameModeAnnihilation" : 0.00000,
"gameModeMayhem" : 0.00000,
"gameModeNemesis" : 0.00000,
"gameModeEliteEnemy" : 0.00000,
"gameModeHostileUniverse" : 0.00000,
"gameModeDangerZone" : 0.00000,
"gameModeEnemyTerritory" : 0.00000,
"level" : 0.00000,
"wave" : 0.00000,
"totalDamage" : 0.00000,
"highestDamage" : 0.00000,
"averageDamage" : 0.00000,
"distance" : 0.00000,
"score" : 0.00000
}
scoreStats9 = {
"gameModeDailyChallenge" : 0.00000,
"gameModeBossRush" : 0.00000,
"gameModeDraft" : 0.00000,
"gameModeWildMetamorphosis" : 0.00000,
"gameModeEndless" : 0.00000,
"gameModeAnnihilation" : 0.00000,
"gameModeMayhem" : 0.00000,
"gameModeNemesis" : 0.00000,
"gameModeEliteEnemy" : 0.00000,
"gameModeHostileUniverse" : 0.00000,
"gameModeDangerZone" : 0.00000,
"gameModeEnemyTerritory" : 0.00000,
"level" : 0.00000,
"wave" : 0.00000,
"totalDamage" : 0.00000,
"highestDamage" : 0.00000,
"averageDamage" : 0.00000,
"distance" : 0.00000,
"score" : 0.00000
}
scoreStats10 = {
"gameModeDailyChallenge" : 0.00000,
"gameModeBossRush" : 0.00000,
"gameModeDraft" : 0.00000,
"gameModeWildMetamorphosis" : 0.00000,
"gameModeEndless" : 0.00000,
"gameModeAnnihilation" : 0.00000,
"gameModeMayhem" : 0.00000,
"gameModeNemesis" : 0.00000,
"gameModeEliteEnemy" : 0.00000,
"gameModeHostileUniverse" : 0.00000,
"gameModeDangerZone" : 0.00000,
"gameModeEnemyTerritory" : 0.00000,
"level" : 0.00000,
"wave" : 0.00000,
"totalDamage" : 0.00000,
"highestDamage" : 0.00000,
"averageDamage" : 0.00000,
"distance" : 0.00000,
"score" : 0.00000
}

scoresA = [scoreStats1, scoreStats2,
            scoreStats3, scoreStats4, 
            scoreStats5, scoreStats6, 
            scoreStats7, scoreStats8, 
            scoreStats9, scoreStats10]

