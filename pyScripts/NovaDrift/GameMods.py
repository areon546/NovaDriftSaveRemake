from pyScripts.GameMaker2Dictionary import GameMaker2Dictionary

class NovaDriftGameModifiers(GameMaker2Dictionary):
    challengeModes = ["practice","endless","dangerZone","enemyTerritory","hostileUniverse","eliteEnemy","nemesis","mayhem","annihilation","wildMetamorphosis","draft"]
    runModifiers = ['practice', 'endless', 'wildMetamorphosis', 'draft']
    
    def __init__(self, dictionary):
        super().__init__("gameMods", dictionary)
        return
    
    # TODO make ask about all challengeModes and runModifiers