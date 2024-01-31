from get_data import *
from get_destinations import *
import pandas as pd
from datetime import datetime



##__________________________ Get the cities
df = pd.read_csv("Booking/Support/CodiPostal_Municipi_Comarca_MarcaTuristica.csv", delimiter = ";")

municipis = set(df["Nom municipi"].values)

cities = []
# iterate over different cities
# for ii in municipis:
#     response = get_dest(ii)
#     try: 
#         if response["region"] == "Catalonia":
#             #print("__", cities)
#             print(ii, "_", response["cityName"], "_", response["region"])
#             cities.append(response)
#         else: 
#             pass
#     except:
#         pass

# # Path to your JSON file
# file_path = 'Booking/Support/cities_ufi.json'

# with open(file_path, 'w') as file:
#     json.dump(cities, file, indent=4)


file_path = 'Booking/Support/cities_ufi.json'

# Reading the JSON data
with open(file_path, 'r') as file:
    ufis = json.load(file)

for ii in ufis: 
    print(ii["ufi"])


products = []
for ii in ufis: 
    print("____________", ii["cityName"], ii["ufi"])
    try: 
        for product in get_all_attractions(id=ii["ufi"], page = 1):
            if ii["ufi"] == product[0]["ufi"]:
                products.append(product)
            else: 
                break
    except:
        pass


# Save data to a JSON file
with open('Booking/Files/attractions_'+str(datetime.now().date())+'.json', 'w') as file:
    json.dump(products, file, indent=4)


