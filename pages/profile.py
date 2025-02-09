from enum import Enum

import flet as ft

from data.settings import UnitSystem, Settings
from data.user_params import UserParameters


class ProfilePage(ft.View):
    def __init__(self, page):
        super().__init__(route='/profile', padding=20)
        self.page = page  # сохранить переменную в классе
        self.user_params = UserParameters.create(page)
        self.settings = Settings.create(page)

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

        # Settings dialog
        self.settings_dialog = self.create_settings_dialog()

        # Layout
        self.controls = [
            ft.AppBar(
                title=ft.Text("My Profile"), bgcolor="#16E3AF", actions=[
                    ft.PopupMenuButton(
                        items=[
                            ft.PopupMenuItem(
                                text="Edit Profile",
                                icon=ft.icons.EDIT,
                                on_click=self.go_to_parameters
                            ),
                            ft.PopupMenuItem(
                                text="Settings",
                                icon=ft.icons.SETTINGS,
                                on_click=self.show_settings
                            ),
                            ft.PopupMenuItem(
                                text="Logout",
                                icon=ft.icons.LOGOUT,
                                on_click=self.logout
                            ),
                        ]
                    )
                ]
            ),
            ft.ListView(
                expand=True,
                controls=[
                    ft.Container(content=self.profile_picture, alignment=ft.alignment.center),
                    ft.Container(content=self.name_display, alignment=ft.alignment.center),
                    ft.Divider(height=2, color="#16E3AF"),
                    ft.Container(height=20),  # Spacer
                    ft.Column([self.create_info_row(label, key, unit) for label, key, unit in self.info_items]),
                ]
            )
        ]

        self.navigation_bar = self.page.navigation_bar

    def create_settings_dialog(self):
        return ft.AlertDialog(
            title=ft.Text("Settings"),
            content=ft.Column([
                ft.Row([
                    ft.Text("Dark Mode"),
                    ft.Switch(
                        value=self.settings.dark_mode,
                        on_change=self.toggle_theme
                    ),
                ]),
                ft.Row([
                    ft.Text("Unit System"),
                    ft.Switch(
                        value=self.settings.unit_system == UnitSystem.IMPERIAL,
                        label="Imperial" if self.settings.unit_system == UnitSystem.IMPERIAL else "Metric",
                        on_change=self.toggle_units
                    ),
                ]),
            ], tight=True),
            actions=[
                ft.TextButton("Close", on_click=self.close_settings),
            ],
        )

    def go_to_parameters(self, e):
        self.page.go('/parameters')

    def show_settings(self, e):
        self.page.dialog = self.settings_dialog
        self.settings_dialog.open = True
        self.page.update()

    def close_settings(self, e):
        self.settings_dialog.open = False
        self.page.update()

    def toggle_theme(self, e):
        self.settings.dark_mode = e.control.value
        self.settings.apply_theme(self.page)
        self.page.update()

    def toggle_units(self, e):
        new_system = UnitSystem.IMPERIAL if e.control.value else UnitSystem.METRIC
        old_system = self.settings.unit_system
        self.settings.unit_system = new_system

        # Convert values
        if hasattr(self.user_params, 'weight'):
            self.user_params.weight = round(Settings.convert_weight(
                self.user_params.weight, old_system, new_system
            ))
        if hasattr(self.user_params, 'height'):
            self.user_params.height = round(Settings.convert_height(
                self.user_params.height, old_system, new_system
            ))

        self.load_data_from_storage()
        self.page.update()

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
        for label, key, unit in self.info_items:
            value = getattr(self.user_params, key)
            if isinstance(value, Enum):
                value = value.value
            if isinstance(value, list):
                value = ', '.join(value)

            # Apply unit conversions for weight and height
            if key == 'weight' or key == 'height':
                unit_suffix = "kg" if self.settings.unit_system == UnitSystem.METRIC else "lbs"
                if key == 'height':
                    unit_suffix = "cm" if self.settings.unit_system == UnitSystem.METRIC else "inches"

            self.info_displays[key].value = str(value)

    def logout(self, e):
        def confirm_logout(e):
            # Clear all stored data
            self.page.client_storage.clear()
            # Close the dialog
            self.page.dialog.open = False
            self.page.go("/signup")

        def cancel_logout(e):
            self.page.dialog.open = False
            self.page.update()

        # Show confirmation dialog
        self.page.dialog = ft.AlertDialog(
            modal=True,
            title=ft.Text("Confirm Logout"),
            content=ft.Text("Are you sure you want to logout?"),
            actions=[
                ft.TextButton("Cancel", on_click=cancel_logout),
                ft.TextButton("Logout", on_click=confirm_logout),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
        )
        self.page.dialog.open = True
        self.page.update()