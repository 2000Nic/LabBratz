from nicegui import ui
from header import Header


class Homepage:
    def __init__(self):
        ui.colors(primary='#7EC8F2')
        TLC = Card('TLC', 'TLC.png', '<p> TLC er en metode til at bestemme <br> koncentrationen af en blanding<p>',
                   'TLC')
        QDA = Card('QDA', 'RadarChart.png', '<p> QDA er en metode:)<p>', 'QDA')
        Bakterie = Card('Bakterietælling', 'Bakterier.png', '<p> Bakterietælling:)<p>', 'bakterie')

        Header()
        self.title('icon.png')
        with ui.row().classes('self-center'):
            TLC.card()
            QDA.card()
            Bakterie.card()

    def title(self, img):
        with ui.card().classes('self-center'):
            ui.html(f'<img src="./static/{img}" style="width: 250px; height: 250px; object-fit: contain;">').classes(
                'self-center')
            ui.html('<b>Velkommen til LabBratz!</b>').classes('text-4xl').classes('self-center')
            with ui.card_section().classes('self-center'):
                ui.label('Med LabBratzz kan du nemt lave alt fra databehandling af en TLC-analyse til QDAer.').classes(
                    'text-1xl')
            with ui.card_actions():
                ui.button('Gå til Info', on_click=lambda: ui.open('info')).classes('unelevated').style(
                    'box-shadow: none !important;').props('flat')


class Card:
    def __init__(self, title, img, tekst, link):
        self.title = title
        self.img = img
        self.tekst = tekst
        self.link = link

    def card(self):
        with ui.card():
            ui.html(
                f'<img src="./static/{self.img}" style="width: 250px; height: 250px; object-fit: contain;">').classes(
                'self-center')
            with ui.card_section():
                ui.html(f'<b>{self.title}</b>').classes('text-2xl')
                ui.html(self.tekst).style('')
            with ui.card_actions():
                ui.button(f'Gå til {self.title}', on_click=lambda: ui.open(self.link)).classes('unelevated').style(
                    'box-shadow: none !important;').props('flat')
