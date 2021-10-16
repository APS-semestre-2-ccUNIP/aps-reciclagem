import json

ListaDeFuncoes = []
ListaDeTipos = ["Plasticos", "Metais Ferrosos", "Papel", "Vidro", "Pilhas e baterias"]

arquivo = open("db\database.json", )

dados = json.load(arquivo)

def menu():
    print("===" * 20)
    print("Escolha uma função")
    print(" 1. Informação de como reciclar\n 2. Listar pontos de coleta\n 3. Filtrar e Listar pontos de coleta\n 4. Localizar o ponto mais proximo")
    print("===" * 20)

def menuTipos():
    print("===" * 20)
    print("Escolha um tipo")
    print(" 1. Plastico\n 2. Metais Ferrosos\n 3. Papel\n 4. Vidro\n 5. Pilhas e baterias")
    print("===" * 20)

def perguntarFuncao():

    funcao = int(input("Qual função você dejesa usar ? "))

    return funcao

def filtrarFuncao(index):

    ListaDeFuncoes[index - 1]()

def comoReciclar(): # Mostra um texto explicando como reciclar os itens
    pass

def pontoDeColeta(): # Lista todos os nossos pontos de coleta
    
    for i in range(0, 5):

        print(f'{dados["TiposDeMateriais"][ListaDeTipos[i]]}')

def filtrarPontosDeColeta(): # Filtra os pontos de coleta pelo tipo

    material = ""

    menuTipos()

    number = int(input("Qual tipo de material você quer reciclar ? "))

    for i in range(0, 5):

        if number == i + 1:

            material = ListaDeTipos[i]

            break
    
    for i in range(0, len(dados["TiposDeMateriais"][material])):

        print(f'{dados["TiposDeMateriais"][material][i]}')

def localizarMaisProximo(): # Localiza o ponto de coleta mais proximo pelas cordenadas
    pass

ListaDeFuncoes = [comoReciclar, pontoDeColeta, filtrarPontosDeColeta, localizarMaisProximo]

menu()
filtrarFuncao(perguntarFuncao())



# f = open("aps-reciclagem\db\database.json", )

# dados = json.load(f)

# print(dados["TiposDeMateriais"]["Plasticos"])
    