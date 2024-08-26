from flet import *
import flet as ft

# Importe suas telas aqui
from screens.home_screen import HomeScreen
from screens.destinos_screen import DestinosScreen
from screens.food_screen import FoodScreen

def main(page: Page):
    page.title = "Apé - Seu Caminho em Pernambuco"
    page.theme_mode = ft.ThemeMode.DARK,
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER,
    page.vertical_alignment = ft.MainAxisAlignment.CENTER,

    def view_builder(route):
        page.views.clear()

        

        # Define a rota padrão para '/' e '/home'
        if page.route == "/":
            page.views.append(View(page.route, [HomeScreen(page)]))
        elif page.route == "/home":
            page.views.append(View(page.route, [HomeScreen(page)]))
        elif page.route == "/destinos":  # Correção de digitação
            page.views.append(View(page.route, [DestinosScreen(page)]))
        elif page.route == "/food":
            page.views.append(View(page.route, [FoodScreen(page)]))
        
        

        page.update()

    page.on_route_change = view_builder
    
    page.go(page.route)  # Define a rota inicial como '/home'

# Inicia o aplicativo Flet, definindo 'main' como a função principal
app(target=main, view=ft.WEB_BROWSER) 
