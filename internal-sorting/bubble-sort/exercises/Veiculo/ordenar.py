from armazenar import armazenar

def ordenar(veiculos):
    for i in range(len(veiculos) - 1, 0, -1):
        for j in range(i):
            if veiculos[j].get_ano() < veiculos[j + 1].get_ano():
                temp = veiculos[j]
                veiculos[j] = veiculos[j + 1]
                veiculos[j + 1] = temp
    for v in veiculos:
        print(f"{v.get_ano()} - {v.get_marca()} - {v.get_cor()}")
    return veiculos
