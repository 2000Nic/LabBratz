from nicegui import ui
from header import Header
from qda_setup import QDA_setup

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
                QDA_setup()
            with ui.tab_panel('Forsøg'):
                ui.label('Forsøg')
            with ui.tab_panel('Data'):
                ui.label('Data')