from nicegui import ui
import json
import io

class QDA_setup:
    params = [{'low': 'Ikke sur', 'name': 'Surhed', 'high': 'Meget sur'}]
    products = ['Æble 1']
    param_container = ui.element('div')
    product_container = ui.element('div')
    QDA_name = "Nyt forsøg"

    def __init__(self):
        ui.label("Indstillinger for QDA").classes("text-h3")
        ui.input("QDA Navn", value=self.QDA_name, on_change=lambda e: self.update_name(e.value))
        self.param_container = ui.element('div').style("margin-top: 20px")
        self.render_params()
        ui.button("Tilføj parameter", on_click=lambda: self.add_param()).style("margin-top: 20px")
        self.product_container = ui.element('div').style("margin-top: 20px; display: block")
        self.render_products()
        ui.button("Tilføj produkt", on_click=lambda: self.add_product()).style("margin-top: 20px")
        ui.element("br")
        ui.button("Gem forsøg", on_click=lambda: self.save_QDA()).style("margin-top: 20px")

    def render_params(self):
        with self.param_container:
            self.param_container.clear()
            for i in range(len(self.params)):
                with ui.element('div').classes("items-center justify-between").style("width: 70vw; display: inline-flex"):
                    param = self.params[i]
                    ui.input('Parameternavn', value=param['name'], on_change=lambda e: self.update_param(i, 'name', e.value)).style("width: 25%")
                    ui.input('Laveste værdi', value=param['low'], on_change=lambda e: self.update_param(i,'low', e.value)).style("width: 25%")
                    ui.input('Højeste værdi', value=param['high'], on_change=lambda e: self.update_param(i,'high', e.value)).style("width: 25%")
                    ui.button(on_click=lambda: self.remove_param(i)).props("icon=highlight_off flat color=primary")

    def update_name(self, v):
        self.QDA_name = v
        print(self.QDA_name)

    def remove_param(self, i):
        del self.params[i]
        self.render_params()

    def add_param(self):
        self.params.append({'low': '', 'name': '', 'high': ''})
        self.render_params()

    def update_param(self, i, k, v):
        self.params[i][k] = v

    def render_products(self):
        with self.product_container:
            self.product_container.clear()
            for i in range(len(self.products)):
                with ui.element('div').classes("items-center justify-between").style("width: 25vw; display: inline-flex"):
                    product = self.products[i]
                    ui.input(f'Produkt {i+1}', value=product, on_change=lambda e: self.update_product(i, e.value)).style("width: 95%")
                    ui.button(on_click=lambda: self.remove_product(i)).props("icon=highlight_off flat color=primary")

    def remove_product(self, i):
        del self.products[i]
        self.render_products()

    def add_product(self):
        self.products.append('')
        self.render_products()

    def update_product(self, i, v):
        self.products[i] = v

    def save_QDA(self):
        QDA = {"name": self.QDA_name, "parameters": self.params, "products": self.products}
        with io.open(f"./saved-setups/{self.QDA_name}.bratz", mode='w', encoding="utf-8") as outfile:
            json.dump(QDA, outfile)
        print("gemt")