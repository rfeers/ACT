import requests
import json

url = "https://www.booking.com/dml/graphql?label=gog235jc-1DCAEoggI46AdIM1gDaEaIAQGYAQm4AQfIAQzYAQPoAQGIAgGoAgO4Aqf5560GwAIB0gIkODU4ODU2MjctYTIzMi00MDQ1LWE4NmMtMGJhZmJlZWE2OTI22AIE4AIB&sid=e5657fe75ac8ea4f509fb96b3c1c9352&aid=397594&lang=en-gb"
headers = {
  'authority': 'www.booking.com',
  'accept': '*/*',
  'accept-language': 'en,ko;q=0.9',
  'content-type': 'application/json',
  'cookie': 'cors_js=1; _pxvid=5fc7c755-232d-11ee-95f0-221885d8371e; OptanonAlertBoxClosed=2023-07-15T16:35:00.718Z; FPID=FPID2.2.%2BDJsHTamLQ0fg4n1pcBuRxa2aJTcHU5m1zigE8mNWGU%3D.1691701378; rskxRunCookie=0; rCookie=9vuyq6v5tljp18n73lj3ll5nfeuh; _ga_FPD6YLJCJ7=GS1.1.1691951988.2.0.1691951988.0.0.0; lastRskxRun=1692037142015; _uetvid=fd6d56c03a0911eeafd539d5305baa2f; _ga_A12345=GS1.1.1694252366.4.0.1694252366.0.0.0; _pxhd=-pXnYSyZVenq9jJd86woFCCc%2FnVHiVublEJtcEz33FBi-uOxbIv3gFUfNE3H9W%2FKKIIpOVdfwBYaUizvER17DA%3D%3D%3AChpkpB1-RM2MAY50EqcVlJYXfY3O8g5tUFq3sbGmpQLl%2Fakl0FeCff%2FTMlJKf1wUGEuEMhUaFms%2FTN8EKSRo5yH0vKGnsoBU8sOSTGGpDGQ%3D; pcm_consent=consentedAt%3D2023-12-19T12%3A13%3A50.266Z%26countryCode%3DES%26expiresAt%3D2024-06-16T12%3A13%3A50.266Z%26implicit%3Dfalse%26regionCode%3DCT%26regulation%3Dgdpr%26legacyRegulation%3Dgdpr%26consentId%3Dfe67fc9b-0f5c-4754-a5c5-a0ff948cecfe%26analytical%3Dtrue%26marketing%3Dtrue; px_init=0; _gcl_au=1.1.548283850.1706090843; _ga=GA1.1.1376287762.1691701378; bkng_sso_ses=eyJib29raW5nX2dsb2JhbCI6W3siaCI6IkJDY3gra0VwZXlDZ3ZNMVJyV2JBL3MvUEJLdThuVUdKU2hHZXBFUnAxUHcifV19; bkng_sso_session=eyJib29raW5nX2dsb2JhbCI6W3sibG9naW5faGludCI6IkJDY3gra0VwZXlDZ3ZNMVJyV2JBL3MvUEJLdThuVUdKU2hHZXBFUnAxUHcifV19; _ga_4GY873RFCC=GS1.1.1706098740.1.1.1706099492.0.0.0; _ga_P07TP8FRGZ=GS1.1.1706098735.1.1.1706099522.0.0.0; _ga_G0GLDX0JXR=GS1.1.1706098711.1.1.1706099554.0.0.0; _ga_ME6FRX2E79=GS1.1.1706098904.1.1.1706099554.0.0.0; xp=02UmFuZG9tSVYkc2RlIyh9YbxZGyl9Y5%2BPUFj2JIAAGeHwifh%2B%2FE2FD%2FZccIJMIYZMishbF6PmXsA%3D; BJS=-; aws-waf-token=e77a7fdc-0749-48f1-bdb6-277b67d387aa:HQoAoh42Yt0DAAAA:grd8iI0M0t0a7rEvceMpvh09CrrpwX54+87UBxbGemGGPS5AnFICG8OFIlyLh+iONbHsFbQmoxXPA6y3OIWWTdy7mgZhwNJMZ0A1Iykblug+ndCogfUjoDxjov0unRrL+TC01iFqa+juOpy7SbJHBfT2K7en0bJ0BJkXtryar2B5r9SLZeVbZIejnCdTUrgWOMMC3T8RECqEFEdaXtRrQw==; lastSeen=1706687661684; OptanonConsent=isGpcEnabled=0&datestamp=Wed+Jan+31+2024+08%3A54%3A21+GMT%2B0100+(Central+European+Standard+Time)&version=202310.2.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=d2dfd35a-50fa-4bc5-938d-1699f9630541&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A0%2CC0004%3A0&implicitConsentCountry=GDPR&implicitConsentDate=1706090839311&AwaitingReconsent=false&backfilled_at=1689438901145&backfilled_seed=1&geolocation=ES%3BCT; bkng_sso_auth=CAIQsOnuTRqIAeNaw5jTtZs6HClo04YalKwHWCPXH6SPs2+ZT/BC+1cIWRssZKVabmbKoP5X8v5/+hn+cJ4shJ0KNDfIKvIkoCL2hH+KCfnOrxJeGe3DTx8BLtiNrAgEJb5COI50tmf2ULE3GO6CKMQJG1UGx5jkrkWu4EsNHUrs/1a7tl/DPufyUHbnMg1rQQc=; bkng=11UmFuZG9tSVYkc2RlIyh9Yaa29%2F3xUOLbp8EZRXTVzcplqnw68te1JPgaYCc%2FVT1%2BH%2Fni%2FLNSt66Ek8uSudkSAc5Gewt2aQz67HTIx5s2yA0YPCnGYG0PjHd8M8OJ4kABe9uR2c3ZuR7ho1pAqOTVZP70SOZ1jTwXtY05Bkkx9%2F0eISbcd5t8sAZr3h6Xg8a9DlfJNzzD%2FYlOm%2BY3Fiu%2FBvcOUfF2uQzb3mXP2rNG3yjE8HGafZ38jMBN4dTiQ%2BDf; _pxhd=3HNhYf%2FIEmuoek0KR1xQpQkrnh7FeR2blH0GBAxKmgS5bT1wf8Lc256hVC3s4AtJGcovVhihms2rhuG5iyd9yA%3D%3D%3AMPCeM-s0c5Et7XlJHt1QloJJ7gWv4tLPHepcIQSGu8QDFDEeC1q96CLKILA79krdVIaRGeKC-zMOH1FxKb5uyt6FrVenr9-eHvGmydM7hv8%3D; bkng=11UmFuZG9tSVYkc2RlIyh9YZN305pdDMb%2Bl5xE4mJnqUcdqxpl7ynPXnmqvvMwduxooYAL95%2FN4ryUqOU%2BHcqnptol8aKfCXYLXe1wcdpBpF0WaXJXBo%2BOgXKHN%2FFf%2FmdLNwmflna%2Fv3wg4fhc6zA78MwT4tpFNcG0KRgE33OpJFBKa5tsGnluX%2BYRPQE8iVM%2BdnvuZo6ai7Gd6cpBmltRZw%3D%3D; bkng_sso_auth=CAIQsOnuTRpm6tlNpMjG7bj1ZI7tib976dEuWAuO201UT0wjiaAHpLnsCojIAHL6sWwm8AFereyILOkVf2LswW9BzGG65BexztKmS1R1GEcSKIaY1keqD6p/EvEKp7Fpdd2wkrqsmTbvbgpOQjCh; pcm_consent=analytical%3Dfalse%26countryCode%3DES%26consentId%3D41d5534f-dd6b-4b19-b11f-e7185cd9d214%26consentedAt%3D2023-12-20T07%3A43%3A44.257Z%26expiresAt%3D2024-06-17T07%3A43%3A44.257Z%26implicit%3Dtrue%26marketing%3Dfalse%26regionCode%3DCT%26regulation%3Dgdpr%26legacyRegulation%3Dgdpr; px_init=0; bkng_sso_auth=CAIQsOnuTRpmeYH2v2VPApLrpeqxbKaOXIK8xqXbieo5Yccrn+KIusS55Z4djOfMsRflL4jxTcqeyU5Q/N05LFCBDa8FbbzRUrKku7n8MBCjKPmGMHU1/odohsOL/7hDQNCNe+OYCrCA0SIaWhWz; pcm_consent=analytical%3Dfalse%26countryCode%3DES%26consentId%3D88a981bf-3048-4428-936e-c8cc2dfa033c%26consentedAt%3D2023-12-20T08%3A03%3A48.131Z%26expiresAt%3D2024-06-17T08%3A03%3A48.131Z%26implicit%3Dtrue%26marketing%3Dfalse%26regionCode%3DCT%26regulation%3Dgdpr%26legacyRegulation%3Dgdpr',
  'origin': 'https://www.booking.com',
  'referer': 'https://www.booking.com/attractions/searchresults/es/barcelona.en-gb.html?label=gog235jc-1DCAEoggI46AdIM1gDaEaIAQGYAQm4AQfIAQzYAQPoAQGIAgGoAgO4Aqf5560GwAIB0gIkODU4ODU2MjctYTIzMi00MDQ1LWE4NmMtMGJhZmJlZWE2OTI22AIE4AIB&aid=397594&source=search_box&query=Girona',
  'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"macOS"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
  'x-booking-context-action-name': 'attractions_index',
  'x-booking-context-aid': '397594',
  'x-booking-csrf-token': 'eyJhbGciOiJIUzUxMiJ9.eyJpc3MiOiJjb250ZXh0LWVucmljaG1lbnQtYXBpIiwic3ViIjoiY3NyZi10b2tlbiIsImlhdCI6MTcwNjY4NzY2MSwiZXhwIjoxNzA2Nzc0MDYxfQ.ki-OMoXEj5IBym6wk1RUHEOFjkfJuNYL6B2FcCaMnPe2Pqv-AAo6Q0cTiaztVQyWwNz0EMyV9LFW49Kjh65_Ng',
  'x-booking-et-serialized-state': 'EfXznrmJoTa50HAA0bCN8iU97_3af4--C03u2i9e0NM-FPklJJcdkEzqtyVYDOBtcvA165h4WDuLRCwDHBbr9Sw',
  'x-booking-pageview-id': 'a5303796bc57001f',
  'x-booking-site-type-id': '1',
  'x-booking-topic': 'capla_browser_b-attractions-product-frontend-capla'
}
query = "query SearchAutoComplete($input: AttractionsSearchAutoCompleteInput!, $contextParams: AttractionsContextParamsInput) {\n  attractionsProduct {\n    searchAutoComplete(input: $input, contextParams: $contextParams) {\n      __typename\n      ... on AttractionsSearchAutoCompleteResponse {\n        products {\n          ...AttractionsSearchProductSuggestionFragment\n          __typename\n        }\n        destinations {\n          ...AttractionsSearchDestinationSuggestionFragment\n          __typename\n        }\n        __typename\n      }\n      ... on AttractionsOrchestratorErrorResponse {\n        error\n        message\n        statusCode\n        __typename\n      }\n    }\n    __typename\n  }\n}\n\nfragment AttractionsSearchProductSuggestionFragment on AttractionsSearchProductSuggestion {\n  title\n  productId\n  productSlug\n  taxonomySlug\n  imageUrl\n  cityUfi\n  cityName\n  cityUrlName\n  countryCode\n  tracking {\n    prid\n    prPageViewId\n    __typename\n  }\n  __typename\n}\n\nfragment AttractionsSearchDestinationSuggestionFragment on AttractionsSearchDestinationSuggestion {\n  region\n  ufi\n  cc1\n  cityUrl\n  srUrl\n  productCount\n  destType\n  country\n  cityName\n  imageUrl\n  __typename\n}\n"

