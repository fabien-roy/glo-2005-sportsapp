class Equipment:
    def __init__(self, equipment_id, manufacturer_id, manufacturer_name, type_id, type_name,
                 name, description=None, announces=None):
        self.id = equipment_id
        self.manufacturer_id = manufacturer_id
        self.manufacturer_name = manufacturer_name
        self.type_id = type_id
        self.type_name = type_name
        self.name = name
        self.description = description
        self.announces = [] if announces is None else announces

    def __eq__(self, other):
        if isinstance(other, Equipment):
            return self.id == other.id
        return False
