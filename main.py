
import flet as ft

from navbar import navbar
from pages.Parameters import ParameterPage
from pages.sign_up import SignupPage


def main(page: ft.Page):
    page.title = "Pocket calories" #app title
    page.adaptive = True
    navigation_bar = navbar(page)

    def route_change(route):
        page.views.clear()
        page.views.append(
            ft.View(
                "/",
                [
                    ft.AppBar(title=ft.Text("Main Window"), bgcolor=ft.colors.SURFACE_VARIANT),
                    navigation_bar
                ],
            )
        )
        if page.route == "/schedule":
            page.views.append(
                ft.View(
                    "/schedule",
                    [
                        ft.AppBar(title=ft.Text("Schedule"), bgcolor=ft.colors.SURFACE_VARIANT),
                        navigation_bar
                    ],
                )
            )

        elif page.route == "/profile":
            page.views.append(
                ft.View(
                    "/profile",
                    [
                        ft.AppBar(title=ft.Text("Profile"), bgcolor=ft.colors.SURFACE_VARIANT),
                        navigation_bar
                    ],
                )
            )
        elif page.route == "/parameters":
            page.views.append(ParameterPage(page))

        elif page.route == "/signup":
            page.views.append(SignupPage(page))

        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        navigation_bar.selected_index = 0
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


ft.app(target=main, view=ft.AppView.WEB_BROWSER)
