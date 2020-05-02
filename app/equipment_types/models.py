class EquipmentType:
    def __init__(self, type_id, name):
        self.id = type_id
        self.name = name

    def __eq__(self, other):
        if isinstance(other, EquipmentType):
            return self.id == other.id
        return False
