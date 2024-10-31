import csv, os


__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

# Let's write a function to do aggregation given an aggregation function and an aggregation key

# Let's write code to
# - print the average temperature for all the cities in Italy
# - print the average temperature for all the cities in Sweden
# - print the min temperature for all the cities in Italy
# - print the max temperature for all the cities in Sweden

class temp:
    def __init__(self, cities,countries):
        self.cities = cities
        self.countries = countries

    def all_cities(self):
        cities = []
        with open(os.path.join(__location__, 'Cities.csv')) as f:
            rows = csv.DictReader(f)
            for r in rows:
                cities.append(dict(r))
        return cities

    def all_countries(self):
        countries = []
        with open(os.path.join(__location__, 'Countries.csv')) as f:
            rows = csv.DictReader(f)
            for r in rows:
                countries.append(dict(r))
        return countries

    def avg_temp(self,cities,countries):
        temps = []
        for city in cities:
            temps.append(float(city['temperature']))
        print("The average temperature of all the cities:")
        print(sum(temps) / len(temps))
        print()

    def all_cities_by_country(self,cities,countries):
        cities_temp = []
        my_country = 'Italy'
        for city in cities:
            if city['country'] == my_country:
                cities_temp.append(city['city'])
        print("All the cities in", my_country, ":")
        print(cities_temp)
        print()

    def avg_temp_by_country(self,cities,countries):
        temps = []
        my_country = 'Italy'
        for city in cities:
            if city['country'] == my_country:
                temps.append(float(city['temperature']))
        print("The average temperature of all the cities in", my_country, ":")
        print(sum(temps) / len(temps))
        print()

    def max_temp_by_country(self,cities,countries):
        temps = []
        my_country = 'Italy'
        for city in cities:
            if city['country'] == my_country:
                temps.append(float(city['temperature']))
        print("The max temperature of all the cities in", my_country, ":")
        print(max(temps))
        print()

    def min_temp_by_country(self,cities,countries):
        temps = []
        my_country = 'Italy'
        for city in cities:
            if city['country'] == my_country:
                temps.append(float(city['temperature']))
        print("The min temperature of all the cities in", my_country, ":")
        print(min(temps))
        print()

    def filter(self,condition, dict_list):
        filtered_list = []
        for item in dict_list:
            if condition(item):
                filtered_list.append(item)
        return filtered_list



    def aggregate(self,aggregation_key, aggregation_function, dict_list):
        x = filter(lambda x: float(x['latitude']) >= 60.0, self.cities)
        for item in x:
            print(item)
        pass

