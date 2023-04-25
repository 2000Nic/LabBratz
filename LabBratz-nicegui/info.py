from nicegui import ui
from header import Header


class Info:
    def __init__(self):
        ui.colors(primary='#7EC8F2')
        self.Alfred = Medlem("Alfred", "42069911", "alfred@toiletpaper.dk")
        self.Dona = Medlem("Dona", "42069911", "Dona@toiletpaper.dk")
        self.Nicolas = Medlem("Nicolas", "42069911", "nicolas@toiletpaper.dk")
        self.Phillip = Medlem("Phillip", "42069911", "phillipvad@toiletpaper.dk")

        Header()
        with ui.column().classes('self-center'):
            self.info()
            self.team()

    def info(self):
        with ui.card().tight().classes('self-center'):
            with ui.card_section():
                ui.label('Info om LabBratz').classes('text-4xl')
            with ui.card_section():
                ui.label('LabBratz').classes('text-2xl')
                ui.html('<p>LabBratz er et program lavet til at hjælpe med at analysere data fra forsøg i laboratoriet.</p>'
                        ' <p>LabBratz er lavet af 4 HTX elever fra NEXT Vibenshus</p> ')

            with ui.card_section():
                ui.label('Værktøjer').classes('text-2xl')
                ui.html('<p>TLC: er en metode til at bestemme koncentrationen af en blanding</p>')
                ui.html('<p>QDA: </p>')
                ui.html('<p>Bakterietælling: </p>')

            with ui.card_section():
                ui.label('Kontakt').classes('text-2xl')
                ui.label('Tlf: 12345678').classes('h3')
                ui.label('Mail: labbratz@toiletpaper.dk').classes('h3')

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
