import flet as ft
from screens.home_screen import HomeScreen
from screens.destinos_screen import DestinosScreen


def main(page: ft.Page):
    page.title = "Apé - Seu Caminho em Pernambuco"

    # Cria as instâncias das telas
    home_screen = HomeScreen()
    destinos_screen = DestinosScreen()

    # Adiciona as telas à página
    page.add(home_screen, destinos_screen)

    # Define a rota inicial (tela que será exibida primeiro)
    page.go(home_screen.route)


# Inicia o aplicativo Flet, definindo 'main' como a função principal
ft.app(target=main)
