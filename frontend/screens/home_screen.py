import flet as ft


def HomeScreen():
    # 1. Criando um tema personalizado com base próxima ao azul desejado
    #page.theme_data = ft.ThemeData(color_scheme_seed=ft.colors.BLUE_700)
    #page.theme_data.color_scheme.primary = ft.colors.from_hex("#3155A4")

    # 2. Usando ft.View como componente principal da tela
    return ft.View(
        route="/",  # Rota da HomeScreen (raiz do aplicativo)
        controls=[  # Lista de controles (widgets) da tela
            ft.Container(  # Container para centralizar o conteúdo
                content=ft.Column(
                    [
                        ft.Text("Bem-vindo ao Apé!",
                                theme_style=ft.TextThemeStyle.HEADLINE_MEDIUM),

                        # Divisores com as cores da bandeira de Pernambuco
                        ft.VerticalDivider(
                            width=1, color='#AA4400'),  # Vermelho
                        ft.VerticalDivider(
                            width=1, color='#FFB511'),  # Amarelo
                        ft.VerticalDivider(width=1, color='#00AD4A'),  # Verde
                        ft.Text("Explore os encantos de Pernambuco!"),

                        ft.ElevatedButton(
                            "Começar a Explorar", on_click=lambda _: print("Clicou no botão!")
                        ),
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                alignment=ft.alignment.center,  # Centraliza o conteúdo do Container
                #theme_mode=ft.ThemeMode.DARK,  # Aplica o tema escuro ao Container
                #theme=theme_data,  # Aplica o tema personalizado ao Container
                #expand=True,  # Expande o Container para ocupar todo o espaço
            ),
        ],
    )
