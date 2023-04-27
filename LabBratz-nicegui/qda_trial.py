from nicegui import ui
import json
import io
import os

class QDA_trial:
    def __init__(self):
        self.trial_container = ui.element("div")
        self.qda_start()

        with ui.dialog() as self.dialog, ui.card():
            ui.label("Er du sikker?")
            ui.label("Når du går tilbage kan der ske uforudsete problemer og filkorruptioner.")
            with ui.row():
                ui.button('Gå til startvalg', on_click=lambda: self.dialog.submit('back'))
                ui.button('Gå til igangværende QDA', on_click=lambda: self.dialog.submit('continue'))

    def qda_start(self):
        self.trial_container.clear()
        with self.trial_container:
            ui.label("Åben et nyt forsøg").classes("text-h4")
            trials = []
            for root, dirs, files in os.walk("./saved-setups/"):
                trials.extend((os.path.join("", f) for f in files if f.endswith(".bratz")))
            for trial in trials:
                ui.button(trial.replace(".bratz", ""), on_click=self.qda_load).style("margin-right: 30px;margin-top:10px")

    def qda_load(self, e):
        trialfile = io.open("./saved-setups/" + str(e.sender.text) + ".bratz", mode="r")
        self.trial_container.clear()
        with self.trial_container.classes("justify-between items-center").style("width:100%"):
            top_container = ui.element("div").style("display: inline")
            with top_container:
                ui.button("Tilbage", on_click=self.back)

            with trialfile:
                data = json.loads(trialfile.read())
                tabs = ui.tabs().classes("self-centered")
                products = data['products']
                params = data['parameters']
                sliders = []
                for j in products:
                    with top_container:
                        with tabs:
                            ui.tab(j)
                    with ui.tab_panels(tabs, value=products[0]):
                        with ui.tab_panel(j):
                            for i in params:
                                ui.label(i['name']).classes("text-h4").style("margin-top:10px")
                                with ui.row().style("width:100%").classes("justify-between items-center"):
                                    ui.label(i['low'])
                                    slider = ui.slider(min=0, max=15, step=0.01, value=7.5).props("selection-color=transparent",).style("max-width: 80%;margin-top:50px;")
                                    sliders.append(slider)
                                    ui.label(i['high'])
                            if j == products[len(products) - 1]:
                                ui.button("Gem og afslut", on_click=lambda: self.save_and_exit(sliders, products, params, e))

    def save_and_exit(self, sliders, products, params, e):
        filename = e.sender.text
        slider_values = {}
        data = {}
        for idx, product in enumerate(products):
            slider_values[product] = {}
            for param in params:
                slider_values[product][param['name']] = sliders[idx * len(params) + params.index(param)].value
        try:
            with io.open(f"./saved-data/{filename}.bratdat", mode="r") as file:
                data = json.load(file)
        except Exception as exp:
            print(exp)

        if len(data) == 0:
            with io.open(f"./saved-data/{filename}.bratdat", mode="w") as templatefile:
                data['products'] = products
                param_list = []
                for param in params:
                    param_list.append(param['name'])
                data['params'] = param_list
                json.dump(data, templatefile)

        data[len(data) - 2] = slider_values
        with io.open(f"./saved-data/{filename}.bratdat", mode="w", encoding="utf-8") as outfile:
            json.dump(data, outfile)
        self.back()


    async def back(self):
        res = await self.dialog
        if res == "back":
            self.qda_start()
