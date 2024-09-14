
import flet as ft

from navbar import navbar
from pages.Parameters import ParameterPage
from pages.Profile import ProfilePage
from pages.Schedule import SchedulePage
from pages.mainwindow import MainWindowPage
from pages.sign_up import SignupPage


def main(page: ft.Page):
    page.title = "Pocket calories"  # app title
    page.adaptive = True
    navigation_bar = navbar(page)

    def route_change(route):
        page.views.clear()
        page.views.append(MainWindowPage(page, navigation_bar))

        if page.route == "/schedule":
            page.views.append(SchedulePage(page, navigation_bar))

        elif page.route == "/profile":
            page.views.append(ProfilePage(page, navigation_bar))
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
    
    if not page.client_storage.get('username'):
        page.go('/signup')
    elif not page.client_storage.get('name'):
        page.go('/parameters')
    else:
        page.go('/')


ft.app(target=main)
