import requests
import json
import argparse # Library to set input variables


# Variables init
url = "https://www.tripadvisor.com/data/graphql/ids"

headers = {
  'authority': 'www.tripadvisor.com',
  'accept': '*/*',
  'accept-language': 'en,ko;q=0.9',
  'content-type': 'application/json',
  'cookie': 'TASameSite=1; TAUnique=%1%enc%3AzSjvhiwVWGmp9BPDAWs7C4aWOm4JvlzQNxDsvu7L9MqOCygq0A0uIjtho%2BB0OUm%2BNox8JbUSTxk%3D; TASSK=enc%3AAP6r9pBF7AoJ0dLCEfF8RzsJBPewvARz9o7sV494CC%2FDI99hzSK1UB3jn0%2BhIXXVHlDgZiW7KuzmJ%2FooaKumdAHawQFZGHZqbauxLy7xtZUUNsVBiFmWcQzhbPIwg7XRZw%3D%3D; OptanonAlertBoxClosed=2023-12-21T09:03:20.810Z; eupubconsent-v2=CP3InNgP3InNgAcABBENAfEsAP_gAEPgACiQg1QoYAAgAEAAQAAwACIAFAAhABUAGQAOQAeACGAEgASwAnACgAFUALAAtABfADEAMoAaABqADmAHYAfABCgCIAIwASQAmABOACgAFWALQAtwBdAF-AMIAxQBkAGUANEAbABtADfAHIAc4A7gDxAIAAhYBEAEXAI4AjwBJwCVAJaATIBNgCdAFCAKQAVAArQBZQC4ALkAX0AwADBAGGAMcAZ0A0gDVgGuAbAA4IBxAHJAPEA84B8AHzAPsA_YB_gIBAQYBBwCIwEYARqAjgCOgEigJKAk0BLQEuAJgATgAnUBPQE_AKLAUgBSQCmgFZgK8Ar4BZgC4AFzALsAXkAvoBgQDFAGSAM1AZwBnQDQQGmAagA2gBtgDcAHCAO2Ad8A80B6gHrAPeAfIA-oB-4D_gQBAgQCBQEEgIMgQkBCcCFwIYAQ2AiKBEoETQIpAioBFgCLwEagI4AR2Aj0BIgCSwEqAJWgSyBLQCXgExAJlgTSBNQCbIE4gTlAnYCdwE_wKGAoiBRgFGwKQApEBScClgKXAU2AqIBUkCqQKqAVcArKBXwFfwLDAsWBZAFlALMAWeAtEBasC1wLYgW6Bb0C4QLigXKBc0C6ALugXkBecC9gL3gX6Bf0DAAMDAYyBFeCbIJvQTgBOEINQg1QWwAEQAKAAuABwAHgAVAAuABwADwAIAASAAvgBiAGUANAA1AB4AD8AIgATAAoABTACrAFsAXQAxABoADeAH4AQkAiACJAEcAJYATQAwABhgDLAGaANkAcgA-IB9gH7AP8BAACDgERgIsAjABGoCOAI6ASIAkoBPwCoAFzALyAX0AxQBnwDXgG0ANwAdIA7YB9gD_gImAReAj0BIgCVAErAJigTIBMoCZwE7AKHgUgBSICkwFNgKkAVVAsQCxQFlALRgWwBbIC3QFyALoAXaAu-BeQF5gL6AYJBNsE3IJvAm-BOEINQBQIAQADoALgA2QCIAGEAToAuQCBwQAMADoAVwBEADCAJ0AgcGADgA6AC4ANkAiABhAFyAQOEABwAdADZAIgAYQBOgC5AIHCgAYAXADCAQOGAAwBXAGEAgcOADgA6AFcARAAwgCdAIHARXIAAgDCAQOJAAwCIAGEAgcUACgA6AIgAYQBOgEDgAAA.f_wACHwAAAAA; OTAdditionalConsentString=1~43.46.55.61.70.83.89.93.108.117.122.124.135.136.143.144.147.149.159.192.196.202.211.228.230.239.259.266.286.291.311.317.320.322.323.327.338.367.371.385.394.397.407.413.415.424.430.436.445.453.482.486.491.494.495.522.523.540.550.559.560.568.574.576.584.587.591.737.802.803.820.821.839.864.899.904.922.931.938.979.981.985.1003.1027.1031.1040.1046.1051.1053.1067.1085.1092.1095.1097.1099.1107.1135.1143.1149.1152.1162.1166.1186.1188.1201.1205.1215.1226.1227.1230.1252.1268.1270.1276.1284.1290.1301.1307.1312.1345.1356.1364.1365.1375.1403.1415.1416.1421.1440.1449.1455.1495.1512.1516.1525.1540.1548.1555.1558.1570.1577.1579.1583.1584.1591.1603.1616.1638.1651.1653.1667.1677.1678.1682.1697.1699.1703.1712.1716.1721.1725.1732.1745.1750.1765.1769.1782.1786.1800.1810.1825.1827.1832.1838.1840.1842.1843.1845.1859.1866.1870.1878.1880.1889.1899.1917.1929.1942.1944.1962.1963.1964.1967.1968.1969.1978.2003.2007.2008.2027.2035.2039.2047.2052.2056.2064.2068.2072.2074.2088.2090.2103.2107.2109.2115.2124.2130.2133.2135.2137.2140.2145.2147.2150.2156.2166.2177.2183.2186.2205.2213.2216.2219.2220.2222.2225.2234.2253.2279.2282.2292.2299.2305.2309.2312.2316.2322.2325.2328.2331.2334.2335.2336.2337.2343.2354.2357.2358.2359.2370.2376.2377.2387.2392.2400.2403.2405.2407.2411.2414.2416.2418.2425.2440.2447.2461.2462.2465.2468.2472.2477.2481.2484.2486.2488.2493.2498.2499.2501.2510.2517.2526.2527.2532.2535.2542.2552.2563.2564.2567.2568.2569.2571.2572.2575.2577.2583.2584.2596.2604.2605.2608.2609.2610.2612.2614.2621.2628.2629.2633.2636.2642.2643.2645.2646.2650.2651.2652.2656.2657.2658.2660.2661.2669.2670.2677.2681.2684.2687.2690.2695.2698.2713.2714.2729.2739.2767.2768.2770.2772.2784.2787.2791.2792.2798.2801.2805.2812.2813.2816.2817.2821.2822.2827.2830.2831.2834.2838.2839.2844.2846.2849.2850.2852.2854.2860.2862.2863.2865.2867.2869.2873.2874.2875.2876.2878.2880.2881.2882.2883.2884.2886.2887.2888.2889.2891.2893.2894.2895.2897.2898.2900.2901.2908.2909.2913.2914.2916.2917.2918.2919.2920.2922.2923.2927.2929.2930.2931.2940.2941.2947.2949.2950.2956.2958.2961.2963.2964.2965.2966.2968.2973.2975.2979.2980.2981.2983.2985.2986.2987.2994.2995.2997.2999.3000.3002.3003.3005.3008.3009.3010.3012.3016.3017.3018.3019.3024.3025.3028.3034.3037.3038.3043.3048.3052.3053.3055.3058.3059.3063.3066.3068.3070.3073.3074.3075.3076.3077.3078.3089.3090.3093.3094.3095.3097.3099.3104.3106.3109.3112.3117.3119.3126.3127.3128.3130.3135.3136.3145.3150.3151.3154.3155.3163.3167.3172.3173.3182.3183.3184.3185.3187.3188.3189.3190.3194.3196.3209.3210.3211.3214.3215.3217.3219.3222.3223.3225.3226.3227.3228.3230.3231.3234.3235.3236.3237.3238.3240.3244.3245.3250.3251.3253.3257.3260.3268.3270.3272.3281.3288.3290.3292.3293.3296.3299.3300.3306.3307.3314.3315.3316.3318.3324.3327.3328.3330.3331.3531.3731.3831.3931.4131.4531.4631.4731.4831.5031.5231.6931.7031.7235.7831.7931.8931.9731.10231.10631.10831.11031.11531.12831.13632.13731.14237.16831; TATrkConsent=eyJvdXQiOiJTT0NJQUxfTUVESUEiLCJpbiI6IkFEVixBTkEsRlVOQ1RJT05BTCJ9; _ga=GA1.1.1230809481.1703149401; VRMCID=%1%V1*id.10568*llp.%2FAttractions-g187497-Activities-Barcelona_Catalonia%5C.html*e.1703754378137; TASID=81CA4D2DCC5BDDA9F857F56BC63EDFE4; TADCID=6OpC3KWhBCq3AT5iABQCmq6heh9ZSU2yA8SXn9Wv5Hsg_eYb6bhEsU29t_gBsQlS8hFscpp3JmXZjfyOm3krXSNQh60B3rBdGfI; PAC=AMJRCdkJULwameXBDsesY74Vhp2IKFznYaak-4cHZeGvXoSRVRSwHjdYACdYJWhrAdc5EY5zdTkyNabaR8NOk22Puz8NbConvqaIIRAi9nSqkJAL3I3MhMrg5DkCTZlCxT4GNja2GjS9Buex4ALtOsXmQ97j1etz6icmDQE97PEkMjYiTu1P2-RdLtzTsjAodw%3D%3D; _abck=10CACDDA380D99327E28B9AE9D958583~-1~YAAQPHR7XFjFMACNAQAA6+EIQAsg1n14mi14ZfAaTieFc1XS2moUsmlJwSilGIlc62uztXGUvBFHEp/a1phs7DcGb0qccylQ2fKQ6XBehw6SQQ1T+aGx9P5EeUggNFf8/7o8aTmTdj7DJcOscQ5wRsJJ2vFdXfklnpq/BMzCtqjrTkwBaEqDK5Gl4duwVo7Dsjgt6JSEhsxbCw3Ly1Xb+03Unq+1tdhS+fFBGDvmGjcLe7O5hbKfCRQCx+jI0dJrkP3X0fKSBIJS40bQCbCtLkgYcLVL9eJCTXujiT5cqBeToYWNkCQ8P/SxUFDw+rwVTz+f2CBn2pwjQNlTDoH2NiLDWN9f0IXGABXZpkmm1hkaMbmP5SOZDsjDhz4nSzPybxXsF7LhPunmebfUrjtp~-1~-1~-1; bm_sz=56664D812CF394510276BC1F0D62AB9D~YAAQPHR7XFnFMACNAQAA6+EIQBaIPL60fETFGkOW7lMt1NGfKKDdJxZ+VQXeb4ysuqLnUW235xJdO3ffct66nzq2ehXCd67buYvl9Ok1M7wAw9C0qcCP7vAFZ/uejfyWxQBy1OnU9+ioEQg0bLaHcoNxvYkkxe8DOwnzRopyf6QaMTKO3COGik93FhduvQQXHynRuv8bzJ7dOpe+SjlCjJWhdj2GgRIZnjoyMZTI6PpX3BlzEmDOGsn+/aYhqcBli3zNIExwZ79Egxc2eYWvxILrCpz0FiG+s3kLsuABKH5ojbgUZP+4Mwdwvl60ARgwXXFeGbAn3hO0lvmvspB8Ql7tNw==~3356981~3687988; pbjs_sharedId=3db31b6e-545f-4bd0-9fe7-20e6835ea314; pbjs_sharedId_cst=0ixmLIcsmw%3D%3D; _lr_sampling_rate=0; _lr_retry_request=true; _lr_env_src_ats=false; pbjs_unifiedID=%7B%22TDID_LOOKUP%22%3A%22FALSE%22%2C%22TDID_CREATED_AT%22%3A%222024-01-25T09%3A52%3A27%22%7D; pbjs_unifiedID_cst=0ixmLIcsmw%3D%3D; ServerPool=C; PMC=V2*MS.34*MD.20231221*LD.20240125; TATravelInfo=V2*AY.2024*AM.2*AD.4*DY.2024*DM.2*DD.5*A.2*MG.-1*HP.2*FL.3*DSM.1706176803858*RS.1; roybatty=TNI1625!APgOH3NWLU0CSx8LXy7p1wTtqfgbJsqoKyimyueu6739aRaatUyjGB5tz0qDgFv9BtNLB8Spwkrcf2xN7nadRw1dGmKIs0tzoG4zZ3a%2BQcEPh5EomdGxElPzJHtMzi%2FnvuRSP349bw9EuNSD37oiMpccvY%2FwZ%2Bqy0hCBnh3US%2Fsj2zHq02ed3SYM6KhfZzoVEg%3D%3D%2C1; ab.storage.deviceId.6e55efa5-e689-47c3-a55b-e6d7515a6c5d=%7B%22g%22%3A%22a261d3b7-8b66-0f51-5e1f-46ee3b9d7fdd%22%2C%22c%22%3A1706176805529%2C%22l%22%3A1706176805529%7D; SRT=TART_SYNC; TART=%1%enc%3AKQVDKAxiMUpR3a1oF29sAFJfU%2Fi6Cq6s6BLaHSVqHerLKM5RzWgR0vucl2FVQrAEb2f8xit%2B59o%3D; ab.storage.sessionId.6e55efa5-e689-47c3-a55b-e6d7515a6c5d=%7B%22g%22%3A%22ae4656b2-3d50-7a40-f862-7cd681de3289%22%2C%22e%22%3A1706176885709%2C%22c%22%3A1706176805527%2C%22l%22%3A1706176825709%7D; __vt=WFmblYdbCzhw9mYQABQCwRB1grfcRZKTnW7buAoPsSr-rg-vOeyW8Tce56yggGavqW3G7HIq5159b-vHlOZH_ZTpBCc0hDSGfvlWC7DC4dDsWsXSwiyKFxwtrMqEv1e0ssPBoaVoY_m9H0WaLD1ZcNrY1A; TAUD=LA-1706176364618-1*RDD-1-2024_01_25*HDD-439154-2024_02_04.2024_02_05*ARC-493247*LD-1041152-2024.2.4.2024.2.5*LG-1041154-2.1.F.; OptanonConsent=isGpcEnabled=0&datestamp=Thu+Jan+25+2024+11%3A10%3A09+GMT%2B0100+(Central+European+Standard+Time)&version=202310.2.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=b003fe64-0e47-4926-843f-c5caca18b6d3&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0004%3A1%2CC0002%3A1%2CC0003%3A1%2CV2STACK42%3A1&geolocation=ES%3BCT&AwaitingReconsent=false; TASession=V2ID.81CA4D2DCC5BDDA9F857F56BC63EDFE4*SQ.24*LS.Attractions*HS.recommended*ES.popularity*DS.5*SAS.popularity*FPS.oldFirst*FA.1*DF.0*TRA.true*LD.187496*EAU._; datadome=lH1Xjkni_hOLxr7XWkdUDsN4dqV0xpoI1zVulro0h5Z0u_GefPldPvAllWQ7jAjI~0PaZ_CFGJ8fYUept9vqvOkpWi_zkoNG4XN0j~fSwh~MUDXv~FJPhbTX8wBiykZP; _ga_QX0Q50ZC9P=GS1.1.1706176339.4.1.1706177427.29.0.0; TAUnique=%1%enc%3A1y15LIMvA6q2Hh8Smu730nYwnxzQNUvBcKGOtvgKLJ7MmHDAQal0fqEou1Bp5ryzNox8JbUSTxk%3D; _abck=3409BDC2293B1554BA31DFA546DF27F5~-1~YAAQjYlJF+xSF2KMAQAADlqPkAt64mNXwbpntIKSPM5PpYv8d9QRinhpVKSiCpjhsvloJA572gcsiiA8OAWd4EPunrZcIRAKvNSYz29QS3by0AayMZviJq8ySvhzjuVKq6SWTNXGM6qPNArtnnZpDXRZ4s7p8zAe1ygXNGlOfSEXTJtmufrFqQ1MVvR+BwsMTDGUv4YVWCzqWlY2n3Pl/VCunIvDH7mHbzGUtGcGcwiRee2+h1D32oNxh6BXH0C3Qg84UKZjlUlx7ipJ5hjw6YUUhzGe4cxMIm35p1toJ3DgYXPM7ySz97Lfsca7MUMx7A5g4Gm6jnxmO8iMASqsi8NNtdqPujYH+mPsUuW34djpwBgWTZdchqHj7pI4F106VIz6vic98SrxX30a~-1~-1~-1; PAC=AImJqwIf9kXkAOwS7LfTdUMHHA5b5Q5tAr-KACthmrHIqiOFPAXp96u-QyK07PElFJnNStRvYvTJwUPSq-CtUfbAEKvgK5CaKQBjNin_Rtk6hDfmqOZUiPppS8AVApkz8nSjPPjKnoSiRfx0600tOD7pt-NSol9udAccyCl0bXfyfCcG0sSjKPfAJxCk8AZGx_yidfoK2SJLaGxWMiMefXwOx9IUURicaNNBEgBSnubdE5GFtFFyEmey_k3VBeooGlIcblY5WPIUb-Qjuy14WscsNLmV2X9bSY_oAEp_AKkfrd21xBSpOLJrf-bSZ9dQvfWawP5zdzLGGo6TTuLltXz8cNolOg9IPUjCFsbgsPfe-Fd5t-BkSwNtMvI8heZbaQ%3D%3D; PMC=V2*MS.95*MD.20231220*LD.20231220; TADCID=dmObudYYt7GcgFfXABQCCKy0j55CTpGVsECjuwJMq3pWH9IV9bVAKEOPOFADePMSq7nB8BULXbMyQ5CmrXh0rAikUilJ9WwO9pw; TASSK=enc%3AAK6NtFZnCkd9%2Bb1N6Y7G9uoZd9Gr3nyx2rxLVFcGvzkmy7RTl76Zg9XLRQWeAZaARBA08KEq5pd%2F%2BeNGWqeg%2FPU%2Ftfj4yjwGYZkS%2BskwkWNeckxh954lwlfsRm0X7xPZuw%3D%3D; TASameSite=1; __vt=p--OYwHAmXyCkBA5ABQCwRB1grfcRZKTnW7buAoPsSr-rReq1GcIk766F2GdnPbwIVYCO4797cuZ67NyGnivbgtg5aBEYxFx5izzi4f8gA1JTjrXCi-O7aeFeW0LpYoyurXjJGe_bdei3hCbHxf1KFdIFw',
  'origin': 'https://www.tripadvisor.com',
  'referer': 'https://www.tripadvisor.com/Attractions-g187496-Activities-Catalonia.html',
  'sec-ch-device-memory': '8',
  'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
  'sec-ch-ua-arch': '"arm"',
  'sec-ch-ua-full-version-list': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.216", "Google Chrome";v="120.0.6099.216"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-model': '""',
  'sec-ch-ua-platform': '"macOS"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'same-origin',
  'sec-fetch-site': 'same-origin',
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

cat_id = 187496

# getting the payload
def get_data(geoId: int, page: int) -> dict:
    page = str(page)
    payload = json.dumps([
    {
        "variables": {
        "navigations": {
            "clientRequestTimestampMs": 1706177427431,
            "request": [
            {
                "eventTimestampMs": 1706177427431,
                "fromPage": "AttractionsFusion",
                "fromParams": [
                {
                    "key": "geoId",
                    "value": str(geoId)
                },
                {
                    "key": "contentType",
                    "value": "attraction"
                },
                {
                    "key": "webVariant",
                    "value": "AttractionsFusion"
                }
                ],
                "fromPath": "/Attractions-g187496-Activities-Catalonia.html",
                "fromRoute": "{\"page\":\"AttractionsFusion\",\"params\":{\"geoId\":187496,\"contentType\":\"attraction\",\"webVariant\":\"AttractionsFusion\"},\"path\":\"/Attractions-g187496-Activities-Catalonia.html\",\"fragment\":\"\"}",
                "identifierType": "TA_PERSISTENTCOOKIE",
                "navigationType": "USER_INITIATED",
                "opaqueIds": [],
                "origin": "https://www.tripadvisor.com",
                "referrer": "https://www.tripadvisor.com/Attractions-g187496-Activities-Catalonia.html",
                "toPage": "AttractionsFusion",
                "toParams": [
                {
                    "key": "geoId",
                    "value": str(geoId)
                },
                {
                    "key": "contentType",
                    "value": "attraction"
                },
                {
                    "key": "webVariant",
                    "value": "AttractionsFusion"
                },
                {
                    "key": "pagee",
                    "value": page
                },
                {
                    "key": "sort",
                    "value": "undefined"
                },
                {
                    "key": "filters",
                    "value": "[]"
                }
                ],
                "toPath": "/Attractions-g187496-Activities-Catalonia.html",
                "toRoute": "{\"page\":\"AttractionsFusion\",\"params\":{\"geoId\":187496,\"contentType\":\"attraction\",\"webVariant\":\"AttractionsFusion\",\"pagee\":\"30\",\"filters\":[]},\"path\":\"/Attractions-g187496-Activities-Catalonia.html\",\"fragment\":\"\"}",
                "uid": "LIT@3Wj13aocIQi1HUDAsSnN",
                "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
            }
            ]
        }
        },
        "extensions": {
        "preRegisteredQueryId": "8f5c28f35caeff98"
        }
    },
    {
        "variables": {
        "page": "AttractionsFusion",
        "params": [
            {
            "key": "geoId",
            "value": str(geoId)
            },
            {
            "key": "contentType",
            "value": "attraction"
            },
            {
            "key": "webVariant",
            "value": "AttractionsFusion"
            },
            {
            "key": "pagee",
            "value": page
            },
            {
            "key": "sort",
            "value": "undefined"
            },
            {
            "key": "filters",
            "value": ""
            }
        ],
        "route": {
            "page": "AttractionsFusion",
            "params": {
            "geoId": geoId,
            "contentType": "attraction",
            "webVariant": "AttractionsFusion",
            "pagee": page,
            "filters": []
            }
        }
        },
        "extensions": {
        "preRegisteredQueryId": "f742095592a84542"
        }
    },
    {
        "variables": {
        "pageName": "AttractionsFusion",
        "relativeUrl": "/Attractions-g187496-Activities-Catalonia.html",
        "parameters": [
            {
            "key": "geoId",
            "value": str(geoId)
            },
            {
            "key": "contentType",
            "value": "attraction"
            },
            {
            "key": "webVariant",
            "value": "AttractionsFusion"
            },
            {
            "key": "pagee",
            "value": page
            },
            {
            "key": "sort",
            "value": "undefined"
            },
            {
            "key": "filters",
            "value": ""
            }
        ],
        "route": {
            "page": "AttractionsFusion",
            "params": {
            "geoId": geoId,
            "contentType": "attraction",
            "webVariant": "AttractionsFusion",
            "pagee": page,
            "filters": []
            }
        }
        },
        "extensions": {
        "preRegisteredQueryId": "1a7ccb2489381df5"
        }
    },
    {
        "variables": {
        "page": "AttractionsFusion",
        "pos": "en-US",
        "parameters": [
            {
            "key": "geoId",
            "value": str(geoId)
            },
            {
            "key": "contentType",
            "value": "attraction"
            },
            {
            "key": "webVariant",
            "value": "AttractionsFusion"
            },
            {
            "key": "pagee",
            "value": page
            },
            {
            "key": "sort",
            "value": "undefined"
            },
            {
            "key": "filters",
            "value": ""
            }
        ],
        "factors": [
            "TITLE",
            "META_DESCRIPTION",
            "MASTHEAD_H1",
            "MAIN_H1",
            "IS_INDEXABLE",
            "RELCANONICAL"
        ],
        "route": {
            "page": "AttractionsFusion",
            "params": {
            "geoId": geoId,
            "contentType": "attraction",
            "webVariant": "AttractionsFusion",
            "pagee": page,
            "filters": []
            }
        }
        },
        "extensions": {
        "preRegisteredQueryId": "8ff5481f70241137"
        }
    },
    {
        "variables": {
        "uid": "LIT@jSJmHGJqExcitfTYJWwG",
        "sessionId": "81CA4D2DCC5BDDA9F857F56BC63EDFE4",
        "currency": "USD",
        "sessionType": "DESKTOP",
        "locationId": 187496,
        "page": "AttractionsFusion"
        },
        "extensions": {
        "preRegisteredQueryId": "fa5da6ee0b1deed3"
        }
    },
    {
        "variables": {
        "locationId": 187496,
        "uid": "LIT@jSJmHGJqExcitfTYJWwG",
        "sessionId": "81CA4D2DCC5BDDA9F857F56BC63EDFE4",
        "currency": "USD"
        },
        "extensions": {
        "preRegisteredQueryId": "42bec0ee6ec0bfd1"
        }
    },
    {
        "variables": {
        "params": {
            "geoId": geoId,
            "contentType": "attraction",
            "webVariant": "AttractionsFusion",
            "pagee": "30",
            "filters": []
        },
        "page": "AttractionsFusion",
        "fragment": ""
        },
        "extensions": {
        "preRegisteredQueryId": "a26bffd43d0e25b6"
        }
    },
    {
        "variables": {
        "request": [
            {
            "locationIds": [
                187496,
                187427
            ],
            "timestamp": "1706177427435",
            "pageContentId": None,
            "pageType": None
            }
        ]
        },
        "extensions": {
        "preRegisteredQueryId": "bc99048f6dd84da1"
        }
    },
    {
        "variables": {
        "request": {
            "tracking": {
            "screenName": "AttractionsFusion",
            "pageviewUid": "LIT@jSJmHGJqExcitfTYJWwG"
            },
            "routeParameters": {
            "geoId": geoId,
            "contentType": "attraction",
            "webVariant": "AttractionsFusion",
            "pagee": page,
            "filters": [
                {
                "id": "allAttractions",
                "value": [
                    "true"
                ]
                }
            ]
            },
            "boundingBox": {
            "northEastCorner": {
                "latitude": 42.549600613083015,
                "longitude": 3.3739433112294197
            },
            "southWestCorner": {
                "latitude": 40.618848735022226,
                "longitude": 0.7191416887706147
            }
            },
            "updateToken": None
        },
        "commerce": {
            "attractionCommerce": {
            "pax": [
                {
                "ageBand": "ADULT",
                "count": 2
                }
            ]
            }
        },
        "tracking": {
            "screenName": "AttractionsFusion",
            "pageviewUid": "LIT@jSJmHGJqExcitfTYJWwG"
        },
        "sessionId": "81CA4D2DCC5BDDA9F857F56BC63EDFE4",
        "unitLength": "MILES",
        "currency": "USD",
        "currentGeoPoint": None,
        "sectionTypes": [
            "Mixer_ArticlesHeroStoriesHighlightSection",
            "Mixer_ArticlesMosaicSection",
            "Mixer_FeaturedStoriesSection",
            "Mixer_Shelf",
            "Mixer_EditorialFeatureSection",
            "Mixer_FullImageFeatureCardSection",
            "Mixer_InsetImageFeatureCardSection",
            "Mixer_CoverPageHeroSection",
            "Mixer_AdPlaceholderSection",
            "Mixer_CategorySearchesSection",
            "Mixer_FactSheetSection",
            "Mixer_PromotionalBannerSection",
            "Mixer_TravelersChoiceSection",
            "Mixer_InteractiveMapSection",
            "Mixer_ArticlesKeepExploringSection",
            "Mixer_AsFeaturedInWidgetSection",
            "Mixer_VideoPlayerSection",
            "Mixer_ReviewExcerptSection",
            "Mixer_BrandChannelCommerceSection",
            "Mixer_PlanYourTripSection",
            "Mixer_BuildTripWithAIHomeSection",
            "Mixer_LocalGuidesSection",
            "Mixer_SponsoredTourismSection",
            "Mixer_CollectionShelfSection"
        ],
        "sectionContentTypes": [
            "Mixer_DescriptionAndCarousel",
            "Mixer_FlexGrid",
            "Mixer_ImageAndCarousel",
            "Mixer_MediumCarousel",
            "Mixer_NarrowCarousel",
            "Mixer_PlusCarousel",
            "Mixer_TravelerSpotlightCarousel",
            "Mixer_WideCarousel",
            "Mixer_ProminentFlexList"
        ],
        "cardTypes": [
            "Mixer_PoiVerticalStandardCard",
            "Mixer_PoiVerticalMerchandisingCard",
            "Mixer_PoiVerticalDescriptionCard",
            "Mixer_PoiVerticalNameWithButtonCard",
            "Mixer_GeoVerticalMinimalCard",
            "Mixer_TripVerticalContributorCard",
            "Mixer_VrGeoVerticalMinimalCard",
            "Mixer_GeoImageBackgroundCard",
            "Mixer_CustomImageBackgroundCard",
            "Mixer_AttractionTaxonomyImageBackgroundCard",
            "Mixer_LinkPostEditorialCard",
            "Mixer_TripEditorialCard",
            "Mixer_VideoEditorialCard",
            "Mixer_ForumCard",
            "Mixer_UgcEditorialFeatureLinkPostCard",
            "Mixer_UgcEditorialFeatureTripCard",
            "Mixer_ReviewVerticalContributorCard",
            "Mixer_CustomVerticalMinimalCard",
            "Mixer_AttractionFlexCard",
            "Mixer_GeoVerticalNameWithButtonCard"
        ],
        "route": {
            "page": "AttractionsFusion",
            "params": {
            "geoId": geoId,
            "contentType": "attraction",
            "webVariant": "AttractionsFusion",
            "pagee": page
            }
        },
        "mapSurface": True,
        "debug": False,
        "polling": False
        },
        "extensions": {
        "preRegisteredQueryId": "b2c46e725df05768"
        }
    }
    ])

    response = requests.request("POST", url, headers=headers, data=payload)

    return response.json()

def get_all_attractions(geoId:int, page:int = 30):
    while True: 
        data = get_data(geoId, page)
        
        #product_count = data[-1]['data']['Result'][0]['additionalMapSections'][9]['totalResults']
        product_count = 120
        products = data[-1]['data']['Result'][0]['mapSections'][2]['cards']

        print(product_count, page)

        yield products
        if page >= product_count:
            break
        page += 30


# Save all obtained data into a JSON
def save_json(results):
    with open(f'TripAdvisor/Files/attractions.json','w') as jsonfile:
        json.dump(results, jsonfile, indent=4)

 
#results = []

#for products in get_all_attractions(cat_id, page = 30):
#    results.extend(products)


#results = get_data(cat_id, 30)
#save_json(results)
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser() 
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--destination_id', type=int, help='destination id')
    args = parser.parse_args()

    results = []

    for products in get_all_attractions(cat_id, page = 0):
        results.extend(products)
    #print(get_data(destination_id))
    save_json(results)
