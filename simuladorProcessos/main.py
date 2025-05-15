from process import Process
from execução import application

# mas posso muda a saida qualquer coisa
#A saida usei como base o trabalho dos meninos

def main():
    processo = Process()
    processo.addProcess("P1", 15)
    processo.addProcess("P2", 6)
    processo.addProcess("P3", 20)
    processo.addProcess("P4", 4)
    processo.addProcess("P5", 10)
    processo.addProcess("P6", 5)

    application(processo)

if __name__ == "__main__":
    main()

# addProcess  adiciona um processo passando key e valor
# removeProcess  remove um processo atraves da key
# getKey mostra apenas as key
# showInfo mostra todos processo e valor
# application() passando o paramentro dentro desse metodo voce executa#