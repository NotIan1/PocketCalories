import flet as ft
class ProfilePage(ft.View):
    def __init__(self, page, navbar):
        super().__init__(route='/profile', padding=20)
        self.page = page  # сохранить переменную в классе
        self.navbar = navbar

        self.controls = [
            ft.AppBar(title=ft.Text("Profile"), bgcolor=ft.colors.SURFACE_VARIANT),
            # ... код из туториала
            self.navbar
        ]
