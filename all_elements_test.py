import json
from excalidraw.canvas import ExcalidrawCanvas
from excalidraw.element import *

# Create an ExcalidrawCanvas
canvas = ExcalidrawCanvas()

elements = [ 
    Text(text="this is text", x=78.47, y=141.93, width=116.44, height=25, font_size=20),
    Rectangle(x=52.08, y=69.01, width=119.44, height=41.02),
    Diamond(x=231.25, y=60.68, width=32.64, height=27.13),
    Ellipse(x=236.11, y=143.32, width=43.75, height=72.27),
    Arrow(x=309.72, y=74.57, width=52.78, height=102.82, points=[[0, 0], [52.78, 102.82]], end_arrowhead="arrow"),
    Line(x=368.06, y=75.26, width=61.81, height=111.85, points=[[0, 0], [61.81, 111.85]])
]

canvas.add_elements(elements)

# Convert the canvas to JSON
canvas_json = canvas.to_json()

# Save the updated canvas JSON to a file with a .excalidraw extension
with open('./output/my_canvas.excalidraw', 'w') as file:
    json.dump(canvas_json, file, indent=4)
