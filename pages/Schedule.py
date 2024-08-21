import flet as ft

class SchedulePage(ft.View):
    def __init__(self, page, navbar):
        super().__init__(route='/schedule', padding=20)
        self.page = page
        self.navbar = navbar

        self.controls = [
            ft.AppBar(title=ft.Text("Schedule"), bgcolor=ft.colors.SURFACE_VARIANT),
            self.navbar
        ]