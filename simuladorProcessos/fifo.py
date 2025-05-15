from process import Process

class Fifo:
    def __init__(self, processos: Process):
        self.processos = processos

    def executar(self):
        print("\nResultado da simulação (FIFO):")
        print("-"* 50)
        print("Processo | Ordem | Execução | Espera | Turnaround")
        print("-"* 50)

        tempo_espera_total = 0
        tempo_turnaround_total = 0
        tempo_espera = 0
        ordem = 1

        for chave in self.processos.getKey():
            tempo_exec = self.processos.listProcesses[chave]
            turnaround = tempo_espera + tempo_exec

            print(f"{chave:^8} | {ordem:^5} | {tempo_exec:^8} | {tempo_espera:^6} | {turnaround:^10}")
            tempo_espera_total += tempo_espera
            tempo_turnaround_total += turnaround

            tempo_espera += tempo_exec
            ordem += 1

        n = len(self.processos.getKey())
        print("-"* 50)
        print(f"Média do tempo de espera: {tempo_espera_total / n:.2f}")
        print(f"Média do tempo de turnaround: {tempo_turnaround_total / n:.2f}")