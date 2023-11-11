import json
from excalidraw.canvas import ExcalidrawCanvas
from excalidraw.element import Rectangle

# Create an ExcalidrawCanvas
canvas = ExcalidrawCanvas()

days_count = 7
day_width = 70

hours = 24
hour_height = 10
day_height = hour_height * hours

background_width = day_width * days_count
background_height = day_height

background = Rectangle(width=background_width,
                       height=background_height, background_color="black", opacity=40)
canvas.add_element(background)

# Add a rectangle for each day
for day in range(days_count):
    x = day * day_width
    
    for hour in range(hours):
        y = hour * hour_height
        hour_rectangle = Rectangle(x=x, y=y, width=day_width, height=hour_height)
        canvas.add_element(hour_rectangle)
        
    day_rectangle = Rectangle(x=x, y=0, width=day_width, height=background_height)
    canvas.add_element(day_rectangle)

# Convert the canvas to JSON
canvas_json = canvas.to_json()

# Save the updated canvas JSON to a file with a .excalidraw extension
with open('./output/my_canvas.excalidraw', 'w') as file:
    json.dump(canvas_json, file, indent=4)
