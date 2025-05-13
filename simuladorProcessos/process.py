# turnaRound
# processTime
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

    def turnaround(self, key):
        total = 0
        for keys, value in (self.listProcesses.items()):
            total += value
            if keys == key:
                print(f"\nTurnaround de {key}: {total}")
                break

    def processTime(self, key):
        total = 0
        for keys, value in (self.listProcesses.items()):
            if keys == key:
                break
            total += value
        print(f"Tempo de processo de {key}: {total}")
        return total

    def showInfo(self):
        for key, value in self.listProcesses.items():
            print(f'Processo: {key} / Tempo de processo: {value}')
