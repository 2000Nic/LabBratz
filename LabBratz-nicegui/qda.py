from nicegui import ui
from header import Header
from qda_setup import QDA_setup
from qda_trial import QDA_trial

class QDA:
    def __init__(self):
        ui.colors(primary='#96D0F2')
        Header()

        with ui.tabs().classes('self-center') as tabs:
            ui.tab('Opsætning')
            ui.tab('Forsøg')
            ui.tab('Data')
        with ui.tab_panels(tabs, value='Opsætning').style("width:100%"):
            with ui.tab_panel('Opsætning'):
                QDA_setup()
            with ui.tab_panel('Forsøg'):
                QDA_trial()
            with ui.tab_panel('Data'):
                ui.label('Data')