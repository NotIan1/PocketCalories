
import flet as ft

from data.user_params import UserParameters
from navbar import navbar
from pages.dish import DishPage
from pages.parameters import ParameterPage
from pages.profile import ProfilePage
from pages.schedule import SchedulePage
from pages.main_window import MainWindowPage
from pages.sign_up import SignupPage


def main(page: ft.Page):
    page.title = "Pocket calories"  # app title
    page.adaptive = True
    navigation_bar = navbar(page)
    page.navigation_bar = navigation_bar

    # page.client_storage.clear()

    def route_change(route):

        # page.views.clear()
        # navigation_bar.selected_index = 0
        # page.views.append(MainWindowPage(page))

        troute = page.route
        if troute == '/':
            navigation_bar.selected_index = 0
            page.views.append(MainWindowPage(page))
        elif troute == "/signup":
            page.views.append(SignupPage(page))
        elif troute == "/parameters":
            page.views.append(ParameterPage(page))
        elif troute == "/schedule":
            navigation_bar.selected_index = 1
            page.views.append(SchedulePage(page))
        elif troute == "/profile":
            navigation_bar.selected_index = 2
            page.views.append(ProfilePage(page))

        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views.pop()
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    
    if not page.client_storage.get('username'):
        page.go('/signup')
    elif not UserParameters.create(page):
        page.go('/parameters')
    else:
        page.go('/')


ft.app(target=main)
