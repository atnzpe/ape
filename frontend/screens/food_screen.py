import flet as ft


def FoodScreen():
    return ft.Column(
        [
            ft.AppBar(title=ft.Text("Hora de Encher o Bucho - Apé")),
            ft.Text(
                "Em breve, uma lista de lugares incríveis para você conhecer!", size=20)
        ],
        expand=True,
    )