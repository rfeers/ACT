import requests
import json
import argparse # Library to set input variables

#id BCN = -372490

url = "https://www.booking.com/dml/graphql?label=gen173nr-1BCAEoggI46AdIM1gEaEaIAQGYAQm4AQfIAQzYAQHoAQGIAgGoAgO4ApHzt6oGwAIB0gIkN2NhMTUxNWYtYjQyOS00MzIwLTg0Y2QtMDM4ZTQ0NzUxNTZi2AIF4AIB&sid=e7ed4fcba519268f643bca46c1504408&aid=304142&lang=en-gb"

# Setting our API call
query = """query SearchProducts($input: AttractionsProductSearchInput!, $contextParams: AttractionsContextParamsInput) {\n  attractionsProduct {\n    searchProducts(input: $input, contextParams: $contextParams) {\n      ... on AttractionsProductSearchResponse {\n        filterOptions {\n          destinationFilters {\n            ...FilterOptionFragment\n            __typename\n          }\n          labelFilters {\n            ...FilterOptionFragment\n            __typename\n          }\n          priceFilters {\n            ...FilterOptionFragment\n            __typename\n          }\n          typeFilters {\n            ...FilterOptionFragment\n            __typename\n          }\n          ufiFilters {\n            ...FilterOptionFragment\n            __typename\n          }\n          supportedLanguageFilters {\n            ...FilterOptionFragment\n            __typename\n          }\n          __typename\n        }\n        filterStats {\n          filteredProductCount\n          unfilteredProductCount\n          __typename\n        }\n        unavailableProducts\n        products {\n          ...AttractionsProductFragment\n          __typename\n        }\n        sections {\n          attr_book_score {\n            ...AttractionsProductFragment\n            __typename\n          }\n          distance_to_hotel {\n            ...AttractionsProductFragment\n            __typename\n          }\n          trending {\n            ...AttractionsProductFragment\n            __typename\n          }\n          __typename\n        }\n        autoExtendBanner {\n          hasNearbyProducts\n          hasOwnProducts\n          nearbyProductFirstIndex\n          __typename\n        }\n        sorters {\n          name\n          value\n          __typename\n        }\n        defaultSorter {\n          name\n          value\n          __typename\n        }\n        noResultsForQuery\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment FilterOptionFragment on FilterOption {\n  image {\n    url\n    __typename\n  }\n  name\n  productCount\n  tagname\n  childFilterOptions {\n    name\n    tagname\n    productCount\n    __typename\n  }\n  __typename\n}\n\nfragment AttractionsProductFragment on AttractionsProduct {\n  accessibility\n  additionalInfo\n  additionalBookingInfo {\n    childRatesApplicability {\n      label\n      __typename\n    }\n    freeForChildren {\n      age {\n        label\n        __typename\n      }\n      __typename\n    }\n    onlyRegularTickets {\n      label\n      __typename\n    }\n    participantsPerBooking {\n      label\n      __typename\n    }\n    __typename\n  }\n  addresses {\n    arrival {\n      ...AttractionsAddressFragment\n      __typename\n    }\n    attraction {\n      ...AttractionsAddressFragment\n      __typename\n    }\n    departure {\n      ...AttractionsAddressFragment\n      __typename\n    }\n    entrance {\n      ...AttractionsAddressFragment\n      __typename\n    }\n    guestPickup {\n      ...AttractionsAddressFragment\n      __typename\n    }\n    meeting {\n      ...AttractionsAddressFragment\n      __typename\n    }\n    pickup {\n      ...AttractionsAddressFragment\n      __typename\n    }\n    __typename\n  }\n  applicableTerms {\n    policyProvider\n    __typename\n  }\n  audioSupportedLanguagesLabels {\n    code\n    label\n    __typename\n  }\n  cancellationPolicy {\n    comparedTo\n    hasFreeCancellation\n    isStillRefundable\n    percentage\n    period\n    until\n    __typename\n  }\n  covid\n  dietOptions\n  description\n  guideSupportedLanguagesLabels {\n    code\n    label\n    __typename\n  }\n  healthSafety\n  id\n  isBookable\n  labels {\n    text\n    type\n    __typename\n  }\n  name\n  notIncluded\n  offers {\n    additionalInfo\n    availabilityType\n    benefits {\n      freeAudioGuide {\n        label\n        value\n        __typename\n      }\n      freeDrink {\n        label\n        value\n        __typename\n      }\n      freeTransportation {\n        label\n        value\n        __typename\n      }\n      inStoreDiscount {\n        label\n        value\n        __typename\n      }\n      priorityLane {\n        label\n        value\n        __typename\n      }\n      skipTheLine {\n        label\n        value\n        __typename\n      }\n      __typename\n    }\n    description\n    id\n    items {\n      constraint {\n        label\n        maxAge\n        maxGroupSize\n        minAge\n        minGroupSize\n        numAdults\n        numChildren\n        numPeople\n        type\n        __typename\n      }\n      duration {\n        label\n        value\n        __typename\n      }\n      id\n      label\n      maxPerReservation\n      minPerReservation\n      tieredPricing\n      travelerCountRequired\n      type\n      __typename\n    }\n    label\n    languageOptions {\n      label\n      language\n      type\n      __typename\n    }\n    locationInstructions\n    notIncluded\n    reservationRestrictions {\n      adultRequiredForReservation\n      maxOfferItemsPerReservation\n      minOfferItemsPerReservation\n      __typename\n    }\n    typicalDuration {\n      label\n      value\n      __typename\n    }\n    typicalFrequency {\n      label\n      value\n      __typename\n    }\n    whatsIncluded\n    __typename\n  }\n  onSiteRequirements {\n    adultSupervisionRequired {\n      label\n      maxAge\n      __typename\n    }\n    age {\n      label\n      min\n      max\n      __typename\n    }\n    clothingCoveringShouldersKneesRequired {\n      label\n      __typename\n    }\n    comfortableFootwearRecommended {\n      label\n      __typename\n    }\n    drivingLicenseRequired {\n      label\n      __typename\n    }\n    earlyArrival {\n      label\n      minutes\n      __typename\n    }\n    height {\n      label\n      min\n      max\n      __typename\n    }\n    noAlcoholDuringDryDays {\n      label\n      __typename\n    }\n    noAlcoholDuringRamadan {\n      label\n      __typename\n    }\n    onlyOperatesInGoodWeather {\n      label\n      __typename\n    }\n    proofOfIdentityRequired {\n      label\n      __typename\n    }\n    ticketCollection {\n      label\n      __typename\n    }\n    unsuitable {\n      label\n      pregnant\n      reducedMobility\n      __typename\n    }\n    voucherPrintingRequired {\n      label\n      value\n      __typename\n    }\n    weight {\n      label\n      min\n      max\n      __typename\n    }\n    writtenConsentForChildren {\n      label\n      maxAge\n      __typename\n    }\n    __typename\n  }\n  operatedBy\n  photos {\n    ...PhotoTypesFragment\n    __typename\n  }\n  pickupTypes {\n    type\n    __typename\n  }\n  postBookingInfo\n  poweredBy\n  primaryLabel {\n    text\n    type\n    __typename\n  }\n  primaryPhoto {\n    ...PhotoTypesFragment\n    __typename\n  }\n  representativePrice {\n    chargeAmount\n    currency\n    publicAmount\n    __typename\n  }\n  restrictions\n  reviewsStats {\n    allReviewsCount\n    isGoodScore\n    percentage\n    combinedNumericStats {\n      average\n      total\n      __typename\n    }\n    categoryRatingStats {\n      categoryName\n      total\n      average\n      __typename\n    }\n    __typename\n  }\n  shortDescription\n  supplierInfo {\n    isIndividual\n    details {\n      address\n      name\n      __typename\n    }\n    __typename\n  }\n  supportedFeatures {\n    alternativeTimeSlotsPartiallySupported\n    alternativeTimeSlotsSupported\n    indexable\n    isAutomated\n    hasFallbackLocale\n    liveAvailabilityCheckPartiallySupported\n    liveAvailabilityCheckSupported\n    rawContentWebviewTrackingSupported\n    selfFundedDiscountTrackingSupported\n    __typename\n  }\n  slug\n  taxonomy {\n    categories {\n      label\n      slug\n      __typename\n    }\n    tags {\n      label\n      slug\n      __typename\n    }\n    type {\n      label\n      slug\n      __typename\n    }\n    __typename\n  }\n  timeZone\n  typicalDuration {\n    label\n    value\n    __typename\n  }\n  typicalFrequency {\n    label\n    value\n    __typename\n  }\n  ufi\n  ufiDetails {\n    ...UfiDetailsFragment\n    __typename\n  }\n  contextUfiDetails {\n    ...UfiDetailsFragment\n    __typename\n  }\n  uniqueSellingPoints\n  whatsIncluded\n  flags {\n    flag\n    value\n    rank\n    __typename\n  }\n  itinerary {\n    type\n    __typename\n  }\n  productDistances {\n    distanceToCityCenter {\n      distanceDescription\n      distanceKm\n      __typename\n    }\n    distanceToAccommodation {\n      distanceDescription\n      distanceKm\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment AttractionsAddressFragment on AttractionsAddress {\n  address\n  city\n  country\n  googlePlaceId\n  id\n  instructions\n  latitude\n  locationType\n  longitude\n  publicTransport\n  zip\n  __typename\n}\n\nfragment PhotoTypesFragment on AttractionsPhoto {\n  hereProductPageDesktop\n  hereProductPageMobile\n  gallery\n  small\n  __typename\n}\n\nfragment UfiDetailsFragment on AttractionLocationResponse {\n  attractionsCount\n  bCityName\n  bInCityName\n  banners {\n    content\n    title\n    type\n    __typename\n  }\n  image\n  latitude\n  longitude\n  ufi\n  url {\n    city\n    country\n    prefix\n    __typename\n  }\n  countryName\n  __typename\n}\n"""
headers = {
    'authority': 'www.booking.com',
    'accept': '*/*',
    'accept-language': 'en',
    'content-type': 'application/json',
    'cookie': 'px_init=0; cors_js=1; BJS=-; bkng_sso_session=e30; pxcts=9a9ab982-7fac-11ee-b27c-55309a9f3fd4; _pxvid=9a9a9c9a-7fac-11ee-b27c-e94c12d71a44; _pxhd=toN4w1f49X6BXb7h1VUUaX7wnUuPw-vJxG46vHUk1coVsCsQurigejDxPpVZBpiWcoTRYMI1KOA0Uqaxy539TQ%3D%3D%3A3Nz2-cTWr3ebCBlut0UkgK6l3jrPGZa5HkccNyCVF2HRGSUoigUL9ZzdTzxXF9mEb%2FfurYn3n0REF3N8D9j9loyAm8chybg0nabYyeAaG0Y%3D; OptanonAlertBoxClosed=2023-11-10T09:36:21.149Z; bkng_sso_ses=eyJib29raW5nX2dsb2JhbCI6W3siYSI6MSwiaCI6Ikh3R2VLNVR2U0JzdFdUUVZ6ckRDNVdhdFg5OXB2QU5FRTdhakk1Rnd0Ym8ifV19; pcm_consent=consentedAt%3D2023-11-10T09%3A36%3A21.510Z%26countryCode%3DES%26expiresAt%3D2024-05-08T09%3A36%3A21.510Z%26implicit%3Dfalse%26regionCode%3DCT%26regulation%3Dgdpr%26legacyRegulation%3Dgdpr%26consentId%3D123df132-4633-400a-b0d8-b0ab8c518f07%26analytical%3Dfalse%26marketing%3Dfalse; bkng_sso_auth=CAIQsOnuTRqEAYV9lzi4K2o9b5UQkQrLWyIB0gfqvV7jszp0ccxvz3CDm6DCr/7AkVM2EwCOfyyWjEyrxsX5Kol5W1ftU19wee6UET17NDh2dnCTP6sBMuDZqWq4qkbsK5x/PWNosNHcu25XegGEjwAP8PsXFGyxsgdSHYKlZU6XpVZ/Gihxa/gPPLYHEA==; _px3=633289c3a3fa139022c7688d0f94afcb9d79bf2df9ec41e87d75f089fc5b956f:EkL+pMhNonTcPMMgQEv46OyUeKpc+AVN9LxFTCl/Z865KWcWPGGb4gxUikgjeN8pDoTa8dvLKy6CYOwzvT4M7A==:1000:dJRHtXVGz2tgK/I7HQ5drIvROd2xNxJEnoQiPiDjGJq4r/JFwBh87QjRh0KPxKyfqT6qXNkArFy/6Qh1Rlnb6L/tIKtvosJvgg6I+s/+4Vu+IiU3rrOkGxm455V1SAFBfZZCYqXS31+sa2IRKDjvl5Nd6yVWv/8Qi8gd+7rHyWy8tKkhNta6seIeuvyP665U/Km8YPIYBNX0v9EUbc/EnOM4hRTJ0mpdcQyGtFTSQW0=; _pxde=e23dd6d7f89c80ea122f04a78799dd8a5553c32d03e34368365adfab8d22633b:eyJ0aW1lc3RhbXAiOjE2OTk2MDkwMDUyOTAsImZfa2IiOjAsImlwY19pZCI6W119; lastSeen=1699609018191; OptanonConsent=isGpcEnabled=0&datestamp=Fri+Nov+10+2023+10%3A37%3A24+GMT%2B0100+(Central+European+Standard+Time)&version=202308.2.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=292b890a-9414-4247-929d-22844d6842cb&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A0%2CC0004%3A0&implicitConsentCountry=GDPR&implicitConsentDate=1699608979742&backfilled_at=1699608981528&backfilled_seed=1&geolocation=ES%3BCT&AwaitingReconsent=false; bkng=11UmFuZG9tSVYkc2RlIyh9Yaa29%2F3xUOLbXpFeYC4TUhBKk4KVQwNa2M%2FW9OdLxEEitKT1hZvppYPBNxNri0BjM1ehwlZnQy57mM6vfmv2f2EuM8ywTeiAaJst0gEe7jrgjg66suY0oqqD9BwnV0rR883oviQVle%2BhICIfoWzPxcaKlc7ySv%2BrD9d0LOwp3zdfm6wANHHRmJA%3D; bkng=11UmFuZG9tSVYkc2RlIyh9YXSgTtYpR%2F1WOjMvuuinviEpNP0NZab2WEnv%2Fi9d2PaPiCjSqrKSJO%2Bs%2BISzxa6hU2Uh25RFTMuOKt1d1yXHFH5MkrhzSq%2Fxa6ZNCIGW%2BfVi0HIoLAQaNTDyXpDLbNY8r0hOuU2N1f9Eqt16Ip326bLX2U1i3HmoCSnVB9gnDvNCupI1CDBhTaqYOxdow4dAWQ%3D%3D; bkng_sso_auth=CAIQsOnuTRpmUMXyjOYKdtvcBeH900ooKUwobZWnrcN60N/Xw4pa/KfFrC3bgum/zkIqC6D1OPk64yWcls5S3Q2nHvX61Pb1biidc9lh4mbyQ2Nqyyc2mMsUCpxY5FGbxzDNYVPgAvUTXXY6L0gd; pcm_consent=analytical%3Dtrue%26countryCode%3DUS%26consentId%3D406790e3-dbd1-49f4-a4ca-e17347334c00%26consentedAt%3D2023-12-19T12%3A45%3A08.137Z%26expiresAt%3D2024-06-16T12%3A45%3A08.137Z%26implicit%3Dtrue%26marketing%3Dtrue%26regulation%3Dnone%26legacyRegulation%3Dnone',
    'origin': 'https://www.booking.com',
    'referer': 'https://www.booking.com/attractions/searchresults/es/barcelona.html?label=gen173nr-1BCAEoggI46AdIM1gEaEaIAQGYAQm4AQfIAQzYAQHoAQGIAgGoAgO4ApHzt6oGwAIB0gIkN2NhMTUxNWYtYjQyOS00MzIwLTg0Y2QtMDM4ZTQ0NzUxNTZi2AIF4AIB&aid=304142&source=attractions_index_open_shop',
    'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    'x-booking-context-action-name': 'attractions_index',
    'x-booking-context-aid': '304142',
    'x-booking-csrf-token': 'eyJhbGciOiJIUzUxMiJ9.eyJpc3MiOiJjb250ZXh0LWVucmljaG1lbnQtYXBpIiwic3ViIjoiY3NyZi10b2tlbiIsImlhdCI6MTY5OTYwOTA0MywiZXhwIjoxNjk5Njk1NDQzfQ.2gon1hSFgKh4f2mk-EBsnPp__H_peEPRyb5vaLwDok6tDJKgnSw1zCH7xfR_OL2Oy9Ci1D0sdBhTSf1KOeww3Q',
    'x-booking-et-serialized-state': 'EwKq2ZfRCY1ptyS2MqTH5Ibphp3gijQVhJSpSSa5DWha6loZwNRaDR0plHY-8Ty1s',
    'x-booking-pageview-id': '446d43a9eedf0087',
    'x-booking-site-type-id': '1',
    'x-booking-topic': 'capla_browser_b-attractions-product-frontend-capla'
  }

