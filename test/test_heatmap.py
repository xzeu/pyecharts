import random

from example.commons import Faker
from pyecharts import options as opts
from pyecharts.charts import HeatMap


def test_heatmap_base():
    value = [[i, j, random.randint(0, 50)] for i in range(24) for j in range(7)]
    c = (
        HeatMap()
        .add_xaxis(Faker.clock)
        .add_yaxis("series0", Faker.week, value)
        .set_global_opts(visualmap_opts=opts.VisualMapOpts())
    )
    assert c.theme == "white"
    assert c.renderer == "canvas"
    c.render("render.html")
