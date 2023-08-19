print("a")

import overallVars as oV
import pyScripts.CLImenu as CLI

main = oV.main


if __name__ == '__main__':
    
    print("started")

    if (main):    
        CLI.mainMenu()
    
    if (not main):
            print("Not Main.")