def get_dest(city: str) -> dict:
  payload = json.dumps({
    "operationName": "SearchAutoComplete",
    "variables": {
      "input": {
        "limit": 4,
        "query": city
      },
      "contextParams": {
        "urlCode": "",
        "test": False,
        "showInactive": False,
        "source": "search_box",
        "adPlat": "",
        "label": "gog235jc-1DCAEoggI46AdIM1gDaEaIAQGYAQm4AQfIAQzYAQPoAQGIAgGoAgO4Aqf5560GwAIB0gIkODU4ODU2MjctYTIzMi00MDQ1LWE4NmMtMGJhZmJlZWE2OTI22AIE4AIB"
      }
    },
    "extensions": {},
    "query": query
  })

  response = requests.request("POST", url, headers=headers, data=payload).json()

  try:
    dest = {
      "region": response["data"]["attractionsProduct"]["searchAutoComplete"]["destinations"][0]["region"],
      "ufi": response["data"]["attractionsProduct"]["searchAutoComplete"]["destinations"][0]["ufi"],
      "cityName": response["data"]["attractionsProduct"]["searchAutoComplete"]["destinations"][0]["cityName"],
      "boolean": response["data"]["attractionsProduct"]["searchAutoComplete"]["destinations"][0]["region"] == "Catalonia",
      "municipiName": city
    }

    return dest
  
  except: 
    pass

  


#data = get_dest("Girona")
#print(data)


