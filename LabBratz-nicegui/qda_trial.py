from nicegui import ui
import json
import io
import os

class QDA_trial:
    def __init__(self):
        self.trial_container = ui.element("div")
        self.qda_start()
        self.trial_name_or_id = ""

        with ui.dialog() as self.dialog, ui.card():
            ui.label("Er du sikker?")
            ui.label("Når du går tilbage kan der ske uforudsete problemer og filkorruptioner.")
            with ui.row():
                ui.button('Gå til startvalg', on_click=lambda: self.dialog.submit('back'))
                ui.button('Gå til igangværende QDA', on_click=lambda: self.dialog.submit('continue'))

    def qda_start(self):
        self.trial_container.clear()
        with self.trial_container:
            heading = ui.label("Åben et nyt forsøg")
            trials = []
            for root, dirs, files in os.walk("./saved-setups/"):
                trials.extend((os.path.join("", f) for f in files if f.endswith(".bratz")))
            for trial in trials:
                ui.button(trial.replace(".bratz", ""), on_click=self.qda_load)

    def qda_load(self, e):
        trialfile = io.open("./saved-setups/" + str(e.sender.text) + ".bratz", mode="r")
        self.trial_container.clear()
        with self.trial_container.classes("justify-between items-center").style("width:100%"):

            ui.button("Tilbage", on_click=self.back)

            with trialfile:
                data = json.loads(trialfile.read())
                tabs = ui.tabs().classes('self-center')
                products = data['products']
                params = data['parameters']
            for j in data['products']:
                    with tabs:
                        ui.tab(j)
                    with ui.tab_panels(tabs, value=products[0]):
                        with ui.tab_panel(j):
                            for i in params:
                                ui.label(i['name']).classes("text-h4").style("margin-top:10px")
                                with ui.row().style("width:100%").classes("justify-between items-center"):
                                    ui.label(i['low'])
                                    ui.slider(min=0, max=15, step=0.01, value=7.5).props(
                                        "selection-color=transparent").style("max-width: 80%;margin-top:50px;")
                                    ui.label(i['high'])

    async def back(self):
        res = await self.dialog
        if res == "back":
            self.qda_start()
