import flet as ft


class MainWindowPage(ft.View):
    def __init__(self, page, navbar):
        super().__init__(route='/', padding=20)
        self.page = page
        self.navbar = navbar

        self.controls = [
            ft.AppBar(title=ft.Text("Main Window"), bgcolor=ft.colors.SURFACE_VARIANT),
            self.navbar
        ]
