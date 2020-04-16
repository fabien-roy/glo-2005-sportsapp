class Equipment:
    def __init__(self, equipment_id, category, name, description=None):
        self.id = equipment_id
        self.category = category
        self.name = name
        self.description = description

    def __eq__(self, other):
        if isinstance(other, Equipment):
            return self.id == other.id
        return False
