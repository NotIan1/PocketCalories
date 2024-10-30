from datetime import datetime, timedelta

import flet as ft


class SchedulePage(ft.View):
    def __init__(self, page):
        super().__init__(route='/schedule', padding=20)
        self.page = page

        planner = WeeklyPlanner()

        def update_schedule_view():
            schedule_view.controls.clear()
            current_day = planner.current_date.strftime('%A')
            for item in planner.schedule[current_day]:
                schedule_view.controls.append(
                    ft.ListTile(
                        leading=ft.Icon(ft.icons.FASTFOOD if item['type'] == 'meal' else ft.icons.SPORTS_HANDBALL),
                        title=ft.Text(f"{item['time']} - {item['name']}"),
                        subtitle=ft.Text(item['details']),
                        trailing=ft.PopupMenuButton(
                            items=[
                                ft.PopupMenuItem(text="Edit",
                                                 on_click=lambda _: edit_item(
                                                     planner.schedule[current_day].index(item))),
                                ft.PopupMenuItem(text="Delete",
                                                 on_click=lambda _: delete_item(
                                                     planner.schedule[current_day].index(item)))
                            ]
                        )
                    )
                )
            page.update()

        def change_date(delta):
            planner.current_date += timedelta(days=delta)
            date_display.value = planner.current_date.strftime("%A, %B %d, %Y")
            update_schedule_view()

        def add_new_item(e):
            def save_new_item(e):
                planner.add_item(
                    planner.current_date.strftime('%A'),
                    item_type_dropdown.value,
                    name_input.value,
                    time_input.value,
                    details_input.value
                )
                update_schedule_view()

            item_type_dropdown = ft.Dropdown(
                options=[
                    ft.dropdown.Option("meal"),
                    ft.dropdown.Option("activity")
                ],
                width=200
            )
            name_input = ft.TextField(label="Name")
            time_input = ft.TextField(label="Time (HH:MM)")
            details_input = ft.TextField(label="Details")

            def handle_close(e):
                page.close(dialog)

            dialog = ft.AlertDialog(
                title=ft.Text("Add New Item"),
                content=ft.Column([item_type_dropdown, name_input, time_input, details_input]),
                actions=[
                    ft.TextButton("Save", on_click=save_new_item),
                    ft.TextButton("Cancel", on_click=handle_close),
                ]
            )
            page.open(dialog)
            page.update()

        def edit_item(index):
            item = planner.schedule[planner.current_date.strftime('%A')][index]

            def save_edit(e):
                planner.update_item(
                    planner.current_date.strftime('%A'),
                    index,
                    name_input.value,
                    time_input.value,
                    details_input.value
                )
                page.close(dialog)
                update_schedule_view()

            name_input = ft.TextField(label="Name", value=item['name'])
            time_input = ft.TextField(label="Time (HH:MM)", value=item['time'])
            details_input = ft.TextField(label="Details", value=item['details'])

            def handle_close(e):
                page.close(dialog)

            dialog = ft.AlertDialog(
                title=ft.Text("Edit Item"),
                content=ft.Column([name_input, time_input, details_input]),
                actions=[
                    ft.TextButton("Save", on_click=save_edit),
                    ft.TextButton("Cancel", on_click=handle_close),
                ]
            )
            page.open(dialog)
            page.update()

        def delete_item(index):
            planner.remove_item(planner.current_date.strftime('%A'), index)
            update_schedule_view()

        date_display = ft.Text(planner.current_date.strftime("%A, %B %d, %Y"), size=20)

        schedule_view = ft.Column()

        self.controls = [
            ft.Row([
                ft.IconButton(ft.icons.ARROW_BACK, on_click=lambda _: change_date(-1)),
                date_display,
                ft.IconButton(ft.icons.ARROW_FORWARD, on_click=lambda _: change_date(1)),
            ], alignment=ft.MainAxisAlignment.CENTER),
            schedule_view,
            ft.FloatingActionButton(icon=ft.icons.ADD, on_click=add_new_item),
            ft.AppBar(title=ft.Text("Schedule"), bgcolor="#16E3AF", color=ft.colors.WHITE,),
        ]
        self.navigation_bar = self.page.navigation_bar

        update_schedule_view()


class WeeklyPlanner:
    def __init__(self):
        self.current_date = datetime.now()
        self.schedule = {day: [] for day in
                         ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']}
        self.initialize_schedule()

    def initialize_schedule(self):
        for day in self.schedule:
            self.schedule[day].extend([
                {'type': 'meal', 'name': 'Breakfast', 'time': '07:45', 'details': 'Cereal'},
                {'type': 'meal', 'name': 'Lunch', 'time': '14:00', 'details': ''},
                {'type': 'meal', 'name': 'Dinner', 'time': '19:00', 'details': ''}
            ])

    def add_item(self, day, item_type, name, time, details=''):
        self.schedule[day].append({
            'type': item_type,
            'name': name,
            'time': time,
            'details': details
        })
        self.schedule[day].sort(key=lambda x: x['time'])

    def remove_item(self, day, index):
        del self.schedule[day][index]

    def update_item(self, day, index, name, time, details):
        self.schedule[day][index].update({
            'name': name,
            'time': time,
            'details': details
        })
        self.schedule[day].sort(key=lambda x: x['time'])
