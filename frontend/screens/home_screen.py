# home_screen.py
import flet as ft



class HomeScreen(ft.UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page  # Salve a referência à página

    def build(self):
        return ft.Column(
            [
                ft.Text("Bem-vindo ao Ape Turismo!"),
                ft.ElevatedButton("Começar a Explorar", on_click=self.abrir_modal),
            ],
            alignment="center",
            horizontal_alignment="center",
            
        )

    def abrir_modal(self, e):
        self.page.dialog = ft.AlertDialog(
            modal=True,
            title=ft.Text("Para onde vamos?"),
            content=ft.Column(
                [
                    ft.ElevatedButton("Encher o Buxo", on_click=lambda _: self.page.go("/food")),
                    ft.ElevatedButton("Dar uma Voltinha", on_click=lambda _: self.page.go("/destinos")),
                    ft.ElevatedButton("Voltar", on_click=lambda _: self.page.go("/home")),

                ]
            ),
        )
        self.page.dialog.open = True
        self.page.update()
