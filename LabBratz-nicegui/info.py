from nicegui import ui
from header import Header


class Info:
    def __init__(self):
        ui.colors(primary='#7EC8F2')
        Header()
        with ui.column().classes('self-center'):
            self.info()
            self.team()

    def info(self):

        with ui.card().tight().classes('self-center'):
            with ui.card_section():
                ui.label('Info om LabBratz').classes('text-4xl')
            with ui.card_section():
                ui.label('LabBratz').classes('text-2xl')
                ui.html('<p>LabBratz er et program lavet til at hjælpe med at analysere data fra forsøg i laboratoriet.</p>'
                        ' <p>LabBratz er lavet af 4 HTX elever fra NEXT Vibenshus</p> ')

            with ui.card_section():
                ui.label('Værktøjer').classes('text-2xl')
                ui.html('<p>TLC: er en metode til at bestemme koncentrationen af en blanding</p>')
                ui.html('<p>QDA: </p>')
                ui.html('<p>Bakterietælling: </p>')


            with ui.card_section():
                ui.label('Kontakt').classes('text-2xl')
                ui.label('Tlf: 12345678').classes('h3')
                ui.label('Mail: labbratz@toiletpaper.dk').classes('h3')

    def team(self):
        with ui.card().tight().classes('self-center'):
            with ui.card_section():
                ui.label('Teamet bag LabBratz').classes('text-4xl').classes('self-center')
            with ui.row().classes('self-center'):
                with ui.card_section():
                    with ui.card_section():
                        ui.label('Alfred').classes('text-2xl')
                        ui.label('Alfred er en idiot').classes('h3')

                with ui.card_section():
                    with ui.card_section():
                        ui.label('Dona').classes('text-2xl')
                        ui.label('Dona er en idiot').classes('h3')

                with ui.card_section():
                    with ui.card_section():
                        ui.label('Nicolas').classes('text-2xl')
                        ui.label('Nicolas er en idiot').classes('h3')

                with ui.card_section():
                    with ui.card_section():
                        ui.label('Phillip').classes('text-2xl')
                        ui.label('Phillip er en idiot').classes('h3')
