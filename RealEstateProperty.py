class RealEstateProperty():

    def __init__(self,
                 address,
                 sold_price,
                 sold_month,
                 sold_year,
                 sold_day = "",
                 last_sold_month = None,
                 last_sold_year = None,
                 last_sold_price=None,
                 rent=None,
                 type=None,
                 land_size=None,
                 building_size=None,
                 agent=None,
                 link=None,
                 bedrooms=None,
                 bathrooms=None,
                 car_spaces=None):

        self.__address = address
        self.__sold_price = sold_price
        self.__last_sold_price = last_sold_price
        self.__rent = rent
        self.__type = type
        self.__land_size = land_size
        self.__building_size = building_size
        self.__agent = agent
        self.__link = link
        self.__bedrooms = bedrooms
        self.__bathrooms = bathrooms
        self.__car_spaces = car_spaces
        self.__sold_date = sold_day + " " + sold_month + " " + sold_year
        self.__last_sold_date = last_sold_month + " " + last_sold_year

    @property
    def address(self):
        return self.__address

    @property
    def sold_price(self):
        return self.__sold_price

    @property
    def last_sold_price(self):
        return self.__last_sold_price

    @property
    def rent(self):
        return self.__rent

    @property
    def type(self):
        return self.__type

    @property
    def land_size(self):
        return self.__land_size

    @property
    def building_size(self):
        return self.__building_size

    @property
    def agent(self):
        return self.__agent

    @property
    def link(self):
        return self.__link

    @property
    def bedrooms(self):
        return self.__bedrooms

    @property
    def bathrooms(self):
        return self.__bathrooms

    @property
    def car_spaces(self):
        return self.__car_spaces

    @property
    def sold_date(self):
        return self.__sold_date

    @property
    def last_sold_date(self):
        return self.__last_sold_date
