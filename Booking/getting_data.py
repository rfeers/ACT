import requests
import json
import argparse # Library to set input variables


# Initial Variables
headers = {
  'authority': 'www.booking.com',
  'accept': '*/*',
  'accept-language': 'en,ko;q=0.9',
  'content-type': 'application/json',
  'cookie': 'cors_js=1; _pxvid=5fc7c755-232d-11ee-95f0-221885d8371e; OptanonAlertBoxClosed=2023-07-15T16:35:00.718Z; FPID=FPID2.2.%2BDJsHTamLQ0fg4n1pcBuRxa2aJTcHU5m1zigE8mNWGU%3D.1691701378; rskxRunCookie=0; rCookie=9vuyq6v5tljp18n73lj3ll5nfeuh; _ga_FPD6YLJCJ7=GS1.1.1691951988.2.0.1691951988.0.0.0; lastRskxRun=1692037142015; _uetvid=fd6d56c03a0911eeafd539d5305baa2f; _ga=GA1.1.1376287762.1691701378; _ga_A12345=GS1.1.1694252366.4.0.1694252366.0.0.0; _pxhd=-pXnYSyZVenq9jJd86woFCCc%2FnVHiVublEJtcEz33FBi-uOxbIv3gFUfNE3H9W%2FKKIIpOVdfwBYaUizvER17DA%3D%3D%3AChpkpB1-RM2MAY50EqcVlJYXfY3O8g5tUFq3sbGmpQLl%2Fakl0FeCff%2FTMlJKf1wUGEuEMhUaFms%2FTN8EKSRo5yH0vKGnsoBU8sOSTGGpDGQ%3D; bkng_sso_ses=eyJib29raW5nX2dsb2JhbCI6W3siaCI6IkRTdnRxWWlaUldRM3doNjFNVDc4WFdmcm0wY2tDcEFPWldDNCs1TjBhY2sifV19; pcm_consent=consentedAt%3D2023-12-19T12%3A13%3A50.266Z%26countryCode%3DES%26expiresAt%3D2024-06-16T12%3A13%3A50.266Z%26implicit%3Dfalse%26regionCode%3DCT%26regulation%3Dgdpr%26legacyRegulation%3Dgdpr%26consentId%3Dfe67fc9b-0f5c-4754-a5c5-a0ff948cecfe%26analytical%3Dtrue%26marketing%3Dtrue; bkng_sso_session=e30; bkng_expired_hint=eyJib29raW5nX2dsb2JhbCI6W3sibG9naW5faGludCI6MjE5NTAwNjUzNH1dfQ; bkng_sso_auth=CAIQsOnuTRqIASNV09FDZbePSgtM1d5Cg+PT4lWIG41VPAq/oIw1NnMeVA/H3bqwle69kcUsz/7xUujdtxVdaIjuZxztrsf8iADSrbTEHWluseFBls5ruuCGcW1dmmh6OW32PEOicoIvEJtMMhxuWhLlBayvrd8KJEeSX2YCnqzv5iMHHlUHU5670Mo+N+cOEE8=; pxcts=530ff5af-baa0-11ee-97d9-f6a0e4e11c25; _px3=09b2fb1182f8f1dae0069b2dec3361aeaacf51624f8bbb9e4b54c9054e924d68:EFc0k92X5BaR7sdSNHanMVNoI4N4vpADWoY9U6HW3RHcFkXwK5d/Hpy8akalQbk3l3vnyUv55BAKtzKI8uYqxA==:1000:bUbMPhnGosjxJNeaTBae3pCTmuDrSgETj5eZz8Gku9tNUmUaeEn7uQrJ75wxT8r3iaF5bxggp920e9RmBrcrc/37RfCsWQEAns2XhIS/imL6wI1d1/fxAPrLemAPgtdrjMM3YJLTsjccItj9dzzncTIpEZraTVl6vDYryEqMRS9P4gjQ6F+R1dxeT6qP5ThoW7QGag//qbuul/H3hqoEBwMFxPQPxAzgLiXAhR96EHE=; _pxde=045b45794ac66b2209ec4c01311e1ed7f09d7475b3be2360158d09fa007f1b89:eyJ0aW1lc3RhbXAiOjE3MDYwOTA4MjYyNjcsImZfa2IiOjAsImlwY19pZCI6W119; px_init=0; BJS=-; aws-waf-token=74098cfc-be07-4c4b-b6a9-a3a7c5d81bfc:HQoAoh5GEeMkAAAA:SQH+MLOHgDM/mlx2dVSUocfbpXrgISFZsay6/g4GA7/U4BFO/UoEASXAetiEFB1uRr26GGJAdMtm2CgqFCcYJ2yY9elJ/8NInaxW4mdaSPdo5vwKFehtJ5hF6PvK/92NfCmhBG+QjWV/RqdywUPF+Ot8hNUzWZGnUui2m6BLz5W4U/j8UqFqpPt1XB9SwGfca4ipI2hYP8aV/xsl68dDUA==; lastSeen=1706090842269; OptanonConsent=isGpcEnabled=0&datestamp=Wed+Jan+24+2024+11%3A07%3A22+GMT%2B0100+(Central+European+Standard+Time)&version=202310.2.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=d2dfd35a-50fa-4bc5-938d-1699f9630541&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A0%2CC0004%3A0&implicitConsentCountry=GDPR&implicitConsentDate=1706090839311&AwaitingReconsent=false&backfilled_at=1689438901145&backfilled_seed=1&geolocation=ES%3BCT; _gcl_au=1.1.548283850.1706090843; bkng=11UmFuZG9tSVYkc2RlIyh9Yaa29%2F3xUOLb9qg0InA%2FFDfGSMw1xE6iu2wyENaK2g0r7N1vKrP9u7ich7R%2Bnrp2MDf1Q90xK%2FiQIlVzrEvQ9PtvB3B%2FjCF5asTfTuOhlqtJZnQB%2F0QNXkYNXRE6gHRPGHrK%2BsLAAmiEkTaGJQGXiWKn6dqRUkgpy457VEXL8XkwJc907lO4d7wcNDt9%2BC%2BwJbgVVGGGO1AHZ86yiR0pj1t6REjI1hg64LetW1zBi%2Fja; _pxhd=3HNhYf%2FIEmuoek0KR1xQpQkrnh7FeR2blH0GBAxKmgS5bT1wf8Lc256hVC3s4AtJGcovVhihms2rhuG5iyd9yA%3D%3D%3AMPCeM-s0c5Et7XlJHt1QloJJ7gWv4tLPHepcIQSGu8QDFDEeC1q96CLKILA79krdVIaRGeKC-zMOH1FxKb5uyt6FrVenr9-eHvGmydM7hv8%3D; bkng=11UmFuZG9tSVYkc2RlIyh9YXSgTtYpR%2F1WOjMvuuinviEpNP0NZab2WEnv%2Fi9d2PaPiCjSqrKSJO%2Bs%2BISzxa6hU%2B3z2%2Bl5l3pQm0upBL9x0qryWhGEakYHEmhUnhY12jFvbtwYv07g5Xn4I8eeJcJ0g8pawT7H7Kec7x5h0uvV14eHB7bvGlhMD7jFsNQPG9PiuwUY41K%2F3q04a%2FDt3L1psA%3D%3D; bkng_sso_auth=CAIQsOnuTRpmGXR2MT3xohNbnT2lM7uSE8rBRKQgS9yg29cAIK1VtKA9sKWAoL89FsvihUESVJVQUb5sNCU7xYEtWCBItF5shnayqpQdDd0sZEWAJjt+AA5G5FJLzfExIqcVxViLybSLGwR/IpNU; pcm_consent=analytical%3Dfalse%26countryCode%3DES%26consentId%3D41d5534f-dd6b-4b19-b11f-e7185cd9d214%26consentedAt%3D2023-12-20T07%3A43%3A44.257Z%26expiresAt%3D2024-06-17T07%3A43%3A44.257Z%26implicit%3Dtrue%26marketing%3Dfalse%26regionCode%3DCT%26regulation%3Dgdpr%26legacyRegulation%3Dgdpr; bkng_sso_auth=CAIQsOnuTRpmeYH2v2VPApLrpeqxbKaOXIK8xqXbieo5Yccrn+KIusS55Z4djOfMsRflL4jxTcqeyU5Q/N05LFCBDa8FbbzRUrKku7n8MBCjKPmGMHU1/odohsOL/7hDQNCNe+OYCrCA0SIaWhWz; pcm_consent=analytical%3Dfalse%26countryCode%3DES%26consentId%3D88a981bf-3048-4428-936e-c8cc2dfa033c%26consentedAt%3D2023-12-20T08%3A03%3A48.131Z%26expiresAt%3D2024-06-17T08%3A03%3A48.131Z%26implicit%3Dtrue%26marketing%3Dfalse%26regionCode%3DCT%26regulation%3Dgdpr%26legacyRegulation%3Dgdpr',
  'origin': 'https://www.booking.com',
  'referer': 'https://www.booking.com/attractions/searchresults/es/barcelona.html?aid=397594&label=gog235jc-1DCAEoggI46AdIM1gDaEaIAQGYATG4AQfIAQzYAQPoAQH4AQKIAgGoAgO4AtTCw60GwAIB0gIkYTUyZTAwN2ItM2JhYy00MDhjLTllOWUtNmJmYjc1MjNjMDdh2AIE4AIB&source=search_box',
  'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"macOS"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
  'x-booking-context-action-name': 'attractions_index',
  'x-booking-context-aid': '397594',
  'x-booking-csrf-token': 'eyJhbGciOiJIUzUxMiJ9.eyJpc3MiOiJjb250ZXh0LWVucmljaG1lbnQtYXBpIiwic3ViIjoiY3NyZi10b2tlbiIsImlhdCI6MTcwNjA5MDg0MSwiZXhwIjoxNzA2MTc3MjQxfQ.dvdPmpgM3Kq4_PtJ3WciMZgOEGKl6DZFDKUGZvIS3153jEMjEyIqV5bNQVBEIo_pMBwU7OfCBGvjwfeCW2mNrg',
  'x-booking-et-serialized-state': 'EIvctzZG1RzzuCsjK4c7Thkb3WaCMgsORG1QMXP2UuEHN0OkKWyBq368nfGMasyytUMvMy6F40QvHOMNDilS8SQ',
  'x-booking-pageview-id': 'f05a472c91c10054',
  'x-booking-site-type-id': '1',
  'x-booking-topic': 'capla_browser_b-attractions-product-frontend-capla'
}

