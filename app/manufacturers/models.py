class Manufacturer:
    def __init__(self, manufacturer_id, name):
        self.id = manufacturer_id
        self.name = name

    def __eq__(self, other):
        if isinstance(other, Manufacturer):
            return self.id == other.id and self.name == other.name
        return False
