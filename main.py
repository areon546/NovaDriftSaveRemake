print("a")

import overallVars as oV
import pyScripts.CLImenu as CLI
import pyScripts.saveWrite as sW

main = oV.main


if __name__ == '__main__':
    
    print("started")

    if (main):
        print("Main.")    
        #sW.writeSave()
        CLI.mainMenu()
    
    if (not main):
        print("Not Main.")
