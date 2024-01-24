from getting_data import *
import json
import csv

# Replace 'your_file.json' with the path to your JSON file
file_path = "Booking/Files/attractions_999.json"

# Reading the JSON data into a Python dictionary
with open(file_path, 'r') as file:
    data = json.load(file)


# Functions to get our data
#___________________________________________________________________________________________________________ EXTRACT ADDRESSES
def extract_details_from_address(address_data: dict, prefix:str = "") -> dict:
        """Extract specific fields from an address"""
        fields = ['address', 'city', 'latitude', 'longitude', 'country']
        if prefix: 
              prefix = prefix + '_'
        return {f'{prefix}{field}': address_data.get(field, '') for field in fields}

def extract_address(addresses:dict)-> dict:
    """Extract address details from a dictionary of adresses"""
    address_types = {
          'arrival': 'arrival',
          'departure':'departure',
          'attraction':'',
          'meeting':''
    }

    result = {}
    for address_type, prefix in address_types.items():
        if addresses.get(address_type):
            result.update(extract_details_from_address(addresses[address_type][0], prefix))

    # Ensure all keys are present in the result
    keys = [
        'arrival_address', 'arrival_city', 'arrival_latitude', 'arrival_longitude', 'arrival_country',
        'departure_address', 'departure_city', 'departure_latitude', 'departure_longitude', 'departure_country',
        'address', 'city', 'latitude', 'longitude', 'country'
    ]

    for key in keys: 
         result.setdefault(key, '')

    return result

#___________________________________________________________________________________________________________ EXTRACT TAXONOMY
def extract_taxonomy(taxonomy: dict) -> dict:
    """Extract category and tags from a taxonomy dictionary"""
    categories = taxonomy.get('categories') or []
    category = ' - '.join([cat['label'] for cat in categories if 'label' in cat])

    tags = taxonomy.get('tags') or []
    tag = ' '.join([tag_item['label'] for tag_item in tags if 'label' in tag_item])

    return {
        'category': category,
        'tags': tag
    }


#___________________________________________________________________________________________________________ EXTRACT REVIEWS
def extract_reviews(review_dict: dict) -> dict:    
    """Extract ratings and reviews counts from review dictionary"""
    if not review_dict or not isinstance(review_dict, dict):
         return {
              'rating': '', 
              'review_count':''
              }
    reviews = review_dict.get('combinedNumericStats') or {}

    rating = reviews.get('average', '')

    reviews_count = reviews.get('total', '')

    return {
         'rating': rating, 
         'review_count': reviews_count
    }


# Now 'data' is a Python dictionary containing the data from the JSON file
#save_json(data[0], id=000)

# We start persisting our data in CSV-format
with open('attractions.csv', 'w', encoding = 'utf-8-sig') as csvfile:
    fieldnames = [
        'id',
        'name', 
        'description', 
        'ufi', 
        #__________________________________ Geospatial
        #'price', 
        #'currency', 

        'rating', 
        'review_count',
        #'photos',

        #__________________________________ Taxonomy
        'category',
        'tags',

        #__________________________________ Geospatial
        'arrival_address',
        'arrival_city',
        'arrival_latitude', 
        'arrival_longitude',
        'arrival_country', 
        'departure_address',
        'departure_city',
        'departure_latitude', 
        'departure_longitude',
        'departure_country', 
        'address',
        'city', 
        'country',
        'latitude',
        'longitude'

    ]
    # Generate the writer object
    writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
    writer.writeheader()

    # Iterate over all products
    for product in data:
            address = extract_address(product['addresses'])
            taxonomy = extract_taxonomy(product['taxonomy'])
            reviews = extract_reviews(product.get('reviewsStats', {}))
            row = {
                'id':product['id'],
                'name':product['name'],
                'description':product['description'], 
                'ufi': product['ufi']
            }
            row.update(address)
            row.update(taxonomy)
            row.update(reviews)

            writer.writerow(row)