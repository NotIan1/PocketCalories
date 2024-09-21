import flet as ft

# Define a link style dict.
link_style = {
    "height": 50,
    "focused_border_color": "#F4CE14",
    "border_radius": 5,
    "cursor_height": 16,
    "cursor_color": "white",
    "content_padding": 10,
    "border_width": 1.5,
    "text_size": 14,
    "label_style": ft.TextStyle(color="#F4CE14"),
}


# Define a link class...
class Link(ft.TextField):
    def __init__(self, label: str, value: str, page: ft.Page):
        super().__init__(
            value=value,
            read_only=True,
            label=label,
            on_focus=self.selected,
            **link_style,
        )

        self.page = page

    # Define a method to show snackbar for copied event
    def selected(self, event: ft.TapEvent = None):
        self.page.snack_bar = ft.SnackBar(
            ft.Text(f"Copied {self.label}!"), show_close_icon=True, duration=2000
        )

        self.page.snack_bar.open = True
        self.page.update()


class ProfilePage(ft.View):
    def __init__(self, page, navbar):
        super().__init__(route='/profile', padding=20)
        self.page = page  # сохранить переменную в классе
        self.navbar = navbar

        self.controls = [
            ft.AppBar(title=ft.Text("Profile"), bgcolor=ft.colors.SURFACE_VARIANT),
            ft.SafeArea(
                expand=True,
                content=ft.Column(
                    horizontal_alignment="center",
                    controls=[
                        ft.Divider(height=20, color="transparent"),
                        ft.Container(
                            bgcolor="white10",
                            width=128,
                            height=128,
                            shape=ft.BoxShape("circle"),
                            # Define image for profile picture
                            image_src="/profile.jpg",
                            image_fit="cover",
                            shadow=ft.BoxShadow(
                                spread_radius=6,
                                blur_radius=20,
                                color=ft.colors.with_opacity(0.71, "black"),
                            ),
                        ),
                        ft.Divider(height=10, color="transparent"),
                        ft.Text(self.page.client_storage.get("name"), size=32),
                        ft.Text(
                            "Python Programming | UI/UX Design | GUI & Web Apps",
                            weight="w400",
                            text_align="center",
                        ),
                        ft.Divider(height=50, color="transparent"),
                        ft.Column(
                            spacing=20,
                            controls=[
                                # Inerst link items here...
                                Link("Name", "Line Indent", self.page),
                                Link("Youtube", "@lineindent", self.page),
                                Link("Email", "example@gmail.com", self.page),
                            ],
                        ),
                    ],
                ),
            ),
            self.navbar
        ]
