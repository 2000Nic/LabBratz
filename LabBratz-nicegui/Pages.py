from nicegui import ui
from tlc import TLC
from TLC_p import TLC_Page

@ui.page("/TLC")
def Tlc():
    TLC()

@ui.page("/tlc_page")
def tlc_page():
    TLC_Page()

ui.run(port=4040)