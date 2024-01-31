from getting_data import * 
from cleaning_data import * 

cards = []
pins  = []

# Get all the data
for product in get_all_attractions(cat_id, page = 0):
    cards.extend(product[0])
    pins.extend(product[1])

save_json(cards, "Cards_all")
save_json(pins, "Pins_all")

# Clean the data and save it in a CSV
cleaning_data()