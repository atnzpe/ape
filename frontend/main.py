from flet import *
import flet as ft
from flet import View

# Importe suas telas aqui (substitua pelos nomes corretos dos arquivos)
from screens.home_screen import HomeScreen
from screens.destinos_screen import DestinosScreen
from screens.food_screen import FoodScreen


# Define a função principal do aplicativo
def main(page: Page):

    # Define o título da página que será exibido na aba do navegador
    # Configurando o gerenciador de rotas
    page.title = "Apé - Seu Caminho em Pernambuco"

    page.theme_mode = ft.ThemeMode.DARK

    def view_builder(route):
        page.views.clear()
        
        page.views.append(View("/",[ElevatedButton("Partiu Pernambuco!",
                                   on_click=lambda _: [HomeScreen(page)]),
                ]
            )
        )

       
        
        if page.route == "/destino":
            page.views.append(View("/destinos", [DestinosScreen(page)]))
        
        elif page.route == "/food":
            page.views.append(View("/food", [FoodScreen(page)]))
        
        
        page.update()
    page.on_route_change = view_builder
    page.go(page.route)


# Inicia o aplicativo Flet, definindo 'main' como a função principal
app(target=main)
