from process import Process


processo = Process()
processo.addProcess("A", 15)
processo.addProcess("B", 6)
processo.addProcess("C", 20)
processo.addProcess("D", 4)
processo.addProcess("E", 10)
processo.addProcess("F", 5)

processo.showInfo()

processo.turnaround("E")

processo.processTime("E")
