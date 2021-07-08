class Database:
    def __init__(self):
        self.patients = {"sveva": {"music": [(0, "classical"),(0),(0, "rock"),(0, "jazz")], 
                               "tablet":[(1, "politics"), (0, "science"), (0, "health"),
                                         (0, "sport"), (0,"entertainment")]} }

    def addPatient(self, name):
        self.patients[name] = {"music": [("classical",0),("pop",0),("rock",0),("jazz",0)], 
                               "tablet":[(0, "politics"), (0, "science"), (0, "health"),
                                         (0, "sport"), (0,"entertainment")]} 

