import flet as ft


class HomeScreen(ft.UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page  # Referecia a página

    def build(self):
        return ft.Column(
            [
                
                # 2. Divisores com as cores da bandeira de Pernambuco
                
                ft.Text("Explore os encantos de Pernambuco!"),
                ft.ElevatedButton("Começar a Explorar", on_click=self.abrir_modal),      
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
                    ft.ElevatedButton("Dar uma Voltinha", on_click=lambda _: self.page.go("/destinos")),
                ]
            ),
        )
        self.page.dialog.open = True
        self.page.update()