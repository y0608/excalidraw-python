import json
from excalidraw.canvas import ExcalidrawCanvas
from excalidraw.element import Rectangle

# Create an ExcalidrawCanvas
canvas = ExcalidrawCanvas()

rec1 = Rectangle(x=0, y=0, width=20, height=20)
rec2 = Rectangle(x=30, y=0, width=20, height=20)
rec3 = Rectangle(x=0, y=30, width=20, height=20)
rec4 = Rectangle(x=30, y=30, width=20, height=20)


g1 = canvas.create_group()
g2 = canvas.create_group()
g3 = canvas.create_group()

canvas.add_element(rec1)
canvas.add_element(rec2)
canvas.add_element(rec3)
canvas.add_element(rec4)

rec1.add_to_group(g1)
rec2.add_to_group(g1)


# Convert the canvas to JSON
canvas_json = canvas.to_json()

# Save the updated canvas JSON to a file with a .excalidraw extension
with open('./output/my_canvas_with_groups.excalidraw', 'w') as file:
    json.dump(canvas_json, file, indent=4)
