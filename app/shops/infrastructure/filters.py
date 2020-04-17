from app.interfaces.infrastructure.filters import MySQLFilter as Filter
from app.shops.infrastructure.tables import MySQLShopTable as Shops


class MySQLShopFilter(Filter):
    def get_col_names(self):
        return [Shops.name_col,
                Shops.email_col,
                Shops.web_site_col,
                Shops.phone_number_col]

    def get_values(self, form=None):
        return [] if form is None else [form.name.data, form.email.data, form.web_site.data,
                                        form.phone_number.data]
