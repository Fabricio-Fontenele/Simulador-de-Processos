from fifo import Fifo
from sjf import SJF



def application(processo):
        print("Escolha o algoritmo de escalonamento:")
        print(f"1 - FIFO\n2 - SJF\n3 - Ambos")
        opcao = input("Digite sua opção: ")

        if opcao == "1":
            fifo = Fifo(processo)
            fifo.executar()
        elif opcao == "2":
            sjf = SJF(processo)
            sjf.executar()
        elif opcao == "3":
            fifo = Fifo(processo)
            fifo.executar()
            sjf = SJF(processo)
            sjf.executar()
        else:
            print("Opção inválida!")