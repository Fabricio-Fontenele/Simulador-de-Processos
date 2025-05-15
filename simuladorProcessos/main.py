from process import Process
from fifo import Fifo
from sjf import SJF

processo = Process()
processo.addProcess("P1", 15)
processo.addProcess("P2", 6)
processo.addProcess("P3", 20)
processo.addProcess("P4", 4)
processo.addProcess("P4", 10)
processo.addProcess("P5", 5)

fifo_exec = Fifo(processo)

fifo_exec.executar()

sjf_exec = SJF(processo)
sjf_exec.executar()

#A saida usei como base o trabalho dos meninos
# mas posso muda a saida qualquer coisa