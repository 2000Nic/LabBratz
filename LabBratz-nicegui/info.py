from nicegui import ui
from header import Header


class Info:
    def __init__(self):
        ui.colors(primary='#7EC8F2')
        # Medlemmer
        self.Alfred = Medlem("Alfred", "42069911", "alfred@toiletpaper.dk")
        self.Dona = Medlem("Dona", "42069911", "Dona@toiletpaper.dk")
        self.Nicolas = Medlem("Nicolas", "42069911", "nicolas@toiletpaper.dk")
        self.Phillip = Medlem("Phillip", "42069911", "phillipvad@toiletpaper.dk")

        # html
        self.lab = open('about.html', 'r', encoding='utf-8')

        Header()
        with ui.column().classes('self-center'):
            self.info()
            self.team()

    def info(self):
        with ui.card().tight().classes('self-center'):
            with ui.card_section():
                ui.html(self.lab.read())

    def team(self):
        with ui.card().tight().classes('self-center'):
            with ui.card_section():
                ui.label('Teamet bag LabBratz').classes('text-4xl').classes('self-center')
            with ui.row().classes('self-center'):
                self.Alfred.info('<p> Alfred er en idiot</p>')
                self.Dona.info('<p> Dona er en idiot</p>')
                self.Nicolas.info('<p> Nicolas er en idiot</p>')
                self.Phillip.info('<p> Phillip er en idiot</p>')


class Medlem:
    def __init__(self, name, tlf, mail):
        self.name = name
        self.tlf = tlf
        self.mail = mail

    def info(self, tekst):
        with ui.card_section():
            ui.label(self.name).classes('text-2xl')
            ui.label(f"Tlf: {self.tlf}").classes('h3')
            ui.label(f"Mail: {self.mail}").classes('h3')
            ui.html(tekst).classes('self-center')
