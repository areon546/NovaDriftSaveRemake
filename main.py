print("a")

import saveWrite as sw
import dics as di
import overallVars as oV

nSettings = di.settings
nGameMods = di.gameMods
nAccount = di.account
nHighscores = di.highscores
scores = [di.scoreStats1, di.scoreStats2, 
          di.scoreStats3, di.scoreStats4, 
          di.scoreStats5, di.scoreStats6, 
          di.scoreStats7, di.scoreStats8, 
          di.scoreStats9, di.scoreStats10]

main = oV.main

if __name__ == '__main__':
    
    print("worked")
    sw.resetSave()
    
    if (not main):
            print("Not Main.")

    
    if (main):    
        print("""
    Do you want an empty save file or do you wanna customise your own save file?

    A) Custom Save File
    B) Preset
    C) EXIT
        """)

        userChoice = input().upper()
        if (userChoice=='A'): # CUSTOM
            print("now creating a custom file")

            # make the custom file

            # write the custom file
            nSettings["disableMouseAim"] = "0"

            sw.writeSave(nSettings, nGameMods, nAccount, nHighscores, )


        elif (userChoice=='B'): # Presets
            print("""
    Chose a preset below:
    1. Empty
    2. Rank 60 (All Unlocks, otherwise empty)
    3. 



    """)    
            # TODO add selection structure to presets
            sw.emptySave()

        elif (userChoice=='C'):
            print("Goodbye. Hope to see you soon. ")



    #    print("Now check the directory you downloaded this into. You'll find save.ini there. ")

