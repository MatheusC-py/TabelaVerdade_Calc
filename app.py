import os

def coletarEntradas(funcao):
    entradas = set()
    for i in funcao:
        verificador = i.isalpha()
        if verificador == True:
            entradas.add(i)
    entradas = sorted(entradas)
    return entradas

def criarTabela(entradas):
    colunas = len(entradas)
    linhas = 2**colunas
    matriz = []
    alternador = colunas 
    alternar = False
    
    for n in range(colunas):
        linha = [0]*linhas
        matriz.append(linha)
    
    for c in range(colunas):
        alternador = alternador - 1
        for l in range(linhas):
            if l % (2**alternador) == 0:
                if alternar:
                    alternar = False
                else:
                    alternar = True
            if alternar == True: 
                matriz[c][l] = 0
            else:
                matriz[c][l] = 1
    return matriz

def avaliarExpressao(funcao, contexto):
    funcao = funcao.replace("*", " and ")
    funcao = funcao.replace(".", " and ")
    funcao = funcao.replace("+", " or ")
    funcao = funcao.replace("!=", " ^ ")
    funcao = funcao.replace("!", " not ")

    try:
        resultado = eval(funcao, {}, contexto)
        return int(resultado)
    except Exception as e:
        print(f"Erro ao avaliar a expressão: {e}")
        return None

def fazerOperacao(tabela, funcao, entradas):
    resultados = []
    for linha in zip(*tabela):
        contexto = dict(zip(entradas, linha))
        resultado = avaliarExpressao(funcao, contexto)
        resultados.append(resultado)
    return resultados

def imprimirTabela(entradas, funcao, tabela, resultado):
    print("=-="*20)
    print("A função que foi utilizada foi: {}\n\n".format(funcao))
    
    print(f"{' | '.join(entradas)} | Resultado")
    print("-" * (len(entradas) * 4 + 11))
    for i in range(len(tabela[0])):
        print(" | ".join(str(tabela[j][i]) for j in range(len(entradas))), f"| {resultado[i]}")

def instrucoes():
    mensagem = """
    BEM VINDO À CALCULADORA DE TABELA VERDADE!
    
    Nesta calculadora, você pode utilizar operações lógicas para gerar tabelas verdade.
    As operações suportadas são:
    * AND ( * ou . )
    * OR ( + ) 
    * NOT ( ! )
    * XOR (ou exclusivo representado por !=)

    Exemplos de expressões:
    * A * B + C (equivale a: A AND B OR C)
    * !A + B (equivale a: NOT A OR B)
    * A != B (equivale a: A XOR B)
    
    A calculadora criará a saída da expressão em tabela verdade.
    """
    print(mensagem)




def main():
    while True:
        print("=-="*20)
        print("CRIADOR DE TABELA VERDADE!")
        print("1.INICIAR\n2.INSTRUÇÕES\n3.SAIR")
        print("=-="*20)
        controlador = int(input("Selecione uma opção: "))
        os.system('cls')

        if controlador == 1:
            funcao = input("Descreva a função para criar a tabela: ")
            funcao = funcao.strip()
            entradas = coletarEntradas(funcao)
            tabela = criarTabela(entradas)
            resultado = fazerOperacao(tabela, funcao, entradas)
            imprimirTabela(entradas, funcao, tabela, resultado)
        elif controlador == 2:
            instrucoes()
        elif controlador == 3:
            break

main()