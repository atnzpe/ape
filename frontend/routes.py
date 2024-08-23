# De Flet importe View, TemplateRoute
from flet import View, TemplateRoute


def view_builder(page, route):
    page.views.clear()
    # Importe suas telas aqui (substitua pelos nomes corretos dos arquivos)
    from screens.home_screen import HomeScreen
    from screens.destinos_screen import DestinosScreen
    from screens.food_screen import FoodScreen

    route_map = {
        "/": View("/", "/home", controls=[HomeScreen(page)]),  # Rota Incial
        "/home": View("/", "/home", controls=[HomeScreen(page)]),
        "/destinos": View("/destinos", "/destinos", controls=[DestinosScreen(page)]),
        "/food": View("/food", "/food", controls=[FoodScreen(page)],)
    }

    page.views.append(route_map.get(route, View(
        "/404", controls=[Text("Página não Encontrada")])))
    page.update()

app_routes = [
    TemplateRoute("/", view_builder),
    TemplateRoute("/home", view_builder),
    TemplateRoute("/destinos", view_builder),
    TemplateRoute("/food", view_builder),
]