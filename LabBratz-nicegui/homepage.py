from nicegui import ui
from header import Header


class Homepage:
    def __init__(self):
        ui.colors(primary='#7EC8F2')
        TLC = Card("TLC", "TLC.png", "<p>Med TLC kan du analysere dine<br>TLC analyser og finde RF-værdier<br>&nbsp; <p>", "TLC")
        QDA = Card("QDA", "RadarChart.png", "<p>Med QDA kan du digitalisere dine<br>sensoriske analyser, og effektivisere<br>din databehandling<p>", "QDA")
        Bakterie = Card("Bakterietælling", "Bakterier.png", "<p>Med bakterietælling kan du hurtigere<br>tælle bakteriekolonier på dine plader<br>&nbsp;<p>", "bakterie")
        Header()
        self.title()
        with ui.row().classes('self-center'):
            TLC.card()
            QDA.card()
            Bakterie.card()

    def title(self):
        with ui.column().classes('self-center'):
            ui.label('Velkommen til LabBratz!').classes('text-4xl').classes('self-center')
            ui.label('Med LabBratzz kan du nemt lave alt fra databehandling af en TLC-analyse til QDAer.').classes(
                'text-1xl')


class Card:
    def __init__(self, title, img, tekst, link):
        self.title = title
        self.img = img
        self.tekst = tekst
        self.link = link

    def card(self):
        with ui.card():
            ui.html(f'<img src="./static/{self.img}" style="width: 250px; height: 250px; object-fit: contain;">').classes('self-center')
            with ui.card_section():
                ui.label(self.title).classes('text-2xl')
                ui.html(self.tekst).style('')
            with ui.card_actions():
                ui.button('Gå til ' + self.title, on_click=lambda: ui.open(self.link)).classes('unelevated').style(
                    'box-shadow: none !important;').props('flat')
