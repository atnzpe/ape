from flet import *
import flet as ft
from flet import View

class FoodScreen(ft.Control):
    def __init__(self, page):
        super().__init__()
        self.page = page
        self.controls = []  # Adicione esta linha

    def build(self):
        
        return ft.Column(
            [
                ft.Text("Delicie-se com a Gastronomia Local!"),
                ft.ElevatedButton("Voltar para Início", on_click=lambda _: self.page.go("/home")), 
            ],
            alignment="center",
            horizontal_alignment="center",
        )

        return self