from math import pi


class ExcalidrawElement:
    def __init__(self, element_type, fill_style="hachure", stroke_width=1,
                 stroke_style="solid", roughness=1, opacity=100, angle_deg=0, 
                 x=0, y=0, stroke_color="#1e1e1e", background_color="transparent", width=5, height=5, roundness=False):
        angle_rad = angle_deg * pi / 180  # Convert angle to radians
        self.element = {
            "type": element_type,
            "version": 52,
            "versionNonce": 1547174344,
            "isDeleted": False,
            "id": "PTRZzVwelfDdRSHcaH9_6",
            "fillStyle": fill_style,                # hachure, cross-hatch or solid
            "strokeWidth": stroke_width,
            "strokeStyle": stroke_style,            # solid, dashed or dotted
            "roughness": roughness,                 # 0 - Architect, 1 - Artist, 2 - Cartoonist
            "opacity": max(0, min(100, opacity)),   # Ensure opacity is between 0 and 100
            "angle": angle_rad,
            "x": x,
            "y": y,
            "strokeColor": stroke_color,
            "backgroundColor": background_color,
            "width": width,
            "height": height,
            "seed": 1191301006,
            "groupIds": [],
            "frameId": None,
            "roundness": {"type": 3} if roundness else {"type": 0},
            "boundElements": [],
            "updated": 1697050228770,
            "link": None,
            "locked": False
        }

    def to_json(self):
        return self.element


class Rectangle(ExcalidrawElement):
    def __init__(self, **kwargs):
        super().__init__("rectangle", **kwargs)
