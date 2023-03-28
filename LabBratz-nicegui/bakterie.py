from nicegui import ui
from header import Header

from image import Image

class Bakterie:
    def __init__(self):
        ui.colors(primary='#B1F28A')
        Header()
        self.im = Image('./baccul.png', colortheme="green")

myim = Bakterie()
ui.run(port=4040)