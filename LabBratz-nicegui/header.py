from nicegui import ui, app

class Header:
    def __init__(self):
        app.add_static_files('/', '.')
        with ui.header().classes('items-center justify-between'):
            ui.interactive_image('./static/logo.png', on_mouse=lambda: ui.open('/')).style('height: auto; width: 100px; margin-right: 60vw; cursor:pointer;')
            ui.button('TLC', on_click=lambda: ui.open('TLC')).classes('unelevated').style('box-shadow: none !important;')
            ui.button('QDA', on_click=lambda: ui.open('QDA'))
            ui.button('Bakterietælling', on_click=lambda: ui.open('bakterie'))
            ui.button('Info', on_click=lambda: ui.open('info'))