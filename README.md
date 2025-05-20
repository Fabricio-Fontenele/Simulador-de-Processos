# Simulador de Processos

Este projeto é um simulador de algoritmos de escalonamento de processos, desenvolvido em Python. Ele permite criar processos com tempos de execução definidos e simular dois algoritmos clássicos de escalonamento: **FIFO (First-In-First-Out)** e **SJF (Shortest Job First)**.

## Funcionalidades

- Adição e remoção de processos com tempos de execução customizados.
- Simulação dos algoritmos FIFO e SJF, exibindo ordem de execução, tempo de espera, turnaround e médias.
- Interface interativa via linha de comando para:
    - Adicionar novos processos.
    - Remover processos existentes.
    - Mostrar informações detalhadas dos processos.
    - Escolher executar os algoritmos FIFO, SJF ou ambos.

## Estrutura dos Principais Arquivos

- `main.py`: Ponto de entrada do simulador. Cria processos de exemplo e chama a aplicação principal.
- `process.py`: Classe responsável por gerenciar a lista de processos (adicionar, remover, listar, exibir informações).
- `execução.py`: Função principal de interação, oferecendo ao usuário a escolha do algoritmo de escalonamento.
- `fifo.py`: Implementação do algoritmo FIFO.
- `sjf.py`: Implementação do algoritmo SJF.

## Como Usar

1.  **Pré-requisito:** Ter Python 3 instalado.
2.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/Fabricio-Fontenele/Simulador-de-Processos.git](https://github.com/Fabricio-Fontenele/Simulador-de-Processos.git)
    cd Simulador-de-Processos/simuladorProcessos
    ```
3.  **Execute o simulador:**
    ```bash
    python main.py
    ```
4.  **Siga as instruções no terminal:**
    - Escolha a ação desejada no menu (Executar Algoritmos, Adicionar Processo, Remover Processo, Mostrar Informações, Sair).
    - Se escolher "Executar Algoritmos", selecione o algoritmo (FIFO, SJF ou Ambos).
    - Se escolher "Adicionar Processo", insira o nome e o tempo de execução do processo.

## Exemplo de Uso

Ao rodar o programa, você poderá:

- Adicionar múltiplos processos com nomes e tempos de execução.
- Escolher entre FIFO, SJF ou ambos para simulação.
- Visualizar tabelas detalhadas com ordem de execução, tempo de espera e turnaround para cada algoritmo.
- A qualquer momento, você pode voltar ao menu principal para adicionar/remover processos ou executar os algoritmos novamente.

Por exemplo:
1.  Você pode adicionar os processos A (tempo 5), B (tempo 2) e C (tempo 8).
2.  Depois, escolher executar o algoritmo FIFO para ver os resultados.
3.  Em seguida, voltar ao menu e executar o algoritmo SJF para comparar os resultados.
4.  Finalmente, você pode usar a opção de "Mostrar Informações dos Processos" para revisar os processos que foram adicionados.

## Observações

- O código pode ser facilmente expandido para suportar outros algoritmos de escalonamento.
- Comentários no código explicam as principais funções de cada classe.

## Colaboradores

- [@Fabricio-Fontenele](https://github.com/Fabricio-Fontenele)
- [@Denisnascimentor](https://github.com/Denisnascimentor)
- [@oAnjophb](https://github.com/oAnjophb)


