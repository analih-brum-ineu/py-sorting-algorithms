from Veiculo import Veiculo

def armazenar(veiculos):
    veiculos = []
    for i in range (3):
        marca = input('Marca: ')
        cor = input('Cor: ')
        ano = int(input('Ano: '))
        veiculos.append(Veiculo(marca, cor, ano))
    return veiculos
