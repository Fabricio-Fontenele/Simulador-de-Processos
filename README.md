# Simulador de Processos

Este projeto é um simulador de algoritmos de escalonamento de processos, desenvolvido em Python. Ele permite criar processos com tempos de execução definidos e simular dois algoritmos clássicos de escalonamento: **FIFO (First-In-First-Out)** e **SJF (Shortest Job First)**.

## Funcionalidades

- Adição e remoção de processos com tempos de execução customizados.
- Simulação dos algoritmos FIFO e SJF, exibindo ordem de execução, tempo de espera, turnaround e médias.
- Interface simples via linha de comando, permitindo selecionar o algoritmo desejado.

## Estrutura dos Principais Arquivos

- `main.py`: Ponto de entrada do simulador. Cria processos de exemplo e chama a aplicação principal.
- `process.py`: Classe responsável por gerenciar a lista de processos (adicionar, remover, listar, exibir informações).
- `execução.py`: Função principal de interação, oferecendo ao usuário a escolha do algoritmo de escalonamento.
- `fifo.py`: Implementação do algoritmo FIFO.
- `sjf.py`: Implementação do algoritmo SJF.

## Como Usar

1. **Pré-requisito:** Ter Python 3 instalado.
2. **Clone o repositório:**
   ```bash
   git clone https://github.com/Fabricio-Fontenele/Simulador-de-Processos.git
   cd Simulador-de-Processos/simuladorProcessos
   ```
3. **Execute o simulador:**
   ```bash
   python main.py
   ```
4. **Siga as instruções no terminal para escolher o algoritmo e visualizar a simulação.**

## Exemplo de Uso

Ao rodar o programa, você poderá:

- Adicionar processos com nome e tempo.
- Escolher entre FIFO, SJF ou ambos para simulação.
- Visualizar tabelas com ordem de execução, tempo de espera e turnaround para cada algoritmo.

## Observações

- O código pode ser facilmente expandido para suportar outros algoritmos de escalonamento.
- Comentários no código explicam as principais funções de cada classe.

## Colaboradores

- [@Fabricio-Fontenele](https://github.com/Fabricio-Fontenele)
- [@Denisnascimentor](https://github.com/Denisnascimentor)
- [@oAnjophb](https://github.com/oAnjophb)

## Licença

Este projeto é livre para fins educacionais e acadêmicos.

---
