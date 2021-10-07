import json

ListaDeFuncoes = []

arquivo = open("aps-reciclagem\db\database.json", )

dados = json.load(arquivo)

def menu():
    print("===" * 20)
    print("Escolha uma função")
    print(" 1. Informação de como reciclar\n 2. Listar pontos de coleta\n 3. Filtrar e Listar pontos de coleta\n 4. Localizar o ponto mais proximo")
    print("===" * 20)

def perguntarFuncao():

    funcao = int(input("Qual função você dejesa usar ? "))

    return funcao

def filtrarFuncao(index):

    ListaDeFuncoes[index - 1]()

def comoReciclar():
    pass

def pontoDeColeta():
    
    print(dados)

def filtrarPontosDeColeta():
    pass

def localizarMaisProximo():
    pass


ListaDeFuncoes = [comoReciclar, pontoDeColeta, filtrarPontosDeColeta, localizarMaisProximo]

menu()
filtrarFuncao(perguntarFuncao())



# f = open("aps-reciclagem\db\database.json", )

# dados = json.load(f)

# print(dados["TiposDeMateriais"]["Plasticos"])
    