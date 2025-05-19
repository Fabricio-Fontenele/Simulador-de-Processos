
## AUTORES : Denis do Nascimento Rodrigues, Fabricio Fontenele e Ruan Pedro de Araujo Anjos

from process import Process
from execução import application

def main():
    processo = Process()
    processo.addProcess("B", 10)
    processo.addProcess("E", 16)
    processo.addProcess("A", 6)
    processo.addProcess("D", 12)
    processo.addProcess("C", 15)

    application(processo)

if __name__ == "__main__":
    main()

# addProcess  adiciona um processo passando key e valor
# removeProcess  remove um processo atraves da key
# getKey mostra apenas as key
# showInfo mostra todos processo e valor
# application() passando o paramentro dentro desse metodo voce executa # 
