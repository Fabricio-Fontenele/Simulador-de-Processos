from fifo import Fifo
from sjf import SJF


def application(process):

    while True:
        print("="*50)
        print(" "* 16,"Escolha a ação")
        print("1 - Executar Algoritmos\n2 - Adicionar Processo")
        print("3 - Remover Processo\n4 - Mostrar Informações dos Processos\n5 - Sair")
        print("="*50)

        action = input("Digite sua opção: ")

        if action == "1":
            run_algorithms(process)

        elif action == "2":
            while True:
                add_process(process)
                continueQuestion = input('Quer adicionar mais processos? (S/N): ').upper()

                if continueQuestion == 'S' or continueQuestion == "SIM":
                    continue
                else:
                    print("-" * 50)
                    break

        elif action == "3":
            remove_process(process)
        elif action == "4":
            show_process_info(process)
        elif action == "5":
            print(" "*17,"FIM DE EXECUÇÃO")
            break
        else:
            print("-" * 50)
            print(" " * 17, "Valor Inválido")
            print("-" * 50)

        contin = input("\nVolta para o menu ? [S/N]: ").upper()

        if contin == "S":
            continue
        elif contin == "N":
            print(f" " * 15, "FIM DE EXECUÇÃO")
            break
        else:
            print("Opção inválida.\n")

def run_algorithms(process):
    if not process.getKey():
        print("\nNão há processos para executar. \nAdicione processos primeiro.")
        return
    
    print("-"*50)
    print("Escolha o algoritmo de escalonamento:")
    print("1 - FIFO\n2 - SJF\n3 - Ambos")
    print("-"*50)

    option = input("Digite sua opção: ")

    if option == "1":
        fifo = Fifo(process)
        fifo.executar()
    elif option == "2":
        sjf = SJF(process)
        sjf.executar()
    elif option == "3":
        fifo = Fifo(process)
        fifo.executar()
        sjf = SJF(process)
        sjf.executar()
    else:
        print("-"*50)
        print(f" "*17,"Valor Invalido")
        print("-"*50)

def add_process(process):
    key = input("\nNome do processo a ser adicionado: ").upper()
    time = int(input("Tempo de execução do processo: "))
    process.addProcess(key, time)
    print(f"Processo ({key}): tempo {time} adicionado.")
    print("-"*50)

def remove_process(process):
    key = input("Digite a chave do processo a ser removido: ").upper()
    if process.removeProcess(key):
        print(f"Processo {key} removido.")
    else:
        print(f"Processo {key} não encontrado.")

def show_process_info(process):
    print("-"*50)
    process.showInfo()
