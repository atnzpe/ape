# home_screen.py
import flet as ft
import os


class HomeScreen(ft.UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page  # Referecia a página

    def build(self):
        return ft.Column(
            [
                ft.Text("TELA DE BOAS VINDAS"),
                ft.Text("Explore os encantos de Pernambuco!"),
                ft.ElevatedButton("Começar a Explorar", on_click=self.abrir_modal),
                ft.Text("INCLUIR UMA IMAGEM - EM BREVE"),
                # Sair do App
                ft.ElevatedButton("Sair", on_click=self.sair_do_app),      
            ],
            alignment="center",
            horizontal_alignment="center",
        )

    def abrir_modal(self, e):
        self.page.dialog = ft.AlertDialog(
            modal=True,
            title=ft.Text("Queres o que?"),
            content=ft.Column(
                [
                    ft.ElevatedButton("Encher o Buxo", on_click=lambda _: self.page.go("/food")),
                    ft.ElevatedButton("Dar uma Voltinha", on_click=lambda _: self.page.go("/destino")),
                    ft.ElevatedButton("Fechar", on_click=self.fechar_modal_preview),
                ]
            ),
            
        )

        self.page.dialog.open = True
        self.page.update()

    def fechar_modal_preview(self, e):
        """Fecha o modal de pré-visualização."""
        if self.page.dialog:
            self.page.dialog.open = False
            self.page.update()

    def sair_do_app(self, e):
        self.page.window_destroy()