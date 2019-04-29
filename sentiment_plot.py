from plotly.offline import plot
from plotly.graph_objs import Pie

# adapted from samples in https://plot.ly/python/pie-charts/
def sentiment_plot(sentiment1, sentiment2):
    fig = {
          "data": [{ "values": [sentiment1[0], sentiment1[1], sentiment1[2]], # input first article sentiment values
          "labels": ["Positive", "Negative", "Neutral",], # input labels
          'marker': {'colors': ['rgb(230, 25, 25)', # input chart colors
                                'rgb(38, 39, 40)',
                                'rgb(66, 134, 244)']},
          "domain": {"x": [0, .48]},
          "name": "Article 1",
          "textfont": {"color": '#ffffff'}, # make label text white
          "hoverinfo":"label+percent+name", # add hover info label
          "hole": .4, # set size of donut hole
          "type": "pie" # pie chart
           },
           {
           "values": [sentiment2[0], sentiment2[1], sentiment2[2]], # input second article sentiment values
           "labels": [
           "Positive",
           "Negative",
           "Neutral",
           ],
           "text":"Article 2",
           "textposition":"inside",
           "textfont": {"color": '#ffffff'},
           "domain": {"x": [.52, 1]},
           "name": "Article 2",
           "hoverinfo":"label+percent+name",
           "hole": .4,
           "type": "pie"
           }],
           "layout": {
            "width": 700, # set width of chart
            "annotations": [
            {
                "font": {
                    "size": 20
                },
                "showarrow": False,
                "text": "Article 1",
                "x": 0.15, # set inner label position for article 1
                "y": 0.5
                },
                {
                "font":
                    {
                    "size": 20
                    },
                "showarrow": False,
                "text": "Article 2",
                "x": 0.85, # set inner label position for article 2
                "y": 0.5
                }]
                }
            }
    my_plot_div = plot(fig, output_type='div')

    return my_plot_div
