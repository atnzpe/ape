from flet import *
import flet as ft

# Importe suas telas aqui
from screens.home_screen import HomeScreen
from screens.destinos_screen import DestinosScreen
from screens.food_screen import FoodScreen

def main(page: Page):
    page.title = "Apé - Seu Caminho em Pernambuco"
    page.theme_mode = ft.ThemeMode.DARK  # Se quiser manter o tema escuro

    def view_builder(route):
        page.views.clear()

        if page.route == "/":  # Rota inicial
            page.views.append(View("/", [HomeScreen(page)]))

        elif page.route == "/home": 
            page.views.append(View("/home", [HomeScreen(page)]))

        elif page.route == "/destinos":  # Correção de digitação
            page.views.append(View("/destinos", [DestinosScreen(page)])) 
        
        elif page.route == "/food": 
            page.views.append(View("/food", [FoodScreen(page)]))
        
        page.update()

    page.on_route_change = view_builder
    page.go(page.route)

app(target=main) 
