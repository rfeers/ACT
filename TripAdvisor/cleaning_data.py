from getting_data import *
from datetime import datetime
import json
import csv

def cleaning_data():
    # Replace 'your_file.json' with the path to your JSON file
    cards_file_path = "TripAdvisor/Files/Cards_all.json"
    pins_file_path = "TripAdvisor/Files/Pins_all.json"

    # Reading the JSON data into a Python dictionary
    with open(cards_file_path, 'r') as file:
        cards = json.load(file)

    with open(pins_file_path, 'r') as file:
        pins = json.load(file)

    date = datetime.now().date()

    # Generating a CSV file with all the info
    with open('TripAdvisor/Files/'+date+'_attractions.csv', 'w', encoding = 'utf-8-sig') as csvfile:
        fieldnames = [
            'Id',
            'Name', 
            'Rating', 
            'Reviews',
            'Tag',
            'merchandisingText', 
            'latitude',
            'longitude', 
            "Scraping_date"
        ]
        # Generate the writer object
        writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
        writer.writeheader()

        # Iterate over all products
        for ii in range(len(cards)):
            product = cards[ii]            
            #print(ii)
            pin = pins[ii]
            #print("product: ", product["saveId"]["id"], "pin: ", pin["saveId"]["id"])
            #print(product.get("merchandisingText",None))
            
            #print(product.get("bubbleRating", {} ))

            try:
                # Attempt to extract the rating
                rating = product["bubbleRating"]["rating"]
                reviews = product["bubbleRating"]["numberReviews"]["text"]
            except (KeyError, TypeError):
                # Set to None if the path does not exist or if an intermediate step is None
                rating = None
                reviews = None
    
            try:
                # Attempt to extract the rating
                tag = product["primaryInfo"]["text"]
                
            except (KeyError, TypeError):
                # Set to None if the path does not exist or if an intermediate step is None
                tag = None
    
            try:
                # Attempt to extract the rating
                merchandisingText = product["merchandisingText"]["text"]
                
            except (KeyError, TypeError):
                # Set to None if the path does not exist or if an intermediate step is None
                merchandisingText = None


            row = {
                    'Id':product["saveId"]["id"],
                    'Name':product["cardTitle"]["text"],
                    'Rating': rating,
                    'Reviews': reviews,
                    'Tag':  tag,
                    'latitude': pin["geoPoint"]["latitude"],
                    'longitude': pin["geoPoint"]["longitude"],
                    'merchandisingText': merchandisingText,
                    'Scraping_date': datetime.now().date()
                    
                }
            writer.writerow(row)
