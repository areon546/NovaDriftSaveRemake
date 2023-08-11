# this method will read a given save file and cut up a string to create a dictionary
i = 0

with open ("save.ini", "r") as save:
    for line in save: 
        # substring []
        if (line[0] == '['):
            title = line[1:-2]
            i=0
        # substring up to =
        else:
            term, val = line.strip().split('=')

        # write to another file
        with open("aaa.txt", "a") as newF:
            if (i==0): # if its a title, then create the dictionary like this
                newF.write(f"""{"}"}\n{title} = {"{"}\n""")
            else:
                newF.write(f""""{term}" : {val},\n""")

        
        i+=1



