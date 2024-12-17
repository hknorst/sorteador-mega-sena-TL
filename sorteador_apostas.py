import random


def escolher_aleatorios(arquivo_entrada, quantidade=11):
    try:
        # Abre o arquivo e lê todas as linhas
        with open(arquivo_entrada, 'r') as file:
            linhas = [linha.strip() for linha in file if linha.strip()]

        # Garante que há linhas suficientes para escolher
        if len(linhas) < quantidade:
            raise ValueError(
                "O arquivo não possui apostas suficientes para a seleção.")

        # Seleciona 'quantidade' linhas aleatórias
        selecionados = random.sample(linhas, quantidade)

        # Exibe os resultados no terminal
        print("Números sorteados e apostadores escolhidos:")
        for item in selecionados:
            print(item)

        # Salva os resultados em um novo arquivo
        with open('resultado_apostas.txt', 'w') as file_saida:
            file_saida.write("Números sorteados e apostadores escolhidos:\n")
            for item in selecionados:
                file_saida.write(item + '\n')

        print("\nOs resultados foram salvos no arquivo 'resultado_apostas.txt'.")

    except FileNotFoundError:
        print(f"Erro: O arquivo '{arquivo_entrada}' não foi encontrado.")
    except ValueError as e:
        print(f"Erro: {e}")


# Caminho do arquivo de entrada
arquivo = 'apostas.txt'

# Chama a função
escolher_aleatorios(arquivo)
