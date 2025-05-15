from process import Process

class SJF:
    def __init__(self, processos: Process):
        self.processos = processos

    def executar(self):
        print("\nResultado da simulação (SJF):")
        print("-"* 50)
        print("Processo | Ordem | Execução | Espera | Turnaround")
        print("-"* 50)

        ordered_processes = sorted(self.processos.listProcesses.items(), key=lambda item: item[1])

        total_waiting_time = 0
        total_turnaround_time = 0
        waiting_time = 0
        order = 1

        for key, temp_exec in ordered_processes:
            turnaround = waiting_time + temp_exec

            print(f"{key:^8} | {order:^5} | {temp_exec:^8} | {waiting_time:^6} | {turnaround:^10}")
            total_waiting_time += waiting_time
            total_turnaround_time += turnaround

            waiting_time += temp_exec
            order += 1

        n = len(ordered_processes)
        print("-"* 50)
        print(f"Média do tempo de espera: {total_waiting_time / n:.2f}")
        print(f"Média do tempo de turnaround: {total_turnaround_time / n:.2f}")
