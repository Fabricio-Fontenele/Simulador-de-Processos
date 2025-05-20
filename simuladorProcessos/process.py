class Process:
    def __init__(self):
        self.listProcesses = {}

    def addProcess(self, key, time):
        self.listProcesses[key] = time

    def removeProcess(self, key):
        if key in self.listProcesses:
            del self.listProcesses[key]
            return True
        return False

    def getKey(self):
        return list(self.listProcesses.keys())
    
    def getProcess(self): 
        return list(self.listProcesses)

    def showInfo(self):
        for key, value in self.listProcesses.items():
            print(f'Processo: {key} / Tempo de processo: {value}')