from process import Process

class Fifo:
    def __init__(self, process: Process):
        self.process = process

    def executar(self):
        print("\nResultado da simulação (FIFO):")
        print("-"* 50)
        print("Processo | Ordem | Execução | Espera | Turnaround")
        print("-"* 50)

        total_waiting_time = 0
        temp_turnaround_total = 0
        waiting_time = 0
        order = 1

        for key in self.process.getKey():
            temp_exec = self.process.listProcesses[key]
            turnaround = waiting_time + temp_exec

            print(f"{key:^8} | {order:^5} | {temp_exec:^8} | {waiting_time:^6} | {turnaround:^10}")
            total_waiting_time += waiting_time
            temp_turnaround_total += turnaround

            waiting_time += temp_exec
            order += 1

        n = len(self.process.getKey())
        print("-"* 50)
        print(f"Média do tempo de espera: {total_waiting_time / n:.2f}")
        print(f"Média do tempo de turnaround: {temp_turnaround_total / n:.2f}")