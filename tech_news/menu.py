import sys


# Requisitos 11 e 12
def analyzer_menu():
    input_user = input(
        """Selecione uma das opções a seguir:
 0 - Popular o banco com notícias;
 1 - Buscar notícias por título;
 2 - Buscar notícias por data;
 3 - Buscar notícias por categoria;
 4 - Listar top 5 categorias;
 5 - Sair.
"""
    )
    match input_user:
        case "0":
            print("Digite quantas notícias serão buscadas")
        case "1":
            print("Digite o título:")
        case "2":
            print("Digite a data no formato aaaa-mm-dd:")
        case "3":
            print("Digite a categoria:")
        case _:
            sys.stderr.write("Opção inválida\n")

    return input_user
