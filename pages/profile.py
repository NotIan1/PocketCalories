from enum import Enum

import flet as ft

from data.user_params import UserParameters


class ProfilePage(ft.View):
    def __init__(self, page, navbar):
        super().__init__(route='/profile', padding=20)
        self.page = page  # сохранить переменную в классе
        self.navbar = navbar
        self.user_params = UserParameters.create(page)

        # Profile picture
        self.profile_picture = ft.Container(
            content=ft.Icon(ft.icons.ACCOUNT_CIRCLE, size=100, color=ft.colors.WHITE),
            width=120,
            height=120,
            border_radius=60,
            bgcolor="#16E3AF",
            alignment=ft.alignment.center,
        )

        # Information display
        self.name_display = ft.Text("Name: ", size=18, weight=ft.FontWeight.BOLD)
        self.info_items = [
            ("Age", "age", "years"),
            ("Gender", "gender", ""),
            ("Weight", "weight", "kg"),
            ("Height", "height", "cm"),
            ("Main sport", "main_sport", ""),
            ("Training frequency", "training_times", "times/week"),
            ("Goal", "goal", ""),
            ("Activity level", "activity_level", ""),
            ("Allergies", "allergies", ""),
        ]
        self.info_displays = {key: ft.Text(f"{label}: ", size=16) for label, key, _ in self.info_items}

        # Load data from client_storage
        self.load_data_from_storage()

        # Layout
        self.controls = [
            ft.AppBar(title=ft.Text("My Profile"), bgcolor="#16E3AF", color=ft.colors.WHITE, actions=[
                ft.IconButton(
                    icon=ft.icons.EDIT,
                    icon_color=ft.colors.WHITE,
                    tooltip="Edit Profile",
                    on_click=self.go_to_parameters
                )
            ]),
            ft.Container(
                content=ft.Column([
                    ft.Container(content=self.profile_picture, alignment=ft.alignment.center),
                    ft.Container(content=self.name_display, alignment=ft.alignment.center),
                    ft.Divider(height=2, color="#16E3AF"),
                    ft.Container(height=20),  # Spacer
                    ft.Column([
                        self.create_info_row(label, key, unit)
                        for label, key, unit in self.info_items
                    ]),
                ],
                    alignment=ft.MainAxisAlignment.START,
                    horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
                    spacing=10),
                padding=20,
                bgcolor=ft.colors.WHITE,
                border_radius=10,
                shadow=ft.BoxShadow(
                    spread_radius=1,
                    blur_radius=10,
                    color=ft.colors.BLACK26,
                    offset=ft.Offset(0, 0),
                )
            ),
            self.navbar
        ]

    def create_info_row(self, label, key, unit):
        return ft.Row([
            ft.Text(f"{label}:", style=ft.TextStyle(weight=ft.FontWeight.BOLD), width=150),
            ft.Container(
                content=self.info_displays[key],
                alignment=ft.alignment.center,
                expand=True
            ),
            ft.Text(unit, width=50) if unit else ft.Container(width=50),
        ], alignment=ft.MainAxisAlignment.CENTER)

    def load_data_from_storage(self):
        self.name_display.value = self.user_params.name
        for label, key, _ in self.info_items:
            value = getattr(self.user_params, key)
            if isinstance(value, Enum):
                value = value.value
            self.info_displays[key].value = f"{value}"

    def go_to_parameters(self, e):
        self.page.go('/parameters')
