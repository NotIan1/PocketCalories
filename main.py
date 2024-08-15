# import flet as ft
# from flet import TextField, Checkbox, ElevatedButton, Text, Row, Column
# from flet_core.control_event import ControlEvent
#
#
# def main(page: ft.page) -> None:
#     page.title = 'Signup'
#     page.vertical_alignment = ft.MainAxisAlignment.CENTER
#     page.theme_mode = ft.ThemeMode.LIGHT
#     page.window_width = 400
#     page.window_height = 400
#     page.window_resizable = False
#
#     text_username: TextField = TextField(label='Username', text_align=ft.TextAlign.LEFT, width=200)
#     text_password: TextField = TextField(label='Password', text_align=ft.TextAlign.LEFT, width=200, password=True)
#     checkbox_signup: Checkbox = Checkbox(label='I agree to the T&Cs', value=False)
#     button_submit: ElevatedButton = ElevatedButton(text='Sign up', width=200, disabled=True)
#
#     def validate(e: ControlEvent) -> None:
#         if all([text_username.value, text_password.value, checkbox_signup.value]):
#             button_submit.disabled = False
#         else:
#             button_submit.disabled = True
#         page.update()
#
#     def submit(e: ControlEvent) -> None:
#         print('Username: ', text_username.value)
#         print('Password: ', text_password.value)
#
#         page.clean()
#         page.add(
#             Row(
#                 controls=[Text(value=f'Welcome: {text_username.value}', size=20)],
#                 alignment=ft.MainAxisAlignment.CENTER
#             )
#         )
#
#     checkbox_signup.on_change = validate
#     text_username.on_change = validate
#     text_password.on_change = validate
#     button_submit.on_click = submit
#
#     page.add(
#         Row(
#             controls=[
#                 Column(
#                     [text_username,
#                      text_password,
#                      checkbox_signup,
#                      button_submit],
#                 )
#             ],
#             alignment=ft.MainAxisAlignment.CENTER)
#     )
#
#
# if __name__ == '__main__':
#     ft.app(target=main)
import flet as ft

from navbar import navbar


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
