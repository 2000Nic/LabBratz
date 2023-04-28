from nicegui import ui
from header import Header
from image import Image

class TLC_Page:

    def __init__(self):
        ui.colors(primary='#F1AEF2')
        Header()
        self.im = Image("./static/uploaded.png", self.upload_new)
        with ui.dialog() as self.dialog, ui.card():
            ui.label('Denne handling vil slette det nuværende billede og alle indstillinger. Du kan med fordel gemme billedet. Vil du fortsætte?')
            with ui.row():
                ui.button('Tilbage', on_click=self.dialog.close)
                ui.button("Fortsæt", on_click=ui.open("/TLC"))

        with ui.column().style("float: left; margin-top: 50px; left: 50px; width: 500px; position: absolute; display: inline-grid;"):
            ui.label("TLC-analyse").style("font-size: 40px; font-weight: bold; color: #757575;")
            ui.separator()

            ui.label("Angiv startlinje").style("font-size: 20px; font-weight: bold; color: #757575;")
            self.bottomline = ui.slider(min=0, max=self.im.bgimage.size[1], value=0)
            self.bottomline.on('update:model-value', lambda x: self.im.draw_bottom_line(f'{x["args"]}'))
            ui.label("Angiv væskefront").style("font-size: 20px; font-weight: bold; color: #757575;")
            self.topline = ui.slider(min=0, max=self.im.bgimage.size[1], value=0)
            self.topline.on('update:model-value', lambda x: self.im.draw_topline(f'{x["args"]}'))
            ui.separator()
            ui.label("Rf-værdier").style("font-size: 20px; font-weight: bold; color: #757575;")
            ui.label("Vælg hvordan markeringen på billedet skal se ud.")
            self.toggle = ui.toggle(["ID", "Rf", "Begge"], value="Begge")
            self.toggle.on('update:model-value', lambda x: self.im.update_view(x["args"]))

    def upload_new(self):
        self.dialog.open()






