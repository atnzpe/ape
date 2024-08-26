from flet import *
import flet as ft
from flet import View


class DestinosScreen(ft.Control):
    def __init__(self, page):
        super().__init__()
        self.page = page

    def build(self):
            
        return ft.Column(
            [
                ft.Text("Explore os Destinos!"),
                ft.ElevatedButton("Voltar para Início",
                                    on_click=lambda _: self.page.go("/home")),
            ],
            alignment="center",
            horizontal_alignment="center",
        )
        
        return self
