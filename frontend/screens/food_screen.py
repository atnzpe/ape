import flet as ft

class FoodScreen(ft.UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page

    def build(self):
        return ft.Column(
            [
                ft.Text("Delicie-se com a Gastronomia Local!", style="headlineMedium"),
                ft.ElevatedButton("Voltar para Início", on_click=lambda _: self.page.go("/home")), 
            ],
            alignment="center",
            horizontal_alignment="center",
        )