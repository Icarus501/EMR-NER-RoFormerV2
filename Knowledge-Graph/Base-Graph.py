from pyecharts import options as opts
from pyecharts.charts import Graph

nodes_data = {
    opts.GraphNode(name="患者1", symbol_size=50),
    opts.GraphNode(name="解剖部位",symbol_size=40),
    opts.GraphNode(name="疾病与诊断",symbol_size=40),
    opts.GraphNode(name="药物",symbol_size=40),
    opts.GraphNode(name="手术",symbol_size=40),
    opts.GraphNode(name="影像检查",symbol_size=40),
    opts.GraphNode(name="实验室检验",symbol_size=40),
    #opts.ItemStyleOpts(color="blue")
    opts.GraphNode(name="胃癌",symbol_size=20),
}

links_data = {
    opts.GraphLink(source="解剖部位",target="患者1"),
    opts.GraphLink(source="疾病与诊断",target="患者1"),
    opts.GraphLink(source="药物",target="患者1"),
    opts.GraphLink(source="手术",target="患者1"),
    opts.GraphLink(source="影像检查",target="患者1"),
    opts.GraphLink(source="实验室检验",target="患者1"),
    opts.GraphLink(source="胃癌",target="疾病与诊断"),
}

c = (
    Graph()
    .add(
        "categories",
        nodes_data,
        links_data,
        repulsion=8000,
        edge_label=opts.LabelOpts(
            is_show=True,position="middle",formatter="诊疗项目"
        ),
        #itemstyle_opts=opts.ItemStyleOpts(color="blue")
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Graph-GraphNode-GraphLink-WithEdgeLabel")
    )
    .render("graph_with_edge_options.html")
)