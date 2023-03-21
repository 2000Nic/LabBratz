from nicegui import ui, app

class Header:
    def __init__(self):
        app.add_static_files('/', '.')
        with ui.header(elevated=True).classes('items-center justify-between'):
            ui.interactive_image('./static/logo.png', on_mouse=lambda: ui.open('/')).style('height: auto; width: 100px; margin-right: 60vw; cursor:pointer;')
            ui.button('TLC', on_click=lambda: ui.open('TLC')).style('box-shadow: 0px;border: 0px')
            ui.button('QDA', on_click=lambda: ui.open('QDA')).style('box-shadow:0px;')
            ui.button('Bakterietælling', on_click=lambda: ui.open('bakterie'))
            ui.button('Info', on_click=lambda: ui.open('info'))