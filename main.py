import json
from excalidraw.canvas import ExcalidrawCanvas
from excalidraw.element import Rectangle

# Create an ExcalidrawCanvas
canvas = ExcalidrawCanvas()

# Create a Rectangle instance and add it to the canvas
my_rectangle = Rectangle(x=0, y=0, width=100, height=100, angle_deg=90, roundness=True)

canvas.add_element(my_rectangle)

# Convert the canvas to JSON
canvas_json = canvas.to_json()

# Save the updated canvas JSON to a file with a .excalidraw extension
with open('./output/my_canvas.excalidraw', 'w') as file:
    json.dump(canvas_json, file, indent=4)
