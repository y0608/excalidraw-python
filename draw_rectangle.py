import json


# I will make a dictionary and convert it to json later
# IMPORTANT! This will work for now, but with bigger structures we have to load everything in the dict, and thats shit

def draw_rectangle(x, y, width, height):
    # Load the existing JSON data
    with open('./elements/rectangle.json', 'r') as file:
        data = json.load(file)

    # Modify the specific attributes
    data["x"] = x
    data["y"] = y
    data["width"] = width
    data["height"] = height

    # Write the updated data back to the JSON file
    with open('./output/rectangle.json', 'w') as file:
        json.dump(data, file, indent=4)

draw_rectangle(100,100,10,10)