query = "query SearchProducts($input: AttractionsProductSearchInput!, $contextParams: AttractionsContextParamsInput) {\n  attractionsProduct {\n    searchProducts(input: $input, contextParams: $contextParams) {\n      ... on AttractionsProductSearchResponse {\n        filterOptions {\n          destinationFilters {\n            ...FilterOptionFragment\n            __typename\n          }\n          labelFilters {\n            ...FilterOptionFragment\n            __typename\n          }\n          priceFilters {\n            ...FilterOptionFragment\n            __typename\n          }\n          typeFilters {\n            ...FilterOptionFragment\n            __typename\n          }\n          ufiFilters {\n            ...FilterOptionFragment\n            __typename\n          }\n          supportedLanguageFilters {\n            ...FilterOptionFragment\n            __typename\n          }\n          minRatingFilter {\n            ...FilterOptionFragment\n            __typename\n          }\n          timeOfDayFilters {\n            ...FilterOptionFragment\n            __typename\n          }\n          __typename\n        }\n        filterStats {\n          filteredProductCount\n          unfilteredProductCount\n          __typename\n        }\n        unavailableProducts\n        products {\n          ...AttractionsProductFragment\n          __typename\n        }\n        sections {\n          attr_book_score {\n            ...AttractionsProductFragment\n            __typename\n          }\n          distance_to_hotel {\n            ...AttractionsProductFragment\n            __typename\n          }\n          trending {\n            ...AttractionsProductFragment\n            __typename\n          }\n          __typename\n        }\n        sorters {\n          name\n          value\n          __typename\n        }\n        defaultSorter {\n          name\n          value\n          __typename\n        }\n        noResultsForQuery\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment FilterOptionFragment on FilterOption {\n  image {\n    url\n    __typename\n  }\n  name\n  productCount\n  tagname\n  childFilterOptions {\n    name\n    tagname\n    productCount\n    __typename\n  }\n  __typename\n}\n\nfragment AttractionsProductFragment on AttractionsProduct {\n  accessibility\n  additionalInfo\n  additionalBookingInfo {\n    childRatesApplicability {\n      label\n      __typename\n    }\n    freeForChildren {\n      age {\n        label\n        __typename\n      }\n      __typename\n    }\n    onlyRegularTickets {\n      label\n      __typename\n    }\n    participantsPerBooking {\n      label\n      __typename\n    }\n    __typename\n  }\n  addresses {\n    arrival {\n      ...AttractionsAddressFragment\n      __typename\n    }\n    attraction {\n      ...AttractionsAddressFragment\n      __typename\n    }\n    departure {\n      ...AttractionsAddressFragment\n      __typename\n    }\n    entrance {\n      ...AttractionsAddressFragment\n      __typename\n    }\n    guestPickup {\n      ...AttractionsAddressFragment\n      __typename\n    }\n    meeting {\n      ...AttractionsAddressFragment\n      __typename\n    }\n    pickup {\n      ...AttractionsAddressFragment\n      __typename\n    }\n    __typename\n  }\n  applicableTerms {\n    policyProvider\n    __typename\n  }\n  audioSupportedLanguagesLabels {\n    code\n    label\n    __typename\n  }\n  cancellationPolicy {\n    comparedTo\n    hasFreeCancellation\n    isStillRefundable\n    percentage\n    period\n    until\n    __typename\n  }\n  covid\n  dietOptions\n  description\n  guideSupportedLanguagesLabels {\n    code\n    label\n    __typename\n  }\n  healthSafety\n  id\n  isBookable\n  labels {\n    text\n    type\n    __typename\n  }\n  name\n  notIncluded\n  offers {\n    additionalInfo\n    availabilityType\n    description\n    id\n    items {\n      constraint {\n        label\n        maxAge\n        maxGroupSize\n        minAge\n        minGroupSize\n        numAdults\n        numChildren\n        numPeople\n        type\n        __typename\n      }\n      duration {\n        label\n        value\n        __typename\n      }\n      id\n      label\n      maxPerReservation\n      minPerReservation\n      tieredPricing\n      travelerCountRequired\n      type\n      __typename\n    }\n    label\n    languageOptions {\n      label\n      language\n      type\n      __typename\n    }\n    locationInstructions\n    notIncluded\n    reservationRestrictions {\n      adultRequiredForReservation\n      maxOfferItemsPerReservation\n      minOfferItemsPerReservation\n      __typename\n    }\n    typicalDuration {\n      label\n      value\n      __typename\n    }\n    whatsIncluded\n    __typename\n  }\n  onSiteRequirements {\n    adultSupervisionRequired {\n      label\n      maxAge\n      __typename\n    }\n    age {\n      label\n      min\n      max\n      __typename\n    }\n    clothingCoveringShouldersKneesRequired {\n      label\n      __typename\n    }\n    comfortableFootwearRecommended {\n      label\n      __typename\n    }\n    drivingLicenseRequired {\n      label\n      __typename\n    }\n    earlyArrival {\n      label\n      minutes\n      __typename\n    }\n    height {\n      label\n      min\n      max\n      __typename\n    }\n    noAlcoholDuringDryDays {\n      label\n      __typename\n    }\n    noAlcoholDuringRamadan {\n      label\n      __typename\n    }\n    onlyOperatesInGoodWeather {\n      label\n      __typename\n    }\n    proofOfIdentityRequired {\n      label\n      __typename\n    }\n    ticketCollection {\n      label\n      __typename\n    }\n    unsuitable {\n      label\n      pregnant\n      reducedMobility\n      __typename\n    }\n    voucherPrintingRequired {\n      label\n      value\n      __typename\n    }\n    weight {\n      label\n      min\n      max\n      __typename\n    }\n    writtenConsentForChildren {\n      label\n      maxAge\n      __typename\n    }\n    __typename\n  }\n  operatedBy\n  photos {\n    ...PhotoTypesFragment\n    __typename\n  }\n  pickupTypes {\n    type\n    __typename\n  }\n  postBookingInfo\n  poweredBy\n  primaryLabel {\n    text\n    type\n    __typename\n  }\n  primaryPhoto {\n    ...PhotoTypesFragment\n    __typename\n  }\n  representativePrice {\n    chargeAmount\n    currency\n    publicAmount\n    __typename\n  }\n  restrictions\n  reviewsStats {\n    allReviewsCount\n    isGoodScore\n    percentage\n    combinedNumericStats {\n      average\n      total\n      __typename\n    }\n    categoryRatingStats {\n      categoryName\n      total\n      average\n      __typename\n    }\n    __typename\n  }\n  shortDescription\n  supplierInfo {\n    isIndividual\n    details {\n      address\n      name\n      __typename\n    }\n    __typename\n  }\n  supportedFeatures {\n    alternativeTimeSlotsPartiallySupported\n    alternativeTimeSlotsSupported\n    indexable\n    isAutomated\n    hasFallbackLocale\n    liveAvailabilityCheckPartiallySupported\n    liveAvailabilityCheckSupported\n    rawContentWebviewTrackingSupported\n    reservationModificationPartiallySupported\n    __typename\n  }\n  slug\n  taxonomy {\n    categories {\n      label\n      slug\n      __typename\n    }\n    tags {\n      label\n      slug\n      __typename\n    }\n    type {\n      label\n      slug\n      __typename\n    }\n    __typename\n  }\n  timeZone\n  typicalDuration {\n    label\n    value\n    __typename\n  }\n  ufi\n  ufiDetails {\n    ...UfiDetailsFragment\n    __typename\n  }\n  contextUfiDetails {\n    ...UfiDetailsFragment\n    __typename\n  }\n  uniqueSellingPoints\n  whatsIncluded\n  flags {\n    flag\n    value\n    rank\n    __typename\n  }\n  itinerary {\n    type\n    __typename\n  }\n  distances {\n    distanceToAccommodation {\n      distanceDescription\n      distanceKm\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment AttractionsAddressFragment on AttractionsAddress {\n  address\n  city\n  country\n  googlePlaceId\n  id\n  instructions\n  latitude\n  locationType\n  longitude\n  publicTransport\n  zip\n  __typename\n}\n\nfragment PhotoTypesFragment on AttractionsPhoto {\n  hereProductPageDesktop\n  hereProductPageMobile\n  gallery\n  small\n  __typename\n}\n\nfragment UfiDetailsFragment on AttractionLocationResponse {\n  attractionsCount\n  bCityName\n  bInCityName\n  banners {\n    content\n    title\n    type\n    __typename\n  }\n  image\n  latitude\n  longitude\n  ufi\n  url {\n    city\n    country\n    prefix\n    __typename\n  }\n  countryName\n  __typename\n}\n"
url = "https://www.booking.com/dml/graphql?aid=397594&label=gog235jc-1DCAEoggI46AdIM1gDaEaIAQGYATG4AQfIAQzYAQPoAQH4AQKIAgGoAgO4AtTCw60GwAIB0gIkYTUyZTAwN2ItM2JhYy00MDhjLTllOWUtNmJmYjc1MjNjMDdh2AIE4AIB&sid=e5657fe75ac8ea4f509fb96b3c1c9352&lang=en-us"

