import sys
from tech_news.scraper import get_tech_news
from tech_news.analyzer.ratings import top_5_categories
from tech_news.analyzer.search_engine import (
    search_by_title,
    search_by_date,
    search_by_category,
)


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
            data_user = input("Digite quantas notícias serão buscadas: ")
            get_tech_news(int(data_user))
        case "1":
            data_user = input("Digite o título: ")
            search_by_title(data_user)
        case "2":
            data_user = input("Digite a data no formato aaaa-mm-dd: ")
            search_by_date(data_user)
        case "3":
            data_user = input("Digite a categoria: ")
            search_by_category(data_user)
        case "4":
            top_5_categories()
        case "5":
            print("Encerrando script")
        case _:
            sys.stderr.write("Opção inválida\n")

    return input_user
