# Importa a biblioteca Flet
import flet as ft

# Importa a tela HomeScreen do módulo screens.home_screen
from screens.home_screen import HomeScreen
from screens.destinos_screen import DestinosScreen
from screens.food_screen import FoodScreen

# Define a função principal do aplicativo
def main(page: ft.Page):
    # Define o título da página que será exibido na aba do navegador
    page.title = "Apé - Seu Caminho em Pernambuco_Main"  

    # Cria uma instância da tela HomeScreen
    home_screen = HomeScreen()
    destino_screen = DestinosScreen()
    food_screen = FoodScreen()

    # Adiciona a instância da tela HomeScreen à página principal
    page.add(home_screen) 

# Inicia o aplicativo Flet, definindo 'main' como a função principal
ft.app(target=main)