from armazenar import armazenar
from ordenar import ordenar
from Veiculo import Veiculo

def main():
    veiculos = armazenar(Veiculo)
    ordenar(veiculos)

if __name__ == '__main__':
    main()
