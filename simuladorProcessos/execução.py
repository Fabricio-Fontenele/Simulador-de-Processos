from fifo import Fifo
from sjf import SJF



def application(process):
        print("Escolha o algoritmo de escalonamento:")
        print(f"1 - FIFO\n2 - SJF\n3 - Ambos")
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
            print("Opção inválida!")
