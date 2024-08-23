# Importa a biblioteca Flet
import flet as ft
from routes import app_routes, view_builder


# Define a função principal do aplicativo
def main(page: ft.Page):
    # Define o título da página que será exibido na aba do navegador
    page.title = "Apé - Seu Caminho em Pernambuco"  # Configurando o gerenciador de rotas
    page.on_route_change = view_builder
    page.go(page.route)
    

    # Adiciona a instância da tela HomeScreen à página principal
    #page.add(home_screen) 

# Inicia o aplicativo Flet, definindo 'main' como a função principal
ft.app(target=main,route_change=view_builder,routes=app_routes)