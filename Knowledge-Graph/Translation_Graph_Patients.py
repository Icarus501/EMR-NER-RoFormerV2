import json

from pyecharts import options as opts
from pyecharts.charts import Graph


with open("Translation-Patients.json", "r", encoding="utf-8") as f:
    j = json.load(f)
    nodes = j["nodes"]
    links = j["links"]
    categories = j["categories"]

c = (
    Graph(init_opts=opts.InitOpts(width="700px", height="900px"))
    .add(
        "",
        nodes=nodes,
        links=links,
        categories=categories,
        layout="circular",
        is_rotate_label=True,
        linestyle_opts=opts.LineStyleOpts(color="source", curve=0.2),
        #label_opts=opts.LabelOpts(position="right"),
    )
    #.set_global_opts(
        #title_opts=opts.TitleOpts(title=""),
        #legend_opts=opts.LegendOpts(orient="vertical", pos_left="2%", pos_top="20%"),
    #)
    .render("Graph_patients_Translation.html")
)
