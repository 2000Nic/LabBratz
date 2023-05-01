from nicegui import ui
from header import Header
from qda_setup import QDA_setup
from qda_trial import QDA_trial
from qda_data import QDA_data

class QDA:
    def __init__(self):
        ui.colors(primary='#96D0F2')
        Header()
        self.tabmenu = ui.tabs().classes('self-center')
        with self.tabmenu:
            ui.tab('Opsætning')
            ui.tab('Forsøg')
            ui.tab('Data')
        with ui.tab_panels(self.tabmenu, value='Opsætning').style("width:100%"):
            with ui.tab_panel('Opsætning'):
                QDA_setup()
            with ui.tab_panel('Forsøg'):
                QDA_trial()
            with ui.tab_panel('Data'):
                QDA_data()