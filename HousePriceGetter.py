from builtins import print

from bs4 import BeautifulSoup
from RealEstateProperty import RealEstateProperty
import requests
import re
from time import sleep


class HoursePriceGetter():

    def __init__(self, suburb, state, proptype="", minbed="", maxbed=""):
        self.__suburb = suburb.replace(" ", "%20")
        self.__address = 'http://house.ksou.cn/p.php?q=' + suburb + '&s=1&st=&type=' + proptype + '&region=' + suburb + '&sta=' + state + '&agent=0&minprice=&maxprice=&minbed=' + minbed + '&maxbed=' + maxbed + '&minland=&maxland='
        print(self.__address)
        self.__source = ""
        self.__source = requests.get(self.__address).text
        # while self.__source == "":
        #     try:
        #         print("trying again")
        #         self.__source = requests.get(self.__address).text
        #         break
        #     except:
        #         sleep(1)
        self.__source = requests.get(self.__address).text
        self.__soup = BeautifulSoup(self.__source, 'lxml')
        self.__ppty_list = self.__soup.findAll('table', id=re.compile('^r'))
        self.__property_list = []
        self.attributeParser()

    def attributeParser(self):
        ppty_list = self.__ppty_list
        for ppty in ppty_list:
            address = ppty.findAll('a')[2].text
            attr_list = ppty.findAll('b')
            first_line = attr_list[0].parent.text.split(" ")
            sold_price = first_line[1]
            year = first_line[-1].split("(")[0]
            month = first_line[-2]
            if len(first_line) == 5:
                day = ""
            else:
                day = first_line[-3]
            attr_list = attr_list[1:]
            attr = ""
            attr = attr_list[0].parent.text.lower().split(" ")
            last_sold = ""
            last_sold_month = ""
            last_sold_year = ""
            rent = ""
            while ":" not in attr[0]:
                if 'rent' in attr:
                    rent = attr[1]
                    rent_year = attr[-1]
                    rent_month = attr[-2]
                elif "last" in attr:
                    last_sold = attr[2]
                    last_sold_year = attr[-1].split("(")[0].title()
                    last_sold_month = attr[-2].title()
                attr_list = attr_list[1:]
                attr = attr_list[0].parent.text.lower().split(" ")
            property_type = attr[0][:-1].title()
            beds = attr[1]
            bathrooms = attr[3]
            if len(attr) == 6:
                car_spaces = ""
            else:
                car_spaces = attr[5]
            if len(attr_list) > 0:
                attr_list = attr_list[1:]
            agent = ""
            land_size = ""
            building_size = ""
            while len(attr_list) > 0:
                attr = attr_list[0].parent.text.lower()
                if "agent" in attr:
                    agent = attr.split(": ")[1].title()
                elif "land" in attr:
                    land_size = attr.split(" ")[2]
                    if "building" in attr:
                        building_size = attr.split(" ")[7]
                elif "building" in attr:
                    building_size = attr.split(" ")[7]
                if len(attr_list) > 0:
                    attr_list = attr_list[1:]
            rpropty = RealEstateProperty(address=address,
                                         sold_price=sold_price,
                                         type = property_type,
                                         bedrooms=beds,
                                         bathrooms=bathrooms,
                                         car_spaces=car_spaces,
                                         sold_day=day,
                                         sold_month=month,
                                         sold_year=year,
                                         agent=agent,
                                         land_size=land_size,
                                         building_size=building_size,
                                         last_sold_price=last_sold,
                                         last_sold_month=last_sold_month,
                                         last_sold_year=last_sold_year)
            self.__property_list.append(rpropty)


    @property
    def ppty_list(self):
        return self.__property_list