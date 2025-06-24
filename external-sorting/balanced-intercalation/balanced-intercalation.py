import os
import heapq

def create_runs(input, size): # definição da função que criará subarrays com partes (runs) do arquivo original
    runs = [] # array em que blocos (runs) do arquivo original serão armazenados

    with open(input, 'r', encoding='utf-8') as file: # abre/acessa o arquivo original em modo leitura (r) e termina a leitura de forma certa com with
        run = [] # variável/array temporário para armazenar os dados de cada run que vai dentro de "runs"
        c = 0 # inicia-se um contador em 0
        for line in file: # para cada linha do arquivo...
            run.append(line.strip()) # a string é recebida, dividida na quebra de linha
            c += 1 # contador vai contando em qual linha está
            if c == size: # quando o contador chegar na última linha
                run.sort() # a run será ordenada
                s_run = f"run_{len(runs)}.txt" # a run é salva numa arquivo com nome sequencial
                with open(s_run, 'w', encoding='utf-8') as writer: # o arquivo temporário criado na linha de cima é acessado em modo de escrita (w) e depois termina a escrita de modo certo com with
                    for s in run: # para cada string/nome na run
                        writer.write(f"{s}\n") # será escrito no arquivo temporário seguido de uma quebra de linha
                runs.append(s_run) # depois o array maior com todas as runs receberá o arquivo temporário
                run = [] # limpamos a "run" temporária já que esta/seu arquivo/dados já foi salvo no array "runs"
                c = 0 # o contador é zerado

        if run: # caso sobre strings na divisão por size (definido como 5)
            run.sort() # estas serão ordenadas...
            s_run = f"run_{len(runs)}.txt" # e inseridas em um arquivo temporário
            with open(s_run, 'w', encoding='utf-8') as reader: # acessa esse último arquivo temporário em modo escrita (w) e o fecha depois da maneira correta com with
                for s in run: # para cada string/nome na "run"
                    reader.write(f"{s}\n") # a string/nome será escrito seguido de uma quebra de linha
            runs.append(s_run) # arquivo temporário recebido pelo array maior "runs"

    return runs # "runs" é retornado para ser acessível fora da função

def intercalate_runs(runs, output): # definição da função que intercalará/juntará os arrays/arquivos
    files = [open(run, 'r', encoding='utf-8') for run in runs] # abre todos os arquivos "run" contidos em "runs"
    heap = [] # cria-se uma heap vazia

    for i, file in enumerate(files): # passa pela primeira linha de cada run
        line = file.readline() # lendo-a...
        if line: # e se for lida...
            heapq.heappush(heap, (line.strip(), i)) # é recebida pela heap em forma de tupla com string/nome e o índice da run de origem dentro de "runs"

    with open(output, 'w', encoding='utf-8') as writer: # abre o arquivo final em modo escritor
        while heap: # enquanto houver elementos na heap...
            m, o = heapq.heappop(heap) # a string/nome de menor valor (A < B < C, etc) e o índice de origem serão retornados por uma heap verdadeira e removidos da temporária
            writer.write(f"{m}\n") # o que será escrito no arquivo é a string/nome seguida por uma quebra de linha
            line = files[o].readline() # lê o próximo valor na origem (o)
            if line: # enquanto houver strings a serem lidas
                heapq.heappush(heap, (line.strip(), o)) # serão retornadas para a heap verdadeira a string/nome e o índice da run de origem

    for file in files: # cada arquivo temporário aberto...
        file.close() # será fechado
    for run in runs: # todas as "run" dentro de "runs"
        os.remove(run) # serão excluídas/removidas

def main():
    input = "unsorted-brazil-cities.txt" # referencia o arquivo de origem
    output = "sorted-brazil-cities.txt" # referencia o arquivo de destino
    size = 5 # define o tamanho de cada "run"

    runs = create_runs(input, size) # chama a função para criar as runs
    intercalate_runs(runs, output) # chama a função para ordenar e juntar as runs

if __name__ == "__main__":
    main()

# encoding='utf-8' é necessário apenas para dados em idiomas que possuem acentuação, como o português
