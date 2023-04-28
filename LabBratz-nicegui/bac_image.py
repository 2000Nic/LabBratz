from nicegui import ui
from nicegui.events import MouseEventArguments
from Blob_detector import Blob_Detector
from marker import Marker
from PIL import Image as Pim
from cairosvg import svg2png
import datetime

class Bac_image:

    def __init__(self, path, upload_new, colortheme='green', automark=True):

        self.bgimage = Pim.open(path)
        self.div = ui.element('div').style("float: right; margin-top: 50px; right: 50px; width: 350px; "
                                           "position: absolute; display: inline-grid;")
        self.keypoints = []
        self.colortheme = colortheme
        self.product_container = ui.element('div').style("float: left; margin-top: 200px; left: 50px; width: 500px; "
                                                         "position: absolute; display: inline-grid;")

        with self.div:
            self.im = ui.interactive_image(path + "?time=" + str(datetime.datetime.now()), on_mouse= self.mouse_handler, cross=True)
            self.add_remove = ui.radio(["Tilføj", "Fjern"], value="Tilføj").props('inline')
            ui.button("Gem som png", on_click=self.save)
            ui.button("Skift billede", on_click=upload_new).style("margin-top: 10px;")

        self.blob_detector = Blob_Detector(path, inv = True)
        self.blob_detect()
        self.draw()


    def blob_detect(self):
        temp_keypts = self.blob_detector.detect()

        for keypt in temp_keypts:
            self.keypoints.append(Marker(keypt.pt[0], keypt.pt[1], self.colortheme))

    def draw(self):
        self.im.set_content(" ")
        for mark in self.keypoints:
            self.im.content += mark.svg()

        self.write_count()

    def mouse_handler(self, e: MouseEventArguments):
        new_mark = Marker(e.image_x, e.image_y, self.colortheme)
        match self.add_remove.value:
            case "Tilføj":
                self.keypoints.append(new_mark)
                self.draw()
            case "Fjern":
                for i, mark in enumerate(self.keypoints):
                    if new_mark.collision(mark):
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

    def write_count(self):
        self.product_container.clear()
        with self.product_container:
            ui.label(str(len(self.keypoints)) + " bakteriekolonier").style("font-size: 20px; font-weight: bold; color: #757575;")

    def get_blob_count(self):
        return len(self.keypoints)




