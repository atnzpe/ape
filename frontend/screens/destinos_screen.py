from flet import *
import flet as ft
from flet import View

class DestinoScreen(ft.UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page

    def build(self):

        return ft.Column(
            [
                ft.Text("TELA DE DESTINOS"),
                ft.Text("Explore Pernambuco!"),
                ft.Text("Em Contrução - Aqui terá uma lista dos locais para conhecer!"),
                ft.ElevatedButton("Quero encher o buxo",
                                  on_click=lambda _: self.page.go("/food")),
                ft.ElevatedButton("Voltar para Início",
                                  on_click=lambda _: self.page.go("/home")),
            ],
            
    
            alignment="center",
            horizontal_alignment="center",
        )