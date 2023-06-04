

# ok so do i want a UI?? so far I think its better to not do that. 

def writeSave(data):
    with open("save.ini", "a") as saveF:
        saveF.write("Hi. ")

def resetSave():
    with open("save.ini", "w") as saveF:
        saveF.write("")

def emptySave(): # creates a 'clean' save
    with open("save.ini", "w") as eSave:
        # score mod list
        for i in range(1,11):
            eSave.write(f"[scoreModList{i}]\n")
            eSave.write('0=""\n')

        # score stat list
        for i in range(1,11):
            eSave.write(f"[scoreModList{i}]\n")
            eSave.write('0=""\n')
        # custom keys (default wasd keybinds)
        # settings
        # game mods
        # account info
        # highscores






if __name__ == '__main__':
    print("This only executes when %s is executed rather than imported" % __file__)

    resetSave()
    emptySave()
