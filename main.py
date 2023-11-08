import json
from excalidraw.canvas import ExcalidrawCanvas
from excalidraw.element import Rectangle

# Create a Rectangle instance
my_rectangle = Rectangle(x=10, y=20, width=30, height=40)

# Create an ExcalidrawCanvas and add the rectangle to it
canvas = ExcalidrawCanvas()
canvas.add_element(my_rectangle)

# Convert the canvas to JSON
canvas_json = canvas.to_json()

# Save the canvas JSON to a file or send it to Excalidraw
with open('./output/my_canvas.json', 'w') as file:
    json.dump(canvas_json, file, indent=4)
