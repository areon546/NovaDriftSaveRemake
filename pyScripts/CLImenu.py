import pyScripts.saveWrite as sw
import pyScripts.dics as di
import overallVars as oV

nSettings = di.settings
nGameMods = di.gameMods
nAccount = di.account
nHighscores = di.highscores
scoresA = [di.scoreStats1, di.scoreStats2, 
            di.scoreStats3, di.scoreStats4, 
            di.scoreStats5, di.scoreStats6, 
            di.scoreStats7, di.scoreStats8, 
            di.scoreStats9, di.scoreStats10]



def mainMenu():
    sw.resetSave()

    userInput = input("""
Do you want an empty save file or do you wanna customise your own save file?

A) Custom Save File
B) Preset

Z) EXIT
    """).upper()

    if (userInput=='A'): # CUSTOM
        makeCustom()

    elif (userInput=='B'): # Presets
        choosePreset()

    elif (userInput=='Z'):
        print("Goodbye. Hope to see you soon. ")


def makeCustom(): # TODO create custom CLI and make those decisions and stuff
    userInput = input("""
Now creating a new save file. Warning, the program will not save your progress 
until you writing to the file.

1. Make build
2. Import from Debug
3. Import from Alicemetic

9. Write to file. 
0. Back

""")

    ########################
    # adding high scores / build
    #  - each time the highscores dic will be sorted
    #  - will also have to have a minimum. 
    #     - in fact lets make the highscores dic a class
    # adding imports
    # 
    # 
    # 
    # 
    # 
    #  
    # 
    # #####################


    if (userInput=='1'):
        # Make Build
        makeBuild()
    elif (userInput=='2'):
        # Debug Import
    elif (userInput=='2'):
        # Alicemetic Import
    elif (userInput=='0'):
        mainMenu()
    elif (userInput=='9'):
        # writes to save.ini
        # oh yeah TODO add a system that tells the user if they have not added something for everything
        # TODO bare minimum for acceptable build is high score info 
        sw.writeSave(nSettings, nGameMods, nAccount, nHighscores, scoresA)
        print("Now check the directory you ran this from. You'll find your save there. ")
        
def makeBuild():
    print("")
    # ok so what are the requirements of a build?
    # high score info
        # distance, avg dmg, total dmg, highest dmg, wave, lvl, name, 
    # a mod list
    # a name
    # body gears (i can make them choose 1 in each of WBS)
    # game mod, eg wild, anni, draft, 
    


def choosePreset(): 
    # TODO add selection structure to presets
    # TODO add more presets
    # TODO set up a way to have presets
    userInput = input("""
Chose a preset below:
1. Empty
2. Clean Rank 60 (All Unlocks, otherwise empty)

0. Back
""")
    
    if (userInput=='0'):
        mainMenu()
    elif (userInput=='1'):
        sw.emptySave()
    elif (userInput=='2'):
        nAccount["accountLevel"] = 60.00000
        sw.writeSave()




