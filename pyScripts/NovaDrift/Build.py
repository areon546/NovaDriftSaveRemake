import base64
from pyScripts.GameMaker2Dictionary import *
from pyScripts.NovaDrift.Mod import *

class NovaDriftBuild(GameMaker2Dictionary):
    
    def __init__(self, weapon, body, shield, name, buildNumber):
        GameMaker2Dictionary.__init__(self, f"scoreStats{buildNumber}", NovaDriftBuild.emptyBuild())
        self.setDictionaryValue("weapon", weapon)
        self.setDictionaryValue("body", body)
        self.setDictionaryValue("shield", shield)
        self.setBuildName(name)

        self.modCount = 0
        return
    
    def setBuildName(self, name):
        self.buildName = name # TODO remove if unused
        self.setDictionaryValue("name", name)
        self.setDictionaryValue("buildNumber", NovaDriftBuild.nameToBase64(name))
        return
    
    def getScore(self):
        return self.dictionary["score"]
    
    def addMod(self, mod: Mod):
        self.modCount += 1
        self.setDictionaryValue(f"mod{self.modCount}", mod)
        return
    
    # Static Methods
    def nameToBase64(name: str): # https://stackoverflow.com/questions/23164058/how-to-encode-text-to-base64-in-python
        b = base64.b64encode(bytes(name, 'utf-8')) # bytes
        base64_str = b.decode('utf-8') # convert bytes to string
        return base64_str
    
    def EmtpyBuildArray(numBuilds: int):
        buildArray = []
        for i in range(numBuilds):
            buildArray.append(NovaDriftBuild("oBlaster", 1.0, 1.0, "", i))

        return buildArray

    def emptyBuild():
        build = {
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
        "score" : 0.00000,
        "weapon" : "oBlaster",
        "body" : 1.000000,
        "shield" : 1.000000,
        }
        
        return build
    