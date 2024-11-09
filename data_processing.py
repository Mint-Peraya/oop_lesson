import csv
import os
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

cities = []
with open(os.path.join(__location__, 'Cities.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        cities.append(dict(r))

countries = []
with open(os.path.join(__location__, 'Countries.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        countries.append(dict(r))


class TableDB:
    def __init__(self):
        self.table_database = []

    def insert(self, table):
        index = self.search(table)
        if index == -1:
            self.table_database.append(table)
        else:
            print(f"{table}: Duplicated account")

    def search(self, table_name):
        for account in self.table_database:
            if account == table_name:
                return account
        return -1


class Table:
    def __init__(self, table_name, table):
        self.table_name = table_name
        self.table = table

    def filter(self, condition):
        filtered_list = []
        for item in self.table:
            if condition(item):
                filtered_list.append(item)
        return filtered_list

    def aggregate(self, aggregation_function, aggregation_key):
        agglist = []
        for item in self.table:
            val = float(item[aggregation_key])
            agglist.append(val)

        return aggregation_function(agglist)

    def __str__(self):
        return f"Table: {self.table_name}, with {len(self.table)}"


city_table = Table("cities", cities)
country_table = Table("countries", countries)
db = TableDB()
db.insert(city_table)
db.insert(country_table)


def cityinct(mycountry):
    ct = city_table.filter(lambda x: x["country"] == mycountry)
    ctinmy = Table(f"{mycountry}_cities", ct)
    db.insert(ctinmy)
    return ctinmy


def testavg(mycountry):
    ctinmy = cityinct(mycountry)
    avg = ctinmy.aggregate(lambda x: sum(x)/len(x), "temperature")
    print(f"The average temperature of all the cities in {mycountry} :")
    print(avg)
    print()


def test_minmax(mycountry, choice):
    ctinmy = cityinct(mycountry)
    maxt = ctinmy.aggregate(lambda x: max(x), "temperature")
    mint = ctinmy.aggregate(lambda x: min(x), "temperature")
    if choice == "min":
        print(f"The minimum temperature of all the cities in {mycountry} :")
        print(mint)
    elif choice == "max":
        print(f"The maximum temperature of all the cities in {mycountry} :")
        print(maxt)
    print()


def all_maxmin_latitude(choice):
    maxl = city_table.aggregate(lambda x: max(x), "latitude")
    minl = city_table.aggregate(lambda x: min(x), "latitude")
    if choice == "min":
        print("Min latitude for the cities in every countries:")
        print(minl)
    elif choice == "max":
        print("Max latitude for the cities in every countries:")
        print(maxl)
    print()


# - print the average temperature for all the cities in Italy
testavg("Italy")
# - print the average temperature for all the cities in Sweden
testavg("Sweden")
# - print the min temperature for all the cities in Italy
test_minmax("Italy", 'min')
# - print the max temperature for all the cities in Sweden
test_minmax("Sweden", 'max')
# max_latitude
all_maxmin_latitude("max")
# min_latitude
all_maxmin_latitude("min")
