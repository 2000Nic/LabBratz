from nicegui import ui
import json
import io
import os
from radarcharts import Radarchart

class QDA_data:
    def __init__(self):
        self.data_container = ui.element("div")
        self.qda_data_choose()

    def qda_data_choose(self):
        self.data_container.clear()
        with self.data_container:
            heading = ui.label("Åben data for et forsøg").classes("text-h4")
            trials = []
            for root, dirs, files in os.walk("./saved-data/"):
                trials.extend((os.path.join("", f) for f in files if f.endswith(".bratdat")))
            for trial in trials:
                ui.button(trial.replace(".bratdat", ""), on_click=self.qda_data_load).style("margin-right: 30px;margin-top:10px")

    def qda_data_load(self, e):
        values = {}

        filename = str(e.sender.text)
        trialdatafile = io.open(f"./saved-data/{filename}.bratdat", mode="r")
        with trialdatafile:
            raw_data = json.loads(trialdatafile.read())
            params = raw_data['params']
            products = raw_data['products']
            value_count = len(raw_data) - 2
            for product in products:
                values[product] = {}
                for param in params:
                    values[product][param] = 0
            for i in range(len(raw_data) - 2):
                datapoint = raw_data[str(i)]
                for product in products:
                    for param in params:
                        values[product][param] += datapoint[product][param]
                        if i == len(raw_data) - 3:
                            values[product][param] = values[product][param] / value_count
        self.qda_data_show(values, products, params)

    def qda_data_show(self, vals, products, params):
        self.data_container.clear()
        chart_maker = Radarchart()
        with self.data_container.classes("justify-between items-center"):
            # ALLE PRODUKTER I EN CHART #
            all_vals = []
            for product in products:
                temp_val = []
                for param in params:
                    temp_val.append(vals[product][param])
                all_vals.append(temp_val)
            chart_maker.make_chart("QDA Alle produkter", params, all_vals, True, products)
            # SLUT ALLE PROODUKTER I EN CHART #
            # INDIVIDUELLE CHARTS #
            for product in products:
                val_to_show = []
                temp_val = []
                for param in params:
                    temp_val.append(vals[product][param])
                val_to_show.append(temp_val)
                chart_maker.make_chart(f"Diagram for {product}", params, val_to_show, False, product)
            # SLUT INDIVIDUELLE CHARTS#

