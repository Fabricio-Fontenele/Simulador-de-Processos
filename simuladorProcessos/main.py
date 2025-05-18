
## AUTORES : Denis do Nascimento Rodrigues, Fabricio Fontenele e Ruan Pedro de Araujo Anjos

from process import Process
from execução import application

def main():
    processo = Process()
    processo.addProcess("P1", 15)
    processo.addProcess("P2", 7)
    processo.addProcess("P3", 30)
    processo.addProcess("P4", 2)
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
