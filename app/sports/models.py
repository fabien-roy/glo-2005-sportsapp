class Sport:
    def __init__(self, sport_id, name, climates=None, required_equipment_types=None,
                 recommendations=None):
        self.id = sport_id
        self.name = name
        self.climates = [] if climates is None else climates
        self.required_equipment_types = [] if required_equipment_types is None else \
            required_equipment_types
        self.recommendations = [] if recommendations is None else recommendations

    def __eq__(self, other):
        if isinstance(other, Sport):
            return self.id == other.id
        return False
