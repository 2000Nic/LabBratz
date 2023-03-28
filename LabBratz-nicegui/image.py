from nicegui import ui, app
from nicegui.events import MouseEventArguments
from Blob_detector import Blob_Detector
from marker import Marker
from PIL import Image as Pim
from cairosvg import svg2png

class Image:

    def __init__(self, path, colortheme='pink'):

        self.bgimage = Pim.open(path)

        with ui.element('div').style("float: right; margin-top: 50px; right: 50px; width: 600px; position: absolute; display: inline-grid;"):
            self.im = ui.interactive_image(path, on_mouse= self.mouse_handler, cross=True)
            self.add_remove = ui.radio(["Tilføj", "Fjern"], value="Tilføj")
            self.save_button = ui.button("Gem som png", on_click=self.save)

        self.keypoints = []
        self.blob_detector = Blob_Detector(path)
        self.colortheme = colortheme

        self.setup()

    def setup(self):
        colorstyle = 'inline color=' + self.colortheme


        self.add_remove.props('inline').props(colorstyle)
        self.blob_detect()
        self.draw()

    def blob_detect(self):
        temp_keypts = self.blob_detector.detect()

        for keypt in temp_keypts:
            self.keypoints.append(Marker(keypt.pt[0], keypt.pt[1], self.colortheme))

    def draw(self):
        for mark in self.keypoints:
            self.im.content += mark.svg()

    def mouse_handler(self, e: MouseEventArguments):
        new_mark = Marker(e.image_x, e.image_y, self.colortheme)
        match self.add_remove.value:
            case "Tilføj":
                self.keypoints.append(new_mark)
                self.im.content += self.keypoints[-1].svg()
            case "Fjern":
                for i, mark in enumerate(self.keypoints):
                    if new_mark.collision(mark):
                       self.im.set_content(" ")
                       del self.keypoints[i]
                       self.draw()
                    else:
                        pass

    def save(self):
        width = self.bgimage.size[0]
        height = self.bgimage.size[1]

        viewbox = 'viewBox="0 0 ' + str(width) + ' ' + str(height) + '"'
        xmlns = 'xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" '

        header = '<svg width="' + str(width) + '" height="' + str(height) + '" ' + xmlns + viewbox + '>'
        footer = '</svg>'

        svg = header + self.im.content + footer

        with open("overlay.svg", 'w') as f:
            f.write(svg)

        svg2png(url="overlay.svg", write_to="overlay.png")

        olimage = Pim.open("./overlay.png")
        new_image = Pim.new('RGB', (width,height), (250, 250, 250))
        new_image.paste(self.bgimage, (0, 0))
        new_image.paste(olimage, (0, 0), mask=olimage)
        # Displaying the image
        new_image.show()


app.add_static_files('/', '.')

myIM = Image('./baccul.png')
ui.run(port=4040)


