# Importa a biblioteca Flet
import flet as ft

# Importa a tela HomeScreen do módulo screens.home_screen
from screens.home_screen import HomeScreen  

#Importa a Tela de Destinos do modulo screens.destinos_screen
from screens.destinos_screen import DestinosScreen

# Define a função principal do aplicativo
def main(page: ft.Page):
    # Define o título da página que será exibido na aba do navegador
    page.title = "Apé - Seu Caminho em Pernambuco_Main"  

    # Cria uma instância da tela HomeScreen
    home_screen = HomeScreen()

    #Cria a instacia da Tela DestinosScreen
    destinos_screen = DestinosScreen 

    #Defina as rotas para cada Tela
    page.views = [home_screen, destinos_screen]

    #Defina a rota incial
    page.go(home_screen.route)

# Inicia o aplicativo Flet, definindo 'main' como a função principal
ft.app(target=main)
