import superGlobals as oV
from pyScripts.CLImenu import CLI
from pyScripts.SaveFile import *
from pyScripts.NovaDrift.Build import *
from pyScripts.GameMaker2Dictionary import *

main = oV.main


if __name__ == '__main__':
    
    print("started")

    if (main):
        print("Main.")    
        #sW.writeSave()
        CLI.mainMenu()
    
    if (not main):
        print("Not Main.")
        
        # CLI.makeSaveFile()
        
        dictionary = NovaDriftBuild.emptyBuild()
        
        # saves = GameMaker2Dictionary("saves", dictionary)
        saves = NovaDriftBuild(weapon="oBlaster", body=1.0, shield=1.0, name="AB-Firecracker", buildNumber=1)
        print(saves)
        
        # sf = sF.SaveFile()
        # print(sf.keybinds)
        # sf.outputScoreStatN(1)
        # sf.sortScoreStats()
        # sf.outputScoreStatN(1)
        
        # print(sf.accountData)
