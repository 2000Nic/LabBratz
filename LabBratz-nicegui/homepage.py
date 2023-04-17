from nicegui import ui
from header import Header

class Homepage:
    def __init__(self):
        ui.colors(primary='#7EC8F2')
        Header()

        self.title()

    def title(self):
        with ui.column().classes('self-center'):
            ui.label('Velkommen til LabBratz!').classes('text-4xl')
            ui.label('Med LabBratzz kan du nemt lave alt fra databehandling af en TLC-analyse til QDAer.').classes(
                'text-1xl')

            with ui.row().classes('self-center'):
                with ui.card().tight():
                    ui.html('<img src="./static/TLC.png" style="width: 250px; height: 250px; object-fit: contain;">')
                    ui.label('TLC').classes('text-2xl')

                    with ui.column().classes('self-center'):
                        TLC_About = {
                            1: 'TLC er en metode til at bestemme sammensætningen af en blanding.',
                            2: 'Vores App tilbyder automatisk markering af analyser.',
                        }

                        for key, value in TLC_About.items():
                            ui.label(value).classes('h3')

                    ui.button('Gå til TLC', on_click=lambda: ui.open('TLC')).classes('unelevated').style('box-shadow: none !important;')

                with ui.card().tight():
                    ui.html('<img src="./static/RadarChart.png" style="width: 250px; height: 250px; object-fit: contain;">')
                    ui.label('QDA').classes('text-2xl')
                    ui.label('QDA').classes('text-1xl')
                    ui.button('Gå til QDA', on_click=lambda: ui.open('QDA')).classes('unelevated').style('box-shadow: none !important;')

                with ui.card().tight():
                    ui.html('<img src="./static/Bakterier.png" style="width: 250px; height: 250px; object-fit: contain;">')
                    ui.label('Bakterietælling').classes('text-2xl')
                    ui.label('Automatisk optælling af bakterie kolonier').classes('text-1xl')
                    ui.button('Gå til Bakterietælling', on_click=lambda: ui.open('bakterie')).classes('unelevated').style('box-shadow: none !important;')
