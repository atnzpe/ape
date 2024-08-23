import flet as ft

def DestinosScreen():
    return ft.View(  # Alterado para ft.View
        route="/destinos",  # Rota da DestinosScreen 
        controls=[  # Lista de controles da tela
            ft.AppBar(title=ft.Text("Destinos - Apé")),
            ft.Text(
                "Em breve, uma lista de lugares incríveis para você conhecer!", size=20
            )
        ],
        #expand=True,
    )