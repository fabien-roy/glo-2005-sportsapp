class Shop:
    def __init__(self, shop_id, name, email=None, phone_number=None, web_site=None):
        self.id = shop_id
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.web_site = web_site

    def __eq__(self, other):
        if isinstance(other, Shop):
            return self.id == other.id
        return False
