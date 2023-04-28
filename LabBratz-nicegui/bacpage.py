from nicegui import ui
from header import Header
from image import Image
from bac_image import Bac_image

class Bac_Page:

    def __init__(self):
        ui.colors(primary='#B1F28A')
        Header()
        self.im = Bac_image("./static/uploaded.png", self.upload_new)
        with ui.dialog() as self.dialog, ui.card():
            ui.label('Denne handling vil slette det nuværende billede og alle indstillinger. Du kan med fordel gemme billedet. Vil du fortsætte?')
            with ui.row():
                ui.button('Tilbage', on_click=self.dialog.close)
                ui.button("Fortsæt", on_click=ui.open("bakterie"))

        with ui.column().style("float: left; margin-top: 50px; left: 50px; width: 500px; position: absolute; display: inline-grid;"):
            ui.label("Bakterietælling").style("font-size: 40px; font-weight: bold; color: #757575;")
            ui.separator()

            ui.label("Den automatiske bakterietælling opfangede:").style("font-size: 20px; font-weight: bold; color: #757575;")
            self.im.write_count()

    def upload_new(self):
        self.dialog.open()






