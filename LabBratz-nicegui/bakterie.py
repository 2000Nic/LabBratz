from nicegui import ui
from header import Header
from uploader import Uploader
from bacpage import Bac_Page

@ui.page('/bac_page')
def bac_page():
    Bac_Page()


class Bakterie:
    def __init__(self):
        ui.colors(primary='#B1F28A')
        Header()

        with ui.column().style(
                "float: left; margin-top: 50px; left: 50px; width: 500px; position: absolute; display: inline-grid;"):
            ui.label("Upload bakterier").style("font-size: 40px; font-weight: bold; color: #757575;")
            ui.separator()
            ui.label("Det er en god idé at holde kameraet parallelt med petriskålen før billedet tages, "
                     "samt at beskære billedet så meget som muligt før upload.")\
                .style("font-size: 20px; color: #757575;")

            self.switch = ui.switch('Automatisk markering', value=True).style(
                "margin-top: 50px; font-size: 20px; font-weight: bold; color: #757575;")

            Uploader(self.open_image_page)
            ui.label("Billedet skal enten uploades som .png eller .jpg").style(
                "font-size: 15px; font-weight: bold; color: #757575; margin-bottom: 50px;")

    def open_image_page(self):
        ui.open("/bac_page")

