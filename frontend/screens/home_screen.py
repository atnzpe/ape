import flet as ft


def HomeScreen():

    return ft.Container(  # Container principal para centralizar tudo
        content=ft.Column(
            [
                

                # Container interno para o conteúdo centralizado
                ft.Container(
                    content=ft.Column(
                        [
                            ft.Text("Bem-vindo ao Apé!",
                                    theme_style=ft.TextThemeStyle.HEADLINE_MEDIUM),

                            # 2. Divisores com as cores da bandeira de Pernambuco
                            ft.VerticalDivider(
                                width=1, color='#AA4400'),  # Vermelho
                            ft.VerticalDivider(
                                width=1, color='#FFB511'),  # Amarelo
                            ft.VerticalDivider(
                                width=1, color='#00AD4A'),  # Verde
                            ft.Text("Explore os encantos de Pernambuco!"),

                            ft.ElevatedButton(
                                "Começar a Explorar", on_click=lambda _: print("Clicou no botão!")
                            ),
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    alignment=ft.alignment.center,  # Centraliza horizontal e verticalmente
                    theme_mode=ft.ThemeMode.DARK,  # Usando o tema escuro

                    expand=True,
                ),
            ],
            expand=True,
        ),
        alignment=ft.alignment.center,  # Centraliza tudo na tela
        expand=True,
    )
