import json
import geopy.distance

ListaDeFuncoes = []
ListaDeTipos = ["Plasticos", "Metais Ferrosos", "Papel", "Vidro", "Pilhas e baterias"]

arquivo = open("db\database.json", )

dados = json.load(arquivo)

listaMateriais = dados["TiposDeMateriais"]

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
    print("===" * 20)
    print("Nosso sistema funciona da seguinte maneira: \n")
    print("Você escolhe uma função do nosso menu, \n")
    print("Para receber as informaões que desejar. \n")
    print("Algumas funções precisam saber o tipo de \n")
    print("material que você deseja reciclar")
    print("===" * 20)

def pontoDeColeta(): # Lista todos os nossos pontos de coleta

    for ponto in ListaDeTipos:

        print(ponto)

        for tipo in listaMateriais[ponto]: 

            print(tipo)

def filtrarPontosDeColeta(): # Filtra os pontos de coleta pelo tipo

    material = ""

    menuTipos()

    number = int(input("Qual tipo de material você quer reciclar ? "))

    for i in range(0, 5):

        if number == i + 1:

            material = ListaDeTipos[i]

            break

    for item in listaMateriais[material]:

        print(item)

def localizarMaisProximo(): # Localiza o ponto de coleta mais proximo pelas cordenadas

    Longitude = float(input("Informe a Longitude: "))
    Latitude = float(input("Informe a Latitude: "))

    menuTipos()

    TipoDeLixo = int(input("Informe a Tipo de Lixo: ")) - 1

    listaLocais = dados["TiposDeMateriais"][ListaDeTipos[TipoDeLixo]]

    usuario_coords_1 = [Longitude, Latitude]
    mais_proxima_coords_2 = []

    if len(listaLocais) > 1:

        distance = 0
        distanceAtual = 0
        key_distance = False

        for item in listaLocais:

            mais_proxima_coords_2.append(item["Longitude"])
            mais_proxima_coords_2.append(item["Latitude"])

            distanceAtual = geopy.distance.GeodesicDistance(usuario_coords_1, mais_proxima_coords_2).km

            if key_distance == False or distance > distanceAtual:

                key_distance = True

                distance = distanceAtual

            mais_proxima_coords_2 = []
        
        key_distance = False

        print(distance)

    else:

        print(listaLocais)

ListaDeFuncoes = [comoReciclar, pontoDeColeta, filtrarPontosDeColeta, localizarMaisProximo]

continuacao = "s"

def main(continuacao):

    while continuacao != "n":

        menu()
        filtrarFuncao(perguntarFuncao())

        print("===" * 20)
        print('Digite "n" para parar o programa')
        continuacao = input("Dejesa continuar ? ")
        print("===" * 20)

if __name__ == "__main__":

    main(continuacao)