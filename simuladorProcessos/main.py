from process import Process
from execução import application

def main():
    processo = Process()
    application(processo)

if __name__ == "__main__":
    main()

# addProcess  adiciona um processo passando key e valor
# removeProcess  remove um processo atraves da key
# getKey mostra apenas as key
# showInfo mostra todos processo e valor
# application() passando o paramentro dentro desse metodo voce executa # 
