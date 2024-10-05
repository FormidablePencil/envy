class ComponentRegistry:
    def __init__(self):
        self.registered_components = {}

    def register_component(self, name, component):
        self.registered_components[name] = component

    def get_components(self):
        return self.registered_components

    def is_compatible(self, name, component):
        # Implement version and dependency checking logic here
        return True