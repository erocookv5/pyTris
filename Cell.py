class Cell:
    """
    Cell states:
    None = free
    True = True team
    False = False team
    """    
    def __init__(self):
        self.state = None
    
    def getState(self):
        return self.state

    def setState(self, state):
        self.state = state