# Function to call Booking API -> We get a list of attractions in the destination we set.
def get_data(destionation_id, limit=40, page=1):
    payload = json.dumps({
    "operationName": "SearchProducts",
    "variables": {
      "input": {
        "ufi": int(destionation_id),
        "extractFilterStats": True,
        "extractFilterOptions": True,
        "extractSorters": True,
        "extractSections": False,
        "limit": limit,
        "source": "attractions_index_open_shop",
        "page": page,
        "filterBySupportedLanguage": []
      },
      "contextParams": {
        "urlCode": "",
        "test": False,
        "showInactive": False,
        "source": "attractions_index_open_shop",
        "adPlat": "",
        "label": "gen173nr-1BCAEoggI46AdIM1gEaEaIAQGYAQm4AQfIAQzYAQHoAQGIAgGoAgO4ApHzt6oGwAIB0gIkN2NhMTUxNWYtYjQyOS00MzIwLTg0Y2QtMDM4ZTQ0NzUxNTZi2AIF4AIB"
      }
    },
    "extensions": {},
    "query": query
  })

    response = requests.request("POST", url, headers=headers, data=payload)

    return response.json()

# Save all obtained data into a JSON
def save_json(results, destination_id):
    with open(f'Booking/Files/attractions_{destination_id}.json','w') as jsonfile:
        json.dump(results, jsonfile, indent=4)

