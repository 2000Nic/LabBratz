from nicegui import ui, app
from nicegui.events import MouseEventArguments
from Blob_detector import Blob_Detector
from marker import Marker
from PIL import Image as Pim
from cairosvg import svg2png
import datetime
import csv
class Image:

    def __init__(self, path, upload_new, colortheme='pink', automark=True):

        self.bgimage = Pim.open(path)
        self.div = ui.element('div').style("float: right; margin-top: 50px; right: 50px; width: 350px; "
                                           "position: absolute; display: inline-grid;")
        self.keypoints = []
        self.colortheme = colortheme
        self.topline = ""
        self.bottomline = ""
        self.topline_y = 0
        self.bottomline_y = 0
        self.rf = []
        self.toggles = ["ID", "Rf", "Begge"]
        self.toggled = "Begge"
        self.product_container = ui.element('div').style("float: left; margin-top: 480px; left: 50px; width: 500px; "
                                                         "position: absolute; display: inline-grid;")

        with self.div:
            self.im = ui.interactive_image(path + "?time=" + str(datetime.datetime.now()), on_mouse= self.mouse_handler, cross=True)
            with ui.row():
                self.add_remove = ui.radio(["Tilføj", "Fjern"], value="Tilføj").props('inline')
                ui.button("Slet alle", on_click=self.clear_all)
            ui.button("Gem som png", on_click=self.save)
            ui.button("Skift billede", on_click=upload_new).style("margin-top: 10px;")
            ui.button("Gem tabel", on_click=self.save_table).style("margin-top: 10px; margin-bottom: 30px;").props("color='purple'").tooltip("Når du gemmer en tabel kan du finde den som .csv fil i mappen \"saved-tables\" i programmets mappe.")

        self.blob_detector = Blob_Detector(path)
        self.blob_detect()
        self.draw()



    def blob_detect(self):
        temp_keypts = self.blob_detector.detect()

        for keypt in temp_keypts:
            self.keypoints.append(Marker(keypt.pt[0], keypt.pt[1], self.colortheme))

    def draw(self):
        self.im.set_content(" ")
        self.rf = []
        for i, mark in enumerate(self.keypoints):
            self.im.content += mark.svg()
            try:
                front = self.bottomline_y - self.topline_y
                relative = self.bottomline_y - mark.posy
                self.rf.append({"Data ID": i+1, "Rf-værdi": relative / front})
                x = 'x="' + str(mark.posx - 30) + '" '
                y = 'y="' + str(mark.posy) + '" '
                text=" "

                match self.toggled:
                    case "ID":
                        text = "id:" + str(i+1)
                    case "Rf":
                        text = "rf:" + str(round(relative / front, 2))
                    case "Begge":
                        text = "id:" + str(i+1) + " rf:" + str(round(relative / front, 2))

                self.im.content += '<text ' + x + y + 'class="small">' + text + '</text>'

            except:
                pass
            finally:

                self.im.set_content(self.im.content + self.topline + self.bottomline)
                self.render_table()


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
                       del self.rf[i]
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

    def get_blob_count(self):
        return len(self.keypoints)

    def get_points(self):
        return self.keypoints

    def draw_topline(self, y1: str):
        self.topline = f'<line x1="0" y1="' + y1 + '" x2="' + str(self.bgimage.size[0]) + '" y2="' \
                          + y1 + '" style="stroke:rgb(0,0,0);stroke-width:2"/>'
        self.topline_y = int(y1)
        self.draw()

    def draw_bottom_line(self, y1: str):

        self.bottomline = f'<line x1="0" y1="' + y1 + '" x2="' + str(self.bgimage.size[0]) + '" y2="'\
                          + y1 + '" style="stroke:rgb(0,0,0);stroke-width:2"/>'
        self.bottomline_y = int(y1)
        self.draw()

    def render_table(self):
        self.product_container.clear()
        columns = [
            {'name': 'Data ID', 'label': 'Data ID', 'field': 'Data ID', 'required': True, 'align': 'center'},
            {'name': 'Rf-værdi', 'label': 'Rf-værdi', 'field': 'Rf-værdi', 'required': True, 'sortable': True},
        ]
        rows = self.rf
        with self.product_container:
            ui.table(columns=columns, rows=rows, row_key='name', pagination=2)

    def update_view(self, i: int):
        self.toggled = self.toggles[int(i)]
        self.draw()

    def save_table(self):
        with open("./saved-tables/table.csv", 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=["Data ID", "Rf-værdi"])
            writer.writeheader()
            writer.writerows(self.rf)

    def clear_all(self):
        self.keypoints = []
        self.draw()


