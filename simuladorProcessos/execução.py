from fifo import Fifo
from sjf import SJF
from process import Process

def application(process):
    while True:
        
        print("-"*50)
        print("Escolha o algoritmo de escalonamento:")
        print(f"1 - FIFO\n2 - SJF\n3 - Ambos")
        print("-"*50)
        opcao = input("Digite sua opção: ")
        if opcao == "1":
            fifo = Fifo(process)
            fifo.executar()
        elif opcao == "2":
            sjf = SJF(process)
            sjf.executar()
        elif opcao == "3":
            fifo = Fifo(process)
            fifo.executar()
            sjf = SJF(process)
            sjf.executar()
        else:
            print("-"*50)
            print(f" "*17,"Valor Invalido")
            print("-"*50)

        contin = input("quer continuar ? [S/N]: ").upper().split()

        if contin == "N":
            print(f" "*15,"FIM DE EXECUÇÃO")
            break
        elif contin == "S":
            continue
        else:
            print("Opção inválida. Digite apenas S ou N.\n")
