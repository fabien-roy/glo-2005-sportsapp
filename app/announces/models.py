class Announce:
    def __init__(self, announce_id, shop_id, shop_name, equipment_id, equipment_name, state, price,
                 date=None):
        self.id = announce_id
        self.shop_id = shop_id
        self.shop_name = shop_name
        self.equipment_id = equipment_id
        self.equipment_name = equipment_name
        self.state = state
        self.price = price
        self.date = date

    def __eq__(self, other):
        if isinstance(other, Announce):
            return self.id == other.id
        return False
