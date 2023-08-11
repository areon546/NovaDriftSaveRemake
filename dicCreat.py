

# check if a string has a specific character in it
def checkChar(string, char):

    for i in string: # loop through
        # if specific char is char, then return true

        if (i==char):   
            return True
    
    return False

# this method will read a given save file and cut up a string to create a dictionary
with open ("save.ini", "r") as save:
    for line in save: 
        # substring []
        if (line[0] == '['):
            title = line[1:-2]
            i=0
        # substring up to =
        else:
            term, val = line.strip().split('=')

            if (checkChar(val, '.')): # check if has a ., if so remove ""
                val = val[1:-2]

        # write to another file
        with open("aaa.txt", "a") as newF:
            if (i==0): # if its a title, then create the dictionary like this
                newF.write(f"""{"}"}\n{title} = {"{"}\n""")
            else: # for all other terms, just add them to the dictionary
                newF.write(f""""{term}" : {val},\n""")

        
        i+=1

