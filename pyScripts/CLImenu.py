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


    
    
    if (userInput=='0'):
        mainMenu()
    elif (userInput=='9'):
        # writes to save.ini
        sw.writeSave(nSettings, nGameMods, nAccount, nHighscores, scoresA)
        print("Now check the directory you ran this from. You'll find your save there. ")
        
    


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
        sw.writeSave()




