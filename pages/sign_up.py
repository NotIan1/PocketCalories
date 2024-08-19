import flet as ft
from flet import TextField, Checkbox, ElevatedButton, Text, Row, Column
from flet_core.control_event import ControlEvent

class SignupPage(ft.View):
    def __init__(self, page):
        super().__init__(route='/signup', padding=20)
        self.page = page

        # Input fields and controls
        self.text_username = TextField(
            label="Username",
            text_align=ft.TextAlign.LEFT,
            width=250,
            bgcolor="#E3F2FD",  # Light blue background for text field
            border_color="#2196F3",  # Blue border color
        )

        self.text_password = TextField(
            label="Password",
            text_align=ft.TextAlign.LEFT,
            width=250,
            password=True,
            bgcolor="#E3F2FD",  # Light blue background for text field
            border_color="#2196F3",  # Blue border color
        )

        # Initial checkbox color matches the background color
        self.checkbox_signup = Checkbox(
            label="I agree to the T&Cs",
            value=False,
            fill_color=page.bgcolor,  # Same color as the background
            check_color=ft.colors.WHITE,  # White checkmark color when checked
        )

        self.button_submit = ElevatedButton(
            text="Sign up",
            width=250,
            disabled=True,
            style=ft.ButtonStyle(
                color=ft.colors.WHITE,
                bgcolor=ft.colors.RED,  # Red background for the button when disabled
                shape=ft.RoundedRectangleBorder(radius=8),
                padding={"top": 12, "bottom": 12, "left": 20, "right": 20},
                elevation=5,
            ),
        )

        # Event handlers
        self.checkbox_signup.on_change = self.validate
        self.text_username.on_change = self.validate
        self.text_password.on_change = self.validate
        self.button_submit.on_click = self.submit

        # Page layout
        self.controls = [
            Row(
                controls=[
                    Column(
                        controls=[
                            self.text_username,
                            self.text_password,
                            self.checkbox_signup,
                            self.button_submit,
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=20,
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            )
        ]

    # Validation function
    def validate(self, e: ControlEvent) -> None:
        # Change checkbox color to green if clicked, otherwise match background
        self.checkbox_signup.fill_color = (
            ft.colors.GREEN if self.checkbox_signup.value else self.page.bgcolor
        )

        self.button_submit.disabled = not (
                self.text_username.value and self.text_password.value and self.checkbox_signup.value
        )
        self.button_submit.style.bgcolor = (
            "#4CAF50" if not self.button_submit.disabled else ft.colors.RED
        )  # Change color to green when enabled, red when disabled
        self.page.update()

    def submit(self, e: ControlEvent) -> None:
        print("Username:", self.text_username.value)
        print("Password:", self.text_password.value)

        self.page.go('/parameters'),



def main(page: ft.Page):
    # Page settings
    page.title = "Signup"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window_width = 400
    page.window_height = 400
    page.window_resizable = False
    page.bgcolor = "#F0F4FF"  # Light blue background color

    profile = SignupPage(page)
    page.views.append(profile)
    page.update()

if __name__ == '__main__':
    ft.app(target=main)