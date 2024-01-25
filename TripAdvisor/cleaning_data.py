from getting_data import *
import json
import csv

# Replace 'your_file.json' with the path to your JSON file
file_path = "TripAdvisor/Files/attractions.json"

# Reading the JSON data into a Python dictionary
with open(file_path, 'r') as file:
    data = json.load(file)

#print(data[0].keys())

#print("Id: ", data[0]["saveId"])
#print("Name: ", data[0]["cardTitle"]["text"])
#print("Tag: ", data[0]["primaryInfo"]["text"])
#print("merchandisingText: ", data[0]["merchandisingText"]["text"])
#print("Rating: ", data[0]["bubbleRating"]["rating"])
#print("Reviews: ", data[0]["bubbleRating"]["numberReviews"]["text"])

#print(data[0]["labels"])


# We start persisting our data in CSV-format
with open('attractions.csv', 'w', encoding = 'utf-8-sig') as csvfile:
    fieldnames = [
        'Id',
        'Name', 
        'Rating', 
        'Reviews',
        'Tag',
        'merchandisingText'
    ]
    # Generate the writer object
    writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
    writer.writeheader()

    # Iterate over all products
    for product in data:
        print(type(product))
        row = {
                'Id':product["saveId"],
                'Name':product["cardTitle"]["text"],
                'Rating':product["bubbleRating"]["rating"], 
                #'Reviews': product.get("numberReviews", None)["text"],
                'Tag':  product["primaryInfo"]["text"],
                #'merchandisingText': product["merchandisingText"]["text"]
            }
        writer.writerow(row)
