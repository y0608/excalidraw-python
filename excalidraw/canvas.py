class ExcalidrawCanvas:
    def __init__(self, gridSize=None, backgroundColor="#ffffff"):
        self.elements = []
        self.canvas_json = {
            "type": "excalidraw",
            "version": 2,
            "source": "https://excalidraw.com",
            "elements": self.elements,
            "appState": {
                "gridSize": gridSize,
                "viewBackgroundColor": backgroundColor
            },
            "files": {}
        }

    def add_element(self, element):
        self.elements.append(element.to_json())

    def to_json(self):
        return self.canvas_json
