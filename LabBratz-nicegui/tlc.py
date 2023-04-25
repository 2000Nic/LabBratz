from nicegui import ui, events
from header import Header
from TLC_p import TLC_Page
from uploader import Uploader



@ui.page('/tlc_page')
def tlc_page():
    TLC_Page()


class TLC:
    def __init__(self):
        ui.colors(primary='#F1AEF2')
        Header()

        with ui.column().style("float: left; margin-top: 50px; left: 50px; width: 500px; position: absolute; display: inline-grid;"):
            ui.label("Upload TLC").style("font-size: 40px; font-weight: bold; color: #757575;")
            ui.separator()
            self.switch = ui.switch('Automatisk markering', value=True).style("margin-top: 50px; font-size: 20px; font-weight: bold; color: #757575;")

            Uploader(self.open_image_page)
            ui.label("Billedet skal enten uploades som .png eller .jpg").style("font-size: 15px; font-weight: bold; color: #757575;")

    def open_image_page(self):
        ui.open(tlc_page)
        """ui.open('tlc_page/'+str(self.switch.value))"""


hew = TLC()
ui.run(port=4040)