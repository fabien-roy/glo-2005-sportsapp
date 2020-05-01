class Sport:
    def __init__(self, sport_id, name, climates=None, recommendations=None,
                 required_equipment_types=None):
        self.id = sport_id
        self.name = name
        self.climates = [] if climates is None else climates
        self.recommendations = [] if recommendations is None else recommendations
        self.required_equipment_types = [] if required_equipment_types is None else \
            required_equipment_types

    def __eq__(self, other):
        if isinstance(other, Sport):
            return self.id == other.id
        return False
