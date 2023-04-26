from nicegui import ui, app, events
from PIL import Image as Pim

def handle_upload(self, event: events.UploadEventArguments):
    with event.content as f:
        uploaded_file = Pim.open(f)
        uploaded_file.save("uploaded.png")
        ui.interactive_image("./uploaded.png", cross=True)

app.add_static_files("/", ".")
ui.upload(auto_upload=True, on_upload=handle_upload)

ui.run(port=4040)

