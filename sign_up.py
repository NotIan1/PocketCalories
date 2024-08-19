import flet as ft
from flet import TextField, Checkbox, ElevatedButton, Text, Row, Column
from flet_core.control_event import ControlEvent


def sign_up(page: ft.Page) -> None:
    # Page settings
    page.title = "Signup"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window_width = 400
    page.window_height = 400
    page.window_resizable = False
    page.bgcolor = "#F0F4FF"  # Light blue background color

    # Input fields and controls
    text_username = TextField(
        label="Username",
        text_align=ft.TextAlign.LEFT,
        width=250,
        bgcolor="#E3F2FD",  # Light blue background for text field
        border_color="#2196F3",  # Blue border color
    )

    text_password = TextField(
        label="Password",
        text_align=ft.TextAlign.LEFT,
        width=250,
        password=True,
        bgcolor="#E3F2FD",  # Light blue background for text field
        border_color="#2196F3",  # Blue border color
    )

    # Initial checkbox color matches the background color
    checkbox_signup = Checkbox(
        label="I agree to the T&Cs",
        value=False,
        fill_color=page.bgcolor,  # Same color as the background
        check_color=ft.colors.WHITE,  # White checkmark color when checked
    )

    button_submit = ElevatedButton(
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

    # Validation function
    def validate(e: ControlEvent) -> None:
        # Change checkbox color to green if clicked, otherwise match background
        checkbox_signup.fill_color = (
            ft.colors.GREEN if checkbox_signup.value else page.bgcolor
        )

        button_submit.disabled = not (
            text_username.value and text_password.value and checkbox_signup.value
        )
        button_submit.style.bgcolor = (
            "#4CAF50" if not button_submit.disabled else ft.colors.RED
        )  # Change color to green when enabled, red when disabled
        page.update()

    # Submit function
    def submit(e: ControlEvent) -> None:
        print("Username:", text_username.value)
        print("Password:", text_password.value)

        # Display welcome message
        page.clean()
        page.add(
            Row(
                controls=[Text(value=f"Welcome, {text_username.value}!", size=20, color="#1E88E5")],  # Blue text color
                alignment=ft.MainAxisAlignment.CENTER,
            )
        )

    # Event handlers
    checkbox_signup.on_change = validate
    text_username.on_change = validate
    text_password.on_change = validate
    button_submit.on_click = submit

    # Page layout
    page.add(
        Row(
            controls=[
                Column(
                    controls=[
                        text_username,
                        text_password,
                        checkbox_signup,
                        button_submit,
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=20,
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )


if __name__ == "__main__":
    ft.app(target=sign_up)
