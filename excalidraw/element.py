class ExcalidrawElement:
    def __init__(self, element_type, x=0, y=0, width=10, height=10):
        self.element = {
            "type": element_type,
            "version": 52,
            "versionNonce": 1547174344,
            "isDeleted": False,
            "id": "PTRZzVwelfDdRSHcaH9_6",
            "fillStyle": "hachure",
            "strokeWidth": 1,
            "strokeStyle": "solid",
            "roughness": 1,
            "opacity": 100,
            "angle": 0,
            "x": x,
            "y": y,
            "strokeColor": "#000000",
            "backgroundColor": "transparent",
            "width": width,
            "height": height,
            "seed": 1191301006,
            "groupIds": [],
            "frameId": None,
            "roundness": {"type": 3},
            "boundElements": [],
            "updated": 1697050228770,
            "link": None,
            "locked": False
        }

    def to_json(self):
        return self.element

class Rectangle(ExcalidrawElement):
    def __init__(self, x=0, y=0, width=10, height=10):
        super().__init__("rectangle", x, y, width, height)
