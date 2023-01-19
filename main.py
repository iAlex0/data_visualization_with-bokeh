from bokeh.plotting import figure, output_file, show, save, ColumnDataSource
from bokeh.models import HoverTool
from bokeh.transform import factor_cmap
from bokeh.palettes import Blues8
from bokeh.embed import components
import pandas as pd


# Read in csv file
df = pd.read_csv("cars.csv")
# car = df["Car"]
# hp = df["Horsepower"]

# Create a ColumnDataSource object
source = ColumnDataSource(df)


output_file("index.html")

#  Car List
car_list = source.data["Car"].tolist()


# add plots
p = figure(
    y_range=car_list,
    min_width=800,
    min_height=600,
    title="Cars with the most horsepower", 
    x_axis_label="Horsepower",
    tools="pan,zoom_in,zoom_out,box_select,reset,save",
)


# Render the glyph
p.hbar(
    y='Car',
    right='Horsepower',
    left=0,
    height=0.4,
    fill_color=factor_cmap(
        'Car', 
        palette=Blues8, 
        factors=car_list,
    ),
    fill_alpha=0.9,
    source=source,
    legend_field="Car",
)

# Add legend
p.legend.orientation = "vertical"
p.legend.location = "top_right"
p.legend.label_text_font_size = "10px"

# Add the HoverTool
hover = HoverTool()
hover.tooltips = """
    <div>
        <h3>@Car</h3>
        <div><strong>Price: </strong> @Price</div>
        <div><strong>Horsepower: </strong> @Horsepower</div>
        <div><img src="@Image" alt="" width="200"/>
    </div>
"""
p.add_tools(hover)

# Show results
# show(p)

# Save results
save(p)

# Print out the script and div
# script, div = components(p)
# print(div)
# print(script)
