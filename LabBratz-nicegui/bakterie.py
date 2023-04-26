from nicegui import ui, app
from header import Header
from uploader import Uploader




class Bakterie:
    def __init__(self):
        ui.colors(primary='#B1F28A')
        Uploader(self.on_image_upload)
        app.add_static_files("/static", ".")
        Header()

    def on_image_upload(self):
        print(1)

myi = Bakterie()
ui.run(port=4040)