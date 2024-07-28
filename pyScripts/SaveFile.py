from pyScripts.NovaDrift.Build import NovaDriftBuild
from pyScripts.NovaDrift.NovaDriftDefaultDict import NovaDriftDefaultDictionaries as NovaDrift

class SaveFile:
    challengeModes = ["practice","endless","dangerZone","enemyTerritory","hostileUniverse","eliteEnemy","nemesis","mayhem","annihilation","wildMetamorphosis","draft"]
    runModifiers = ['practice', 'endless', 'wildMetamorphosis', 'draft']
    
    """
    keybings -> customKeys
    settings
    gameModifiers
    accountData
    highScoreData
    scoreStats1..10
    """
    
    def __init__(self, saveType): # remove as necessary, im not sure how i wanna make it work in a potential GUI
        self.__init__() 
        self.saveType = saveType

    def __init__(self):
        _numberOfBuilds = 0
        
        self.keybinds = NovaDrift.keybinds()
        self.settings = NovaDrift.settings()
        self.gameModifiers = NovaDrift.gameModifiers()
        self.accountData = NovaDrift.account()
        self.highScoreData = NovaDrift.highscores()
        self.builds = NovaDriftBuild.EmtpyBuildArray(10)

    def __str__(self):
        stringRepresentation = f"{self.settings}\n{self.gameModifiers}\n{self.accountData}\n{self.highScoreData}\n"
        
        for i in range(len(self.builds)):
            stringRepresentation += f"{self.builds[i]}\n"
            
        stringRepresentation += f"{self.keybinds}"
        
        return stringRepresentation

    def __swap(a,b):
        temp = a
        a = b
        b = temp
        return a,b

    def incrementBuildNumber(self):
        self._numberOfBuilds+=1
        return

    def sortScoreStats(self):
        length = len(self.builds)
        for i in range(length):
            
            # sort score stats
            for j in range(i, length-1):
                # print(i,j)
                # sorts items based on the score attribute
                if (self.builds[j].getScore() < self.builds[j+1].getScore()):
                    self.builds[j], self.builds[j+1] = SaveFile.__swap(self.builds[j], self.builds[j+1])
        return

    ## SETTING VALUES

    def generateValueForKey(self, dictionary, key, message):
        dictionary[key] = input(message)
        return
    
    def toggleBooleanKey(self, dictionary, key):
        userInput = input(f"Do you want to toggle {key}?" + " y\\N: ")
        print("Input 'y' for true, and anything else for false. ")

        if (userInput=="y" and key in dictionary) :
            dictionary[key] = 1.0 - dictionary[key]
        else:
            print(f"Key: {key} not found in dictionary: {dictionary}. ")
        
        return
    
    def generateValueForBooleanKey(self, dictionary, key, message):
        userInput = input(message + " y\\N")
        print("Input 'y' for true, and anything else for false. ")

        value = 0.0
        if (userInput=="y") :
            value = 1.0

        self.changeValueOfKey(dictionary, key, value)

        return
    
    def toggleBooleanKey(self, dictionary, key):
        if (key in dictionary):
            if (dictionary[key]==0.0):
                self.changeValueOfKey(dictionary, key, 1.0)
            else:
                self.changeValueOfKey(dictionary, key, 0.0)
        else:
            print(f"Key {key} not found in dictionary {dictionary}. ")
        return

    def changeValueOfKey(self, dictionary, key, newValue):
        dictionary[key] = newValue
        return
    
    def __generateBooleanInput(message):
        return input(message + " y\\N: ") == 'y'

    # ## ASK USER
    # def askUser(self, message):
    #     if (self.saveType=="cli"):
    #         return input(message)
        
    # def tellUser(self, message):
    #     if (self.saveType=="cli"):
    #         print(message)
            
    #     return

    ## SETTING GAME MODES
    
    def __turnOnAnnihilation(self):
        # if mayhem is on, set all previous values to on
        for challengeMode in self.challengeModes:
            self.setValueForKey(self.gameModifiers, challengeMode, 1.0)
        return
    
    def __turnOffAnnihilation(self):
        self.setValueForKey(self.gameModifiers, "annihilation", 0.0)
        return

    def __turnOnMayhem(self):
        self.__turnOnAnnihilation()
        self.__turnOffAnnihilation()
        return

    
    def __turnOffMayhem(self):
        self.__turnOnMayhem()
        self.setValueForKey(self.gameModifiers, "mayhem", 0.0)
        return

    
    def __turnOnPractice(self):
        # if practice is on, set all other values off
        
        # turn every game mode off
        for key in self.gameModifiers:
            self.setValueForKey(self.gameModifiers, key, 0.0)
            
        # turn on specified game modes
        self.setValueForKey(self.gameModifiers, "practice", 1.0)
        self.setValueForKey(self.gameModifiers, "endless", 1.0)
        
        return
    
    def __turnOffPractice(self):
        self.setValueForKey(self.gameModifiers, "practice", 0.0)
        return
    
    
    def setValueForKey(self, dictionary, key, value):
        if (key in dictionary):
            dictionary[key] = value
        return
    
    # GENERATING A NEW SAVE
    
    def generateGameDamage(self, build):
        # TODO make it ask about average, total, and highest dmg
        suffix = "Damage"
        damageCategories = ['total', 'average', 'highest']
        
        
        for damageCategory in damageCategories:
            self.generateValueForKey(build, (damageCategory+suffix), f"Do you want to enable {damageCategory}?")
        
        return
    
    
    # TODO Unfinished
    
    def generateSave(self):
        
        # ask about keybinds
        if (SaveFile.__generateBooleanInput("Do you want to change keybinds?")):
            self.newKeybinds()
            
        # ask about settings
        if (SaveFile.__generateBooleanInput("Do you want to change settings?")):
            self.newSettings()
            
        # ask about game modifiers
        if (SaveFile.__generateBooleanInput("Do you want to change game modifiers?")):
            self.newGameModifiers()
            
        # ask about account data
        if (SaveFile.__generateBooleanInput("Do you want to change account data?")):
            self.newAccountData()
            
        return
    
    def generateBuild(self):
        # add build
        
        # ask for name
        name = input("Please enter a name for the build. ")
        
        # ask for numbers
            # distance, avg dmg, total dmg, highest dmg, wave, lvl, name, 

        # ask for game modifiers
        # ask for body gears
        # ask for the mod list
            # i do this by asking them to type in the name of a mod 
            
        
        
        self.incrementBuildNumber()
        self.addBuild(name, self._buildNumber)
        return
    
    def addBuild(self, name, buildNumber):
        # place the build in the correct spot in the array
        for i in range(len(self.builds)):
            if (self.builds[i]==None):
                b = NovaDriftBuild(name=name, buildNumber=i)
                index = i
            elif (self.builds[i].getScore() < 0.0):
                b = NovaDriftBuild(name=name, buildNumber=i)
                index = i

        self.builds[index] = b
        return b
    
        
        b = NovaDriftBuild(name=name, buildNumber=buildNumber)
        self.builds.append(b)
        return b
    
    # TODO ask about every single key in the dictionary and ask whether it should be reassigned to a specific value
    def newKeybinds(self):        
        keybinds = self.keybinds.getDictionary()
        return
    
    # TODO ask about every single key in the dictionary and ask whether it should be reassigned to a specific value
    def newSettings(self):
        settings = self.settings.getDictionary()

        # loop through each setting
        for key in settings:
            # for boolean settings, ask if they want to enable or disable
            
            # for other settings, set a value based on valid ranges
            
            # TODO determine which keys are booleans
            """
            settings that arent booleans:
            - volumeMusic
            - volumeSFX
            - volume
            """
            if (key=="volumeMusic" or key=="volumeSFX" or key=="volume"):
                self.generateValueForKey(settings, key, f"Please enter a value between 0 and 10 for {key}. ")
            else :            
                self.generateValueForBooleanKey(settings, key, f"Do you want to enable {key}?")
        
        
        return

    # TODO ask about every single key in the dictionary and ask whether it should be reassigned to a specific value
    def newGameModifiers(self):
        gameModes = self.gameModifiers.getDictionary()
        
        # TODO practice mode turns everything off, other than endless mode
        # TODO endless mode currently doesn't have an ended alternative
        
        for gameMode in gameModes:
            self.generateValueForBooleanKey(self.gameModifiers, gameMode, f"Do you want to enable {gameMode}?")
        return
    
    # TODO ask about every single key in the dictionary and ask whether it should be reassigned to a specific value
    def newAccountData(self):
        accountInfo = self.accountData.getDictionary()
        
        for accountDatum in accountInfo:
            self.generateValueForKey(accountInfo, accountDatum, f"Please enter a value for {accountDatum}. ")
        return
    
    # TODO ask about every single key in the dictionary and ask whether it should be reassigned to a specific value
    def newBuild(self): # creates a new build from scratch, and assigns it into 
        build = {}

        self.generateBuildGameModes(build)
        self.generateGameDamage(build)

        
        # TODO ask about weapon, body, and shield
        
        # TODO while loop, 1 -> n, n is based on when they stop putting in information
        
        
        self._numberOfBuilds+=1
        return
    
    # TODO idk what this does, find out what it's used for and imeplement that i guess
    def generateModInfo(self):
        # I suspect this is what I intend to use for asking about specified mods for builds?
        return
        
    # TODO make it ask about DailyChallenge BossRush Draft WildMeta Endless Annihilation Mayhem Nemesis EliteEnemy HostileUniverse DangerZone EnemyTerritory
    def generateBuildGameModes(self, build):
        gM = "gameMode"
        gameModes = ['DailyChallenge', 'BossRush', 'Draft', 'WildMeta', 'Endless', 'Annihilation', 'Mayhem', 'Nemesis', 'EliteEnemy', 'HostileUniverse', 'DangerZone', 'EnemyTerritory']
        
        for gameMode in gameModes:
            self.generateValueForBooleanKey(build, (gM+gameMode), f"Do you want to enable {gameMode}?")
        
        return

    # TODO figure out the values of the inputs for keybinds
    def keybindToLetterAssociation(self):
        # TODO figure out all the values of all of the keys that game maker 2 uses and let people assign values based off of the letters they type
        # make sure to add special character support, based off of what they normally are represented as (I will do this based off of AHK special character keybinds), as well as just typing it out
        return
    
    # Presets
    
    def setPreset(preset):
        save = SaveFile()
        if (preset=="empty"):
            SaveFile.setEmptyPreset(save)
        elif (preset=="clean60"):
            SaveFile.setClean60Preset(save)
        return
    
    def setEmtpyPreset():
        # set all values to what they would be in a new file
        return
    
    def setClean60Preset(save):
        save.setValueForKey(save.accountData, "accountLevel", 60.0)
        return save
    

    # Getters
    
    def getScoreStatN(self, n):
        if (n>0 & n<11):
            return self.builds[n-1]
        return None
        
    def getScoreStats(self):
        return self.builds

    def outputScoreStatN(self, n):
        print(self.getScoreStatN(n))

    def outputScoreStats(self):
        for i in range (len(self.builds)):
            print(self.builds[i])
            print()
        return

    def getKeybinds(self):
        return self.keybinds
    
    def getSettings(self):
        return self.settings
    
    def getGameModifiers(self):
        return self.gameModifiers
    
    def getAccountData(self):
        return self.accountData

    def getHighscores(self):
        return self.highScoreData
    