from typing import Callable

import flet as ft

from data.sports import SPORTS, Sport


class SportSelector(ft.Container):
    def __init__(
            self,
            value: str = "",
            on_change: Callable[[str], None] | None = None,
            on_add_new_sport: Callable[[str, dict], None] | None = None
    ):
        self.value = value
        self.intensities = {}
        self.on_change = on_change
        self.on_add_new_sport = on_add_new_sport

        self.text_field = ft.Ref[ft.TextField]()
        self.search_field = ft.Ref[ft.TextField]()
        self.add_sport_name_field = ft.Ref[ft.TextField]()
        self.filtered_list = ft.Ref[ft.ListView]()
        self.min_intensity = ft.Ref[ft.Slider]()
        self.avg_intensity = ft.Ref[ft.Slider]()
        self.max_intensity = ft.Ref[ft.Slider]()
        self.error_text_name = ft.Ref[ft.Text]()
        self.error_text_sliders = ft.Ref[ft.Text]()
        self.icon_button = ft.Ref[ft.IconButton]()

        super().__init__(bgcolor=ft.colors.GREY_200,
                         border_radius=ft.border_radius.all(5),
                         padding=5,
                         # margin=5,
                         content=ft.Row(
                             alignment=ft.MainAxisAlignment.CENTER,
                             controls=[
                                 ft.TextField(
                                     ref=self.text_field,
                                     value=self.value,
                                     width=230,
                                     text_align=ft.TextAlign.CENTER,
                                     read_only=True,
                                     border_color="transparent",
                                     hint_text="Выберите спорт" if not self.value else None,
                                 ),
                                 ft.IconButton(
                                     ref=self.icon_button,
                                     on_click=lambda _: self.show_sport_dialog()
                                 )
                             ]
                         ),
                         width=300)

        # self.bgcolor = ft.colors.AMBER,
        # self.border_radius = ft.border_radius.all(5),
        # self.alignment = "center"  # центрирует внешний Row
        self.set_icon_button()

    @property
    def sport(self):
        return Sport(self.value, self.intensities)

    def set_icon_button(self):
        self.icon_button.current.icon = ft.icons.EDIT if self.value else ft.icons.ADD

    def show_sport_dialog(self):
        # Создаем диалог выбора спорта
        self.sport_dialog = ft.AlertDialog(
            title=ft.Text("Выбрать спорт"),
            content=ft.Column(
                controls=[
                    ft.TextField(
                        ref=self.search_field,
                        hint_text="Начните вводить название спорта...",
                        on_change=self.filter_sports,
                        autofocus=True
                    ),
                    ft.ListView(
                        ref=self.filtered_list,
                        height=200,
                        spacing=2
                    )
                ],
                tight=True
            ),
            actions=[
                ft.TextButton("Отмена", on_click=self.close_dialog),
                ft.TextButton("Изменить", on_click=self.apply_sport_change),
            ]
        )

        # Показываем диалог
        self.page.dialog = self.sport_dialog
        self.sport_dialog.open = True
        self.page.update()

    def show_add_sport_dialog(self, sport_name: str):
        self.add_sport_dialog = ft.AlertDialog(
            title=ft.Text("Добавить новый спорт"),
            content=ft.Container(
                width=400,  # Фиксированная ширина диалога
                content=ft.Column(
                    controls=[
                        ft.TextField(
                            ref=self.add_sport_name_field,
                            label="Название спорта",
                            value=sport_name,
                            on_change=self.validate_name,
                            width=400
                        ),
                        ft.Container(
                            content=ft.Text(
                                ref=self.error_text_name,
                                value="",
                                color=ft.colors.RED_400,
                                size=12,
                                text_align=ft.TextAlign.LEFT,
                                width=360,  # Чуть меньше ширины контейнера для отступов
                                selectable=True,  # Позволяет выделять текст
                                visible=False
                            ),
                            padding=ft.padding.only(top=10, bottom=10)  # Отступы сверху и снизу
                        ),
                        ft.Text(
                            "Минимальная интенсивность:",
                            size=14,
                            weight=ft.FontWeight.BOLD
                        ),
                        ft.Slider(
                            ref=self.min_intensity,
                            min=0,
                            max=100,
                            divisions=100,
                            label="{value}%",
                            value=50,
                            on_change=self.validate_intensities,
                            width=400
                        ),
                        ft.Text(
                            "Средняя интенсивность:",
                            size=14,
                            weight=ft.FontWeight.BOLD
                        ),
                        ft.Slider(
                            ref=self.avg_intensity,
                            min=0,
                            max=100,
                            divisions=100,
                            label="{value}%",
                            value=70,
                            on_change=self.validate_intensities,
                            width=400
                        ),
                        ft.Text(
                            "Максимальная интенсивность:",
                            size=14,
                            weight=ft.FontWeight.BOLD
                        ),
                        ft.Slider(
                            ref=self.max_intensity,
                            min=0,
                            max=100,
                            divisions=100,
                            label="{value}%",
                            value=90,
                            on_change=self.validate_intensities,
                            width=400
                        ),
                        ft.Container(
                            content=ft.Text(
                                ref=self.error_text_sliders,
                                value="",
                                color=ft.colors.RED_400,
                                size=12,
                                text_align=ft.TextAlign.LEFT,
                                width=360,  # Чуть меньше ширины контейнера для отступов
                                selectable=True,  # Позволяет выделять текст
                                visible=False
                            ),
                            padding=ft.padding.only(top=10, bottom=10)  # Отступы сверху и снизу
                        )
                    ],
                    tight=True,
                    spacing=10
                ),
                padding=20  # Отступы от краёв диалога
            ),
            actions=[
                ft.TextButton("Отмена", on_click=self.close_add_dialog),
                ft.TextButton("Добавить", on_click=self.add_new_sport),
            ]
        )

        self.page.dialog = self.add_sport_dialog
        self.add_sport_dialog.open = True
        self.page.update()

    def validate_intensities(self, e=None):
        """Проверяет корректность значений интенсивности"""
        if not all([self.min_intensity.current, self.avg_intensity.current, self.max_intensity.current]):
            return

        min_val = self.min_intensity.current.value
        avg_val = self.avg_intensity.current.value
        max_val = self.max_intensity.current.value

        if not (min_val <= avg_val <= max_val):
            self.error_text_sliders.current.value = (
                "Минимальная интенсивность должна быть меньше средней, "
                "а средняя меньше максимальной!"
            )
            self.error_text_sliders.current.visible = True
        else:
            self.error_text_sliders.current.value = ""
            self.error_text_sliders.current.visible = False

        self.page.update()

    def validate_name(self, e=None):
        # Проверяем существование спорта
        capitalized_name = self.add_sport_name_field.current.value.title()
        if capitalized_name in SPORTS:
            self.error_text_name.current.value = f"Спорт '{capitalized_name}' уже существует в списке!"
            self.error_text_name.current.visible = True
        else:
            self.error_text_name.current.value = ""
            self.error_text_name.current.visible = False

        self.page.update()

    def filter_sports(self, e):
        search_term = self.search_field.current.value.lower()
        filtered = [
            sport for sport in SPORTS
            if search_term in sport.lower()
        ]

        # Если нет точного совпадения и есть текст поиска
        if (search_term and
                search_term not in [s.lower() for s in SPORTS]):
            # Добавляем опцию создания нового спорта
            filtered.append(f"Добавить новый спорт: {self.search_field.current.value}")

        self.filtered_list.current.controls = [
            ft.ListTile(
                title=ft.Text(sport),
                on_click=lambda _, s=sport: self.handle_sport_selection(s)
            ) for sport in filtered
        ]
        self.page.update()

    def handle_sport_selection(self, sport: str):
        if sport.startswith("Добавить новый спорт: "):
            # Извлекаем название нового спорта
            new_sport = sport.replace("Добавить новый спорт: ", "")
            self.close_dialog()
            self.show_add_sport_dialog(new_sport)
        else:
            self.selected_sport = sport
            self.apply_sport_change()

    def add_new_sport(self, e):
        if self.error_text_sliders.current.visible or self.error_text_name.current.visible:
            return

        sport_name = self.add_sport_name_field.current.value.title()
        self.intensities = {
            "low": self.min_intensity.current.value,
            "average": self.avg_intensity.current.value,
            "high": self.max_intensity.current.value,
        }

        if self.on_add_new_sport:
            self.on_add_new_sport(sport_name, self.intensities)

        # Добавляем в список спортов
        SPORTS[sport_name] = self.intensities
        # Обновляем текущее значение
        self.value = sport_name
        self.text_field.current.value = sport_name

        self.close_add_dialog()

    def close_dialog(self, e=None):
        self.sport_dialog.open = False
        self.set_icon_button()
        self.page.update()

    def close_add_dialog(self, e=None):
        self.add_sport_dialog.open = False
        self.set_icon_button()
        self.page.update()

    def apply_sport_change(self, e=None):
        if hasattr(self, 'selected_sport'):
            self.value = self.selected_sport
            self.intensities = SPORTS[self.selected_sport]
            self.text_field.current.value = self.selected_sport
            if self.on_change:
                self.on_change(self.selected_sport)
        self.close_dialog()
