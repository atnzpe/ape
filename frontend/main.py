# Importa a biblioteca Flet
import flet as ft

# Importa a tela HomeScreen do módulo screens.home_screen
from screens.home_screen import HomeScreen  

#Importa a Tela de Destinos do modulo screens.destinos_screen
from screens.destinos_screen import DestinosScreen

# Define a função principal do aplicativo
def main(page: ft.Page):
    # Define o título da página que será exibido na aba do navegador
    page.title = "Apé - Seu Caminho em Pernambuco"
    #page.theme_mode=ft.ThemeMode.DARK

     # 1. Instancie as telas (crie os objetos)
    home_screen = HomeScreen()  
    destinos_screen = DestinosScreen()

    # 2. Agora adicione as instâncias à página
    page.add(home_screen)  

    page.go(home_screen.route)

# Inicia o aplicativo Flet, definindo 'main' como a função principal
ft.app(target=main)
