import flet as ft

class DestinosScreen(ft.UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page


    def Build(self):
        return ft.Column(
            [
                ft.Text("Explore os Destinos!", style="headlineMedium"),
                ft.ElevatedButton("Voltar para Início", on_click=lambda _: self.page.go("/home")), 
            ],
            alignment="center",
            horizontal_alignment="center",
        )
