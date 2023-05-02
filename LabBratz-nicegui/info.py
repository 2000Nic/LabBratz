from nicegui import ui
from header import Header


class Info:
    def __init__(self):
        ui.colors(primary='#7EC8F2')

        Header()
        with ui.column().classes('self-center'):
            self.info()

    def info(self):
        with ui.card().tight().classes('self-center').style("width:50%").props("flat"):
            with ui.card_section():
                ui.label('Info om LabBratz').classes('text-4xl')
            with ui.card_section():
                ui.label('LabBratz').classes('text-2xl')
                b = '<br>'
                ui.html(f'<p>LabBratz kan bruges til at automatisere din hverdag i PLS eller andre laboratoriefag. Med LabBratz kan du analysere TLCer uden lineal og lave QDA analyse uden papirarbejde til databehandlingen. <br> LabBratz er lavet af fire HTXere fra Vibenshus Gymnasium i 2023. <br> Programmet er vores officielle asylansøgning til PLS.</p>')
            with ui.card_section():
                ui.label('Værktøjer').classes('text-2xl')
                Expansion("TLC", "Med TLC kan du blot uploade et billede af din TLC og finde RF-værdier med høj nøjagtighed. Du kan også downloade billedet fra programmet til dine rapporter og en tabel med alle RF-værdierne til videre databehandling i Excel.", "science")
                Expansion("QDA", "Med QDA kan du lave sensoriske analyser uden krydser på papir. Programmet laver også automatisk alle dine radar-diagrammer, som kan indsættes direkte i din rapprort.", "psychology")
                Expansion("Bakterietælling", "Med bakterietælling kan du meget hurtigere lave en bakterietælling. Computeren finder selv kolonierne på din agar plade, du skal kun tilfæje eller fjerne, hvis den laver fejl. Og selv hvis du gør det uden automatisk markering husker den i hvert fald hvor langt du er nået og hvilke kolonier du har talt.", "biotech")
            with ui.card_section():
                ui.label('Kontakt').classes('text-2xl')
                with ui.row():
                    ui.icon("memory")
                    ui.label("GitHub:")
                    ui.link("https://github.com/2000Nic/LabBratz", "https://github.com/2000Nic/LabBratz/")
                with ui.row():
                    ui.icon("local_post_office")
                    ui.label('Mail:').classes('h3')
                    ui.link("labbratz@toiletpaper.dk", "mailto:labbratz@toiletpaper.dk")


class Expansion:
    def __init__(self, title, text, icon):
        with ui.expansion(title, icon=icon):
            ui.label(text)
