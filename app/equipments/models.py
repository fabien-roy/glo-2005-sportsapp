class Equipment:
    def __init__(self, equipment_id, category, name, description=None, announces=None):
        self.id = equipment_id
        self.category = category
        self.name = name
        self.description = description
        self.announces = [] if announces is None else announces

    def __eq__(self, other):
        if isinstance(other, Equipment):
            return self.id == other.id
        return False

    def add_announce(self, announce):
        self.announces.append(announce)
