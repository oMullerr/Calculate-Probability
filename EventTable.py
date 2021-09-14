import random  # Biblioteca Built In do Python para geração de números aleatórios

from prettytable import PrettyTable  # Biblioteca Third-Party para formatação de tabelas

letra1 = ['q', 'w', 'x', 'z']  # Primeiro vetor de possíveis letras
letra2 = ['a', 'i', 'u']  # Segundo vetor de possíveis letras
letra3 = ['c', 'f', 'p']  # Terceiro vetor de possíveis letras
letra4 = ['e', 'o']  # Quarto vetor de possíveis letras


def getEspacoAmostral() -> dict:  # Gerador do espaço amostral

    all_combinations = {}  # Todas as combinações de letras em um dicionário

    for i in letra1:
        for j in letra2:
            for k in letra3:
                for l in letra4:
                    key = f"{i}{j}{k}{l}"  # Loops aninhados para combinar todas as letras

                    all_combinations[key] = 0  # Todas as palavras recebem frequência 0

    return all_combinations  # Retorna o dicionário


def geradorPalavras(n, universe) -> dict:  # Gerador de palavras aleatórias

    # Shallow copy da coleção original para não interferirem entre si
    total_resultados = universe.copy()

    # Aqui nós fornecemos a quantidade de sorteios que serão realizados
    for i in range(n):

        l1 = random.randint(0, len(letra1) - 1)  # Inteiros aleatórios
        l2 = random.randint(0, len(letra2) - 1)  # para acessar as
        l3 = random.randint(0, len(letra3) - 1)  # posições dos vetores
        l4 = random.randint(0, len(letra4) - 1)  # de caracteres.

        # Concatenação das letras aleatórias em uma palavra
        palavra = letra1[l1] + letra2[l2] + letra3[l3] + letra4[l4]
        try:
            # Aqui nós tentamos incrementar a ocorrência de uma palavra
            # se ela já existir no dicionário de palavras aleatórias
            total_resultados[palavra] += 1
        except:
            # Em caso de falha, nós atualizamos o dicionário com uma nova ocorrência
            total_resultados.update({palavra: 1})
    return total_resultados  # Retorna o dicionário


def normalizeData(collection, universe) -> list:  # Normalizador de dados para formatação adequada

    normalized = []  # Lista que armazena linhas de uma matriz de dados

    for e in universe:  # Para cada elemento do espaço amostral

        # Nós criamos uma linha com todos os
        # elementos daquele nível das sublistas
        row = [e] + list(map(lambda coll: coll[e], collection))  # Iterando com o map()

        normalized.append(row)  # Adicionando cada nova linha na lista "normalizada"

    return normalized  # Retornando a "matriz" de dados


def gerarTabela():
    universe = getEspacoAmostral()  # Criando um objeto que representa o espaço amostral

    frequencies = [72, 216, 720, 2160, 7200, 72000]  # Tamanho dos testes realizados

    sorteios = []  # Lista que guardará todos os testes realizados

    # Gerando os sorteios aleatórios de acordo com a quantidade de sorteios
    for i in frequencies:
        teste = geradorPalavras(i, universe)  # Guardamos os resultados em 'teste'
        sorteios.append(teste)  # Colocamos este resultado em uma lista

    # Criando uma matriz de dados normalizados através da função 'normalizeData'
    matrix = normalizeData(sorteios, universe)

    # Esta linha é puramente para a formatação dos headers da tabela
    headers = ["Palavra"] + frequencies

    # Utilizando a biblioteca 'prettytable' para criar uma tabela
    table = PrettyTable(headers, title="Trabalho A15", align="l", valign="m")

    # Adicionando todas as linhas de acordo com os dados da matriz
    for row in matrix:
        table.add_row(row)

    # Adicionando a coluna de resultados esperados
    esperado = [f"sorteios/{len(universe)}" for i in range(len(matrix))]
    table.add_column(fieldname="Esperado", valign="m", column=esperado)

    return table  # Retornando a tabela


print(gerarTabela())
