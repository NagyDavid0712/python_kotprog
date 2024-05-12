import locale

class Product:

    def __init__(self, id, engine_type, main_category, category, product_img, product_img_alt, product_title, product_price, product_description, isAvailable):
        locale.setlocale(locale.LC_ALL, '')
        self._id = id
        self._engine_type = engine_type
        self._main_category = main_category
        self._category = category
        self._product_img = product_img
        self._product_img_alt = product_img_alt
        self._product_title = product_title
        self._product_price = locale.currency(product_price, grouping=True)
        self._product_description = product_description
        self._isAvailable = isAvailable

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, n):
        self._id = n
    
    @property
    def engine_type(self):
        return self._engine_type

    @engine_type.setter
    def engine_type(self, n):
        self._engine_type = n
    
    @property
    def main_category(self):
        return self._main_category

    @main_category.setter
    def main_category(self, n):
        self._main_category = n

    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, n):
        self._category = n

    @property
    def product_img(self):
        return self._product_img
    
    @product_img.setter
    def product_img(self, n):
        self._product_img = n

    @property
    def product_img_alt(self):
        return self._product_img_alt
    
    @product_img_alt.setter
    def product_img_alt(self, n):
        self._product_img_alt = n

    @property
    def product_title(self):
        return self._product_title
    
    @product_title.setter
    def product_title(self, n):
        self._product_title = n

    @property
    def product_price(self):
        return self._product_price
    
    @product_price.setter
    def product_price(self, n):
        self._product_price = locale.currency(n, grouping=True)

    @property
    def product_description(self):
        return self._product_description
    
    @product_description.setter
    def product_description(self, n):
        self._product_description = n
    
    @property
    def isAvailable(self):
        return self._isAvailable
    
    @isAvailable.setter
    def isAvailable(self, n):
        self._isAvailable = n

    