id_bcn = -372490
destination_id = id_bcn

# Getting the payload
def get_data(id: int, page : int = 1, limit: int = 40 ):
    payload = json.dumps({
    "operationName": "SearchProducts",
    "variables": {
        "input": {
        "ufi": id,
        "extractFilterStats": True,
        "extractFilterOptions": True,
        "extractSorters": True,
        "extractSections": False,
        "limit": limit,
        "source": "search_box",
        "page": page,
        "filterBySupportedLanguage": []
        },
        "contextParams": {
        "urlCode": "",
        "test": False,
        "showInactive": False,
        "source": "search_box",
        "adPlat": "",
        "label": "gog235jc-1DCAEoggI46AdIM1gDaEaIAQGYATG4AQfIAQzYAQPoAQH4AQKIAgGoAgO4AtTCw60GwAIB0gIkYTUyZTAwN2ItM2JhYy00MDhjLTllOWUtNmJmYjc1MjNjMDdh2AIE4AIB"
        }
    },
    "extensions": {},
    "query": query
    })
    return requests.request("POST", url, headers=headers, data=payload).json()

# We generate a generator that will give us the payloads one by one. 
def get_all_attractions(id: int, page: int) -> list:
    print(id, page)
    while True:
        data = get_data(id, page)
        print("jeje",data)
        product_count = data["data"]["attractionsProduct"]["searchProducts"]["filterStats"]["filteredProductCount"]
        print(product_count, page)
        yield data["data"]["attractionsProduct"]["searchProducts"]["products"]

        if page * 40 > product_count:
            break
        page += 1

# Save all obtained data into a JSON
def save_json(results, id):
    with open(f'Booking/Files/attractions_{destination_id}.json','w') as jsonfile:
        json.dump(results, jsonfile, indent=4)


if __name__ == "__main__":
    parser = argparse.ArgumentParser() 
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--destination_id', type=str, help='destination id')
    #group.add_argument('--destination_name', type=str, help='destination name')
    args = parser.parse_args()

    products = []

    for products in get_all_attractions(id=int(args.destination_id), page = 1):
        products.extend(products)
    #print(get_data(destination_id))
    save_json(products, id=args.destination_id)

        
