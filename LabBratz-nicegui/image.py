from nicegui import ui
from nicegui.events import MouseEventArguments
from Blob_detector import Blob_Detector
from marker import Marker
import cv2

class Image:

    def __init__(self, path):

        self.im = ui.interactive_image(path, on_mouse= self.mouse_handler, cross=True)
        self.keypoints = []
        self.blob_detector = Blob_Detector(path)
        self.add_remove = ui.radio(["Tilføj", "Fjern"], value="Tilføj").props('inline')
        self.blob_detect()
        self.draw()

    def blob_detect(self):
        temp_keypts = self.blob_detector.detect()

        for keypt in temp_keypts:
            self.keypoints.append(Marker(keypt.pt[0], keypt.pt[1]))

    def draw(self):
        for mark in self.keypoints:
            self.im.content += mark.svg()

    def mouse_handler(self, e: MouseEventArguments):
        print(e.type)
        new_mark = Marker(e.image_x, e.image_y)
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



