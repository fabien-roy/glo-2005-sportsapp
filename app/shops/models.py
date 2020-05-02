class Shop:
    def __init__(self, shop_id, name, email=None, phone_number=None, web_site=None, announces=None):
        self.id = shop_id
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.web_site = web_site
        self.announces = [] if announces is None else announces

    def __eq__(self, other):
        if isinstance(other, Shop):
            return self.id == other.id
        return False
