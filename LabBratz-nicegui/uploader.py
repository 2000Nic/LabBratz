from PIL import Image as Pim
from nicegui import ui, events, app


class Uploader():

    def __init__(self, func):
        self.uploader = ui.upload(auto_upload=True, on_upload=self.handle_upload).style("margin-top: 50px;")
        self.func = func

    def handle_upload(self, event: events.UploadEventArguments):
        with event.content as f:
            uploaded_file = Pim.open(f)
            uploaded_file.save("static/uploaded.png")
            self.func()


