import heapq

def create_s_chunks(input, size): # definição da função que criará os chunks, recebe o arquivo original e a quantia de nomes que cada chunk receberá
    chunks = [] # uma variável chamada "chunks" recebe um array vazio
    with open(input, 'r') as file: # abre o arquivo original referenciado em modo leitura (r), encerra corretamente após a leitura com with
        chunk = [] # uma variável temporária chamada "chunk" recebe cada parte em que os dados são quebrados
        for line in file: # loop for para passar por cada linha do arquivo referenciado
            chunk.append(line.strip()) # "chunk" vai recebendo cada string, quebrando-as após uma quebra de linha
            if len(chunk) == size: # se o tamanho de chunk chegar ao limite estabelecido...
                chunk.sort() # chunk será ordenado pela função padrão da linguagem sort()
                chunks.append(chunk) # este primeiro chunk ordenado será recebido no array "chunks", ou seja, um array armazenado dentro de outro
                chunk = [] # como o chunk anterior foi sorteado e armazenado, agora declaramos que "chunk" volta a ser um array vazio/limpo

        if chunk: # caso sobre strings na hora da divisão de chunks...
            chunk.sort() # estes serão ordenados...
            chunks.append(chunk) # e recebidos pelo array "chunks"

    return chunks # array "chunks" é retornado para ser utilizado fora deste primeiro ambiente

def merge_s_chunks(chunks, output): # definição da função que unirá os chunks ordenados e acessará/escreverá os chunks unidos em um arquivo final
    heap = [(chunk[0], i, 0) for i, chunk in enumerate(chunks) if chunk] # variável heap (fila de prioridade mínima) recebe tuplas, cada string dos chunks será recebida como um valor (o nome), de qual "chunk" dentro do "chunks" veio a string (i de "chunks") e a posição dentro dos arrays "chunk" que é 0 pois sempre começa-se do primeiro
    heapq.heapify(heap) # tranforma a variável "heap" em uma heap verdadeira utilizando uma função importada da biblioteca heapq

    with open(output, 'w') as file: # abre o arquivo final no modo escrita (w), e termina a escrita corretamente com with
        while heap: # loop para enquanto existirem elementos na heap...
            value, c_index, e_index = heapq.heappop(heap) # o elemento/tupla de menor valor da heap (A < B < C ...) é recebido e quebrado em tuplas com três variáveis cada, variáveis essas que recebem os três dados (nome, índice no "chunks", índice no "chunk"), depois removido e retornado ao mesmo tempo através do heappop()
            file.write(value + '\n') # escreve o valor (nome) com uma quebra de linha em seguida

            if e_index + 1 < len(chunks[c_index]): # assegura que estamos dentro do array "chunks"...
                next_element = chunks[c_index][e_index + 1] #  se houver, acessa o próximo nome do array "chunks"...
                heapq.heappush(heap, (next_element, c_index, e_index + 1)) # e o adiciona à heap...

def external_merge_sort(input, output, size): # definição da função mergesort externo
    chunks = create_s_chunks(input, size) # array "chunks" recebe a chamada da função "create_sorted_chunks"
    merge_s_chunks(chunks, output) # chamada da função "merge-sorted-chunks", array "chunks" é combinado e escrito no arquivo final

def main():
    input = "unsorted-first-names.txt"  # caminho/nome do arquivo original
    output = "sorted-first-names.txt"  # caminho/nome do arquivo final
    size = 100 # define o tamanho de cada chunk temporário dentro do array "chunk"

    external_merge_sort(input, output, size) # chamada da função mergesort externo e passagem dos parâmetros

if __name__ == "__main__":
    main()
