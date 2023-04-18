from nicegui import ui
from header import Header


class Homepage:
    def __init__(self):
        ui.colors(primary='#7EC8F2')
        Header()
        self.title()
        self.about_cards()

    def title(self):
        with ui.column().classes('self-center'):
            ui.label('Velkommen til LabBratz!').classes('text-4xl')
            ui.label('Med LabBratzz kan du nemt lave alt fra databehandling af en TLC-analyse til QDAer.').classes(
                'text-1xl')

    def about_cards(self):
            with ui.row().classes('self-center'):
                with ui.card().tight():
                    ui.html('<img src="./static/TLC.png" style="width: 250px; height: 250px; object-fit: contain;">')
                    with ui.card_section():
                        ui.label('TLC').classes('text-2xl')
                        ui.html('<p>TLC er en metode til at bestemme koncentrationen af en blanding</p>')

                    with ui.card_actions():
                        ui.button('Gå til TLC', on_click=lambda: ui.open('TLC')).classes('unelevated').style('box-shadow: none !important;').props("flat")

                with ui.card().tight():
                    ui.html('<img src="./static/RadarChart.png" style="width: 250px; height: 250px; object-fit: contain;">')
                    with ui.card_section():
                        ui.label('QDA').classes('text-2xl')
                        ui.label('QDA er en metode til at bestemme sammensætningen af en blanding.').classes('text-1xl')
                    with ui.card_actions():
                        ui.button('Gå til QDA', on_click=lambda: ui.open('QDA')).classes('unelevated').style('box-shadow: none !important;').props('flat')

                with ui.card().tight():
                    ui.html('<img src="./static/Bakterier.png" style="width: 250px; height: 250px; object-fit: contain;">')
                    with ui.card_section():
                        ui.label('Bakterietælling').classes('text-2xl')
                        ui.label('Automatisk optælling af bakterie kolonier').classes('text-1xl')
                    with ui.card_actions():
                        ui.button('Gå til Bakterietælling', on_click=lambda: ui.open('bakterie')).classes('unelevated').style('box-shadow: none !important;').props('flat')