# Function to generate a loop and concat all the available data
def get_attractions( destination_id:int, page:int, limit:int = 40) -> list:
    # get all the products iterating over the pages
    while True:
        data = get_data(destination_id,page) #We get the data for each iteration
        # print number of products
        print(data['data']['attractionsProduct']['searchProducts']['filterStats']['filteredProductCount'], page)
        print(data['data']['attractionsProduct']['searchProducts']['products'])
        
        yield data['data']['attractionsProduct']['searchProducts']['products']

        if page*limit >= data['data']['attractionsProduct']['searchProducts']['filterStats']['filteredProductCount']:
            break
        page += 1


if __name__ == "__main__":
    parser = argparse.ArgumentParser() 
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--destination_id', type=str, help='destination id')
    group.add_argument('--destination_name', type=str, help='destination name')
    args = parser.parse_args()

    #products = []

    for products in get_attractions(destination_id=args.destination_id,page = 1,limit = 40):
        print(products)
        products.extend(products)

    save_json(products, destination_id=args.destination_id)
    
    #results = get_data(destionation_id=args.destination_id)
    #list_temp = [results]
    #save_json(list_temp, destination_id=args.destination_id)
    #print(get_data(destionation_id=args.destination_id))
    #print(get_atractions(destionation_id=args.destination_id))

