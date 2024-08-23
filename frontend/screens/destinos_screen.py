import flet as ft

def DestinosScreen():
    return ft.Container(  # Container principal para centralizar tudo
        content=ft.Column(
            [
                

                # Container interno para o conteúdo centralizado
                ft.Container(
                    content=ft.Column(
                        [
                            ft.AppBar(title=ft.Text("Destinos - Apé")),
                            
                            ft.VerticalDivider(
                                width=1, color='#AA4400'),  # Vermelho
                            ft.VerticalDivider(
                                width=1, color='#FFB511'),  # Amarelo
                            ft.VerticalDivider(
                                width=1, color='#00AD4A'),  # Verde
                            ft.Text("Explore os encantos de Pernambuco!"),
                            ft.Text("Em breve, uma lista de lugares incríveis para você conhecer!", size=20)
                            
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    alignment=ft.alignment.center,  # Centraliza horizontal e verticalmente
                      # Usando o tema escuro

                    expand=True,
                ),
            ],
            expand=True,
        ),
        alignment=ft.alignment.center,  # Centraliza tudo na tela
        expand=True,
    )