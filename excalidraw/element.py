from math import pi

class ExcalidrawElement:
    def __init__(self, element_type, x=0, y=0, width=10, height=10, angle_deg=0,
                 stroke_color="#1e1e1e", background_color="transparent", fill_style="hachure",
                 stroke_width=1, stroke_style="solid", roughness=1, opacity=100, roundness=None):
        self.element = {
            "type": element_type,                   # rectangle, diamond, ellipse, arrow, line, text, ...
            "id": None,                             # Set to None as it will be generated later
            "x": x,
            "y": y,
            "width": width,
            "height": height,
            "angle": angle_deg * pi / 180,          # Convert angle to radians
            "strokeColor": stroke_color,
            "backgroundColor": background_color,
            "fillStyle": fill_style,                # hachure, cross-hatch or solid
            "strokeWidth": stroke_width,            # 1,2,4 are the default values
            "strokeStyle": stroke_style,            # solid, dashed or dotted
            "roughness": roughness,                 # 0 - Architect, 1 - Artist, 2 - Cartoonist
            "opacity": max(0, min(100, opacity)),   # Ensure opacity is between 0 and 100
            "groupIds": [],                         # if 2 or more elements have the same group id, they will be grouped together
            "frameId": None,
            "roundness": roundness,
            "seed": None,                           # Set to None as it will be generated later
            "version": None,                        # Set to None as it will be generated later
            "versionNonce": None,                   # Set to None as it will be generated later
            "isDeleted": False,
            "boundElements": None,
            "updated": None,                        # Set to None as it will be generated later
            "link": None,
            "locked": False,
        }

    def add_to_group(self, group_id):
        self.element["groupIds"].append(str(group_id))

    def to_json(self):
        return self.element


class Text(ExcalidrawElement):
    def __init__(self, text="Text", font_size=20, font_family=1, text_align="left", vertical_align="top", baseline=17, **kwargs):
        super().__init__("text", **kwargs)
        self.element.update({
            "text": text,
            "fontSize": font_size,
            "fontFamily": font_family,
            "textAlign": text_align,
            "verticalAlign": vertical_align,
            "baseline": baseline,
        })


class Rectangle(ExcalidrawElement):
    def __init__(self, **kwargs):
        super().__init__("rectangle", **kwargs)


class Diamond(ExcalidrawElement):
    def __init__(self, **kwargs):
        super().__init__("diamond", **kwargs)


class Ellipse(ExcalidrawElement):
    def __init__(self, **kwargs):
        super().__init__("ellipse", **kwargs)


class Arrow(ExcalidrawElement):
    def __init__(self, points, start_arrowhead=None, end_arrowhead=None, **kwargs):
        super().__init__("arrow", **kwargs)
        self.element.update({
            "points": points,
            "startArrowhead": start_arrowhead,
            "endArrowhead": end_arrowhead,
        })


class Line(ExcalidrawElement):
    def __init__(self, points, start_arrowhead=None, end_arrowhead=None, **kwargs):
        super().__init__("line", **kwargs)
        self.element.update({
            "points": points,
            "startArrowhead": start_arrowhead,
            "endArrowhead": end_arrowhead,
        })