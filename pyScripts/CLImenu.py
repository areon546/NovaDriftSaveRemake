import pyScripts.saveWrite as sw
import pyScripts.SaveFile as sF
import pyScripts.dics as di
import superGlobals as oV



class CLI:
    save = sF.SaveFile()

    def mainMenu():
        sw.resetSave()

        userInput = input("""
Do you want an empty save file or do you wanna customise your own save file?

A) Custom Save File
B) Preset

Z) EXIT
""").upper()

        if (userInput=='A'): # CUSTOM
            CLI.makeCustom()

        elif (userInput=='B'): # Presets
            CLI.choosePreset()

        elif (userInput=='Z'):
            print("Goodbye. Hope to see you soon. ")
            return


    def makeCustom(): # TODO create custom CLI and make those decisions and stuff
        message = ""
        userInput = input(f"""
Now creating a new save file. Warning, the program will not save your progress 
until you choose 'Write to file'.

{message}

1. Make Custom Save File
2. Add new Build
3. Import from Debug CSV
4. Import from Alicemetic

0. Write to file. 
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
            CLI.makeSaveFile()
        elif (userInput=='2'):
            # Make build
            CLI.makeBuild()
        elif (userInput=='3'):
            # Debug Import
            pass
        elif (userInput=='4'):
            # Alicemetic Import
            CLI.importSaveFromAlicemetic()
        elif (userInput=='0'):
            # writes to save.ini
            # oh yeah TODO add a system that tells the user if they have not added something for everything
            # TODO bare minimum for acceptable build is high score info 
            sw.writeSave(CLI.save)
            print("Now check the directory you ran this from. You'll find your save there. ")
            
    def makeSaveFile():
        CLI.save.generateSave()
        print("build made")
        CLI.makeCustom()
        return
    
    def makeBuild():
        CLI.save.generateBuild()
        CLI.makeCustom()
        return
        
    def choosePreset():
        presetMap = {
            "1": "empty",
            "2": "clean60"
        }
        
        userInput = input("""
Chose a preset below:
1. Empty
2. Clean Rank 60 (All Unlocks, otherwise empty)

0. Back
    """)
        
        if (userInput=='0'):
            CLI.mainMenu()
        elif (presetMap.get(userInput)!=None):
            CLI.save.setPreset(presetMap.get(userInput))
        else:
            # ask about 
            print("Invalid input. Try Again")
            CLI.choosePreset()

    # TODO make a parser from https://alicemetic.github.io/nova-drift-cheatsheet/ to a build
    def importSaveFromAlicemetic():
        pass