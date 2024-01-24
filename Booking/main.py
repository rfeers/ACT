# iterate over different cities

# We define the id for our cities
cities = {
            "Barcelona": -372490,
            "Girona": -383956,
            "Tarragona": -403902, 
            "Lleida": 900039124
            #"Catalunya": 734
}

from getting_data import *

products = []
for id in cities.values(): 
    for product in get_all_attractions(id=id, page = 1):
        products.extend(product)


save_json(products, id=999)


