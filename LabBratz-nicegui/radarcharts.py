from nicegui import ui
import plotly.graph_objects as go
class Radarchart:
    def __init__(self):
        pass
    def make_chart(self, nam, cats, vals, show_trace_name, trace_nams):
        #Determines weather the traces are filled in
        #filling = 'none'
        #if infill:
        #    filling='toself'
        #Copies first point and adds as last point in each trace, so the trace closes
        cats.append(cats[0])
        for n in vals:
            n.append(n[0])
        #Makes the graph
        figure = go.Figure()
        if show_trace_name:
            for i,n in enumerate(vals):
                figure.add_trace(go.Scatterpolar(r=n,theta=cats,dr=1, showlegend=show_trace_name, name=trace_nams[i]))
        else:
            for i,n in enumerate(vals):
                figure.add_trace(go.Scatterpolar(r=n,theta=cats,dr=1, showlegend=show_trace_name))
        figure.update_layout(
            title=go.layout.Title(text=nam),
            polar={'radialaxis': {'visible': True}},
            showlegend=True
        )
        figure.update_polars(radialaxis=dict(range=[0, 15]))
        return ui.plotly(figure).style("width: 45%")
yolo = Radarchart()
yolo.make_chart('SUP!',['Till a mans not hot', 'Noice dude', 'Wollah wollah, ingen bollah', 'Yo mama'],[[1,4,10,15],[3,2,8,4]],False,False)
ui.run()