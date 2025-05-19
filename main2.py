
## AUTORES : Denis do Nascimento Rodrigues, Fabricio Fontenele e Ruan Pedro de Araujo Anjos
from execução import application
from process import Process


def main():
    processoss = Process()
    processoss.addProcess("A", 6)
    processoss.addProcess("B", 10)
    processoss.addProcess("C", 15)
    processoss.addProcess("D", 12)
    processoss.addProcess("E", 16)
    processoss.addProcess("C", 15)
    processoss.addProcess("E", 16)

    application(processoss)

if __name__ == "__main__":
    main()
