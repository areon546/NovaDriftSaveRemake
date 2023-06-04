plan: 
- database storing at most 10 
- if nothing is inputted into a value, then it is treated as the default value for that, with some restrictions
  - for example body gear is mandatory
  - level isnt mandatory

- has default values. 
 1. pure reset, purist file
 2. rank 60 file

elements in the save file:
- [scoreModList] - depreciated, 1 - 10
- [scoreStats] - 1 - 10
- [customKeys]
- [settings]
- [gameMods]
- [account]
- [highscores]


- each [scoreModList] will so far be made using one of my current ones, or a blank. due to talk of them being fully removed, it will likely not exist for long. 
- [scoreStats] will contain:
 - game mode metadata
 - level
 - wave
 - damage
   - total
   - highest
   - average
 - distance
 - score
 - body gear
 - mods
 - name
 - base64Name


