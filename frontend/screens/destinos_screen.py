import flet as ft


def DestinosScreen():
    return ft.Column(
        [
            ft.AppBar(title=ft.Text("Destinos - Apé")),
            ft.Text(
                "Em breve, uma lista de lugares incríveis para você conhecer!", size=20)
        ],
        expand=True,
    )
