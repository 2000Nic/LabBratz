from nicegui import ui
from header import Header

class QDA:
    def __init__(self):
        ui.colors(primary='#96D0F2')
        Header()

        with ui.tabs().classes('self-center') as tabs:
            ui.tab('Opsætning')
            ui.tab('Forsøg')
            ui.tab('Data')
        with ui.tab_panels(tabs, value='Opsætning'):
            with ui.tab_panel('Opsætning'):
                Opsatning()
            with ui.tab_panel('Forsøg'):
                ui.label('Forsøg')
            with ui.tab_panel('Data'):
                ui.label('Data')

class Opsatning:
    def __init__(self):
        ui.label('Vælg parametre').classes('h3')