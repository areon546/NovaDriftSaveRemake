


what will my program do?
  - let me rebuild a save file within minutes, if enough screenshots exist for it to be done manually
   - it will be done manually by the user, no image processing. 
  - convert from DEBUG csv file, using alicemetic to create the build in the first place


what might my program do?
  - edit the keybinds into this save file
  - import save files - wait i dont know how to do this in the first place,
    - actually i more or less did this manually to create the dictionaries, i should be able to do this with some automation but it would also be useless
  - alicemetic link would be more annoying text processing, and I'd have to get each and every mod associated string but this is doable

what will my program not do:
  - have users and save their progress. it will be wiped on user exit
  - it will not have specific links to specific states as alicemetic has as its supposed to be a five minuite thing where you cross reference and select the appropriate sections


ND Questions
- ask devs if editing save file affects leaderboards, it shouldnt but i wanna be certain


- if something is inputted into an I, then it overwrites the respective default dictionary
  - some choices might be mandatory, im not sure yet
  - for the websites, this is only calculated when the download button is pressed

- has preset save files
 1. total reset
 2. rank 60 but otherwise clean file



stuff to write to save.ini
- [scoreStats] - 1 - 10
- [customKeys]
- [settings]
- [gameMods]
- [account]
- [highscores]

- [scoreStats] will contain:
 - game mode metadata - 
 - level - 
 - wave - 
 - averageDMG - 
 - highestDMG - 
 - totalDMG - 
 - distance - I
 - score - I
 - body gear - I
 - name - I
 - base64Name - will be calculated onhand. i will have a look at how it does it and use that as the baseline
 - mods


The file will be written from a dictionary where the key and definition are appended together once edited. 
Scores will be stored seperately and it will always write to scoreStats10 even if there is nothing inputted


bare minimum logic
- command line (tedious)






goal
- menu / graphical (difficult)

ok so
- user presses buttons on the screen and those are saved as a dictionary
  - not everything is a button so some things need to be text I fields
- those buttons are transformed into a CSV file
- this CSV file is then used to create the save file
  - each line of the CSV file is a different section


- id want this to be a website. 

- when adding builds, it will have to add newer ones above if they had a higher score, and below if they had a lower score