import flet as ft


class HomeScreen(ft.Control):
    def __init__(self, page):
        super().__init__()
        self.page = page

    def build(self):
        
        return ft.Column(
            [
                ft.Text("Explore os encantos de Pernambuco!"),
                ft.ElevatedButton("Começar a Explorar",
                                  on_click=self.abrir_modal),
            ],
            alignment="center",
            horizontal_alignment="center",
        )

        return self  # <---- Correção: return self fora do bloco do Column

    def abrir_modal(self, e):
        dialog = ft.AlertDialog(
            modal=True,
            title=ft.Text("Queres o que?"),
            content=ft.Column(
                [
                    ft.ElevatedButton(
                        "Encher o Buxo", on_click=lambda _: self.page.go("/food")),
                    ft.ElevatedButton(
                        "Dar uma Voltinha", on_click=lambda _: self.page.go("/destinos")),
                    ft.ElevatedButton("Voltar para Início",
                                      on_click=lambda _: self.page.go("/home"))
                ]
            ),
        )
        self.page.overlay.append(dialog)
        dialog.open = True
        self.page.update()
