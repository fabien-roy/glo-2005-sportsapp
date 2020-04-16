class Announce:
    def __init__(self, announce_id, shop_id, equipment_id, state, price, date=None):
        self.id = announce_id
        self.shop_id = shop_id
        self.equipment_id = equipment_id
        self.state = state
        self.price = price
        self.date = date

    def __eq__(self, other):
        if isinstance(other, Announce):
            return self.id == other.id
        return False
