class GameMaker2Dictionary:
    
    def __init__(self, name, dictionary):
        self.title = name
        self.dictionary = dictionary
        return
    
    def __str__(self):
        return f"[{self.title}]\n{self.dictionaryToString()}"
    
    def dictionaryToString(self):
        string = ""
        for key in self.dictionary:
            string += f"{self.keyValueToString(key)}\n"
        return string
    
    def keyValueToString(self, key):
        if key in self.dictionary:
            return f"{key} = \"{self.dictionary[key]}\""
        else:
            return f"badKey{key} = \"0.00000\"" # TODO check if it crashes if this occurs, if it does, make it return an empty string
    
    def setDictionaryValue(self, key, value):
        self.dictionary[key] = value
        return
    
    def getDictionary(self):
        return self.dictionary
    
    