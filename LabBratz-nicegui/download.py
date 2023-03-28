from nicegui import ui

class Download:

    def __init__(self, type=""):
        self.type = type
        self.txt = "Download som " + type
        self.button = ui.button(self.txt, on_click=self.run)

    def run(self):

        match self.type:
            case "billede":
                pass
            case "graf":
                pass

