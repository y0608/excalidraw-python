class ExcalidrawCanvas:
    def __init__(self, gridSize=None, backgroundColor="#ffffff"):
        self.elements = []
        self.groups = []
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
    
    def create_group(self):
        group_id = len(self.groups)
        self.groups.append(group_id)
        return group_id

    def add_element(self, element, group_id=None):
        if group_id is not None:
            element.add_to_group(group_id)
        self.elements.append(element.to_json())

    def to_json(self):
        return self.canvas_json
