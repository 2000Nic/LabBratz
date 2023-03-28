from nicegui import ui
from header import Header
from image import Image

class TLC:
    def __init__(self):
        ui.colors(primary='#F1AEF2')
        Header()
        self.im = Image('./baccul.png', colortheme='pink')
