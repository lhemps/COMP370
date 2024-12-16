from bokeh.io import curdoc
from bokeh.layouts import column
from bokeh.models import Select
from bokeh.plotting import figure
import pandas as pd


df = pd.read_csv('monthly_avg_response_times.csv', parse_dates=['month'])
df['incident_zip'] = df['incident_zip'].astype(str)

zipcode_options = sorted(df['incident_zip'].unique().tolist())

zipcode1_select = Select(title="Zipcode 1", options=zipcode_options, value="10001")
zipcode2_select = Select(title="Zipcode 2", options=zipcode_options, value="10002")

p = figure(title="Monthly Response Times", x_axis_type="datetime", height=400, width=700)
p.xaxis.axis_label = "Month"
p.yaxis.axis_label = "Response Time (Hours)"

# Ensure data is sorted by month
df = df.sort_values('month')

# Initial plot for all data
all_data = df.groupby('month')['response_time_hours'].mean().reset_index()
p.line(all_data['month'], all_data['response_time_hours'], line_width=2, color='gray', legend_label="All Data")

# Plot for the first selected zipcodes
zipcode1_data = df[df['incident_zip'] == zipcode1_select.value]
zipcode2_data = df[df['incident_zip'] == zipcode2_select.value]
line_zip1 = p.line(zipcode1_data['month'], zipcode1_data['response_time_hours'], line_width=2, color='blue', legend_label=f"Zipcode {zipcode1_select.value}")
line_zip2 = p.line(zipcode2_data['month'], zipcode2_data['response_time_hours'], line_width=2, color='green', legend_label=f"Zipcode {zipcode2_select.value}")

p.legend.location = "top_left"
p.legend.label_text_font_size = '10pt'
p.legend.orientation = "horizontal"
p.add_layout(p.legend[0], 'below')

def update_plot(attr, old, new):
    # Update data for Zipcode 1
    zipcode1_data = df[df['incident_zip'] == zipcode1_select.value]
    line_zip1.data_source.data = {'x': zipcode1_data['month'], 'y': zipcode1_data['response_time_hours']}

    # Update data for Zipcode 2
    zipcode2_data = df[df['incident_zip'] == zipcode2_select.value]
    line_zip2.data_source.data = {'x': zipcode2_data['month'], 'y': zipcode2_data['response_time_hours']}

    p.legend.items = [
        ('All Data', [p.renderers[0]]),
        (f"Zipcode {zipcode1_select.value}", [line_zip1]),
        (f"Zipcode {zipcode2_select.value}", [line_zip2])
    ]

# Attach the update function to the dropdowns
zipcode1_select.on_change('value', update_plot)
zipcode2_select.on_change('value', update_plot)

# Define the layout and attach it to the document
layout = column(zipcode1_select, zipcode2_select, p)
curdoc().add_root(layout)
curdoc().title = "NYC 311 Dashboard"