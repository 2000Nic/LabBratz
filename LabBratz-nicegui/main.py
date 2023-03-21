from nicegui import ui
from homepage import Homepage
from qda import QDA
from tlc import TLC
from info import Info
from bakterie import Bakterie

@ui.page('/', title='LabBratz', favicon='./static/icon.png')
def home():
    Homepage()

@ui.page('/QDA', title='QDA', favicon='./static/icon.png')
def qda():
    QDA()

@ui.page('/TLC', title='TLC', favicon='./static/icon.png')
def tlc():
    TLC()

@ui.page('/bakterie', title='Bakterietælling', favicon='./static/icon.png')
def bakterie():
    Bakterie()

@ui.page('/info', title='LabBratz', favicon='./static/icon.png')
def info():
    Info()

ui.run()