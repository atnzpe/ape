from flet import *
import flet as ft
from flet import View


class FoodScreen(ft.UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page

    def build(self):

        return ft.Column(
            [
                ft.Text("TELA FOOD"),
                ft.Text("Delicie-se com a Gastronomia de Pernambuco!"),
                ft.Text("Em Contrução - Aqui terá uma lista dos locais para comer!"),
                ft.ElevatedButton("Quero dar uma voltinha em Pernambuco",
                                  on_click=lambda _: self.page.go("/destino")),
                ft.ElevatedButton("Voltar para Início",
                                  on_click=lambda _: self.page.go("/home")),
            ],
            alignment="center",
            horizontal_alignment="center",
        )
