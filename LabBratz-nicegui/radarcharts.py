from nicegui import ui
import plotly.graph_objects as go
class Radarchart:
    def __init__(self):
        pass
    def make_chart(self, nam, cats, vals,infill):
        #Determines weather the traces are filled in
        filling = 'none'
        if infill:
            filling='toself'
        #Copies first point and adds as last point in each trace, so the trace closes
        cats.append(cats[0])
        for n in vals:
            n.append(n[0])
        #Makes the graph
        figure = go.Figure()
        for n in vals:
            figure.add_trace(go.Scatterpolar(r=n,theta=cats,dr=1, fill=filling))
        figure.update_layout(
            title=go.layout.Title(text=nam),
            polar={'radialaxis': {'visible': True}},
            showlegend=True
        )
        figure.update_polars(radialaxis=dict(range=[0, 15]))
        return ui.plotly(figure).style("width: 45%")
yolo = Radarchart()
yolo.make_chart('SUP!',['Till a mans not hot', 'Noice dude', 'Wollah wollah, ingen bollah', 'Yo mama'],[[1,2,3,4],[3,2,1,4]],False)
ui.run()