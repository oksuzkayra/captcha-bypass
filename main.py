from core import methods_json, methods_urlencoded

req = """
POST /Form HTTP/1.1
X-Bug-Bounty: BugCrowd-oksuzkayra
Host: prod-api.devhub.worldpay.io
Connection: keep-alive
sec-ch-ua: "Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"
Accept: application/json, text/plain, */*
Content-Type: application/json
sec-ch-ua-mobile: ?0
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36
x-api-key: 0C8S6IBsnj8WQ3clQLwdf8iZvi4HDDVE9uXirdEe
sec-ch-ua-platform: "macOS"
Origin: https://developer.worldpay.com
Sec-Fetch-Site: cross-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://developer.worldpay.com/
Accept-Encoding: gzip, deflate, br, zstd
Accept-Language: tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7
Content-Length: 843

{"form_id":"feedback","data":{"email":null,"type":"Providing feedback","comment":"asdasdasd","location":null,"reCaptchaResponse":"03AFcWeA64omUlhteE6WHFuceIzdPcCkizhr4Nxkyfq71SD5oDuZDWLxfXTZByrVokv2Z5b2KB-nS6qxuj0nb29R90Eiif4gphVfve_S4pVt672uDP4HFCFUZSJYJCqKjYk-8RD2xxbLwBJX6o3uU91_DAz6a5eykEAYABKUDsPuOYMQaMQWE27Hch2fZ3B2TiCPazmgG4-UtPSOizVflbkPDItcQLV1rcUdpPg5-vuQHVGGpOg_nE2fOXUrZMGiPsMww1aMghRqglJYeduUKhKVRl0hFD1XkWSTJv8sogRa0sBaqn1axYdllybMKpLzM2mor4ylHHvgGflEbddC7zJPxR99DmJjstM4kud2Kb6DGVCZsPCJAGS3BONPm5mJ0u1YGj0ep400wUq9rC47f3vtz5_UwJzsLLcsw8690CM4iYWiXXrwTsPQuZuL54R3y5M1lxhSQ4QA5gzjf5SXvKhsQU6aQeCiBK86pwPDLy4Z4-7gsKJNg1F4YXRkYw5D9tQNngPkNGxFFwqkaPwum0h9lhEiYd4ZL3HjlwCkvWpfQuELCiCT7rIOvtEWSC5DpxLcxXWfF-giCor1-hxOFPLbnsKfPncnjszK_vXZPcpNDISXu8Enmz2ZooF_WyBIcmoDOEN3h66Ls4suf7x1DeRSRcMZxYMD_VDQB7Y5TsXXmdP4T5QlT2qN0"},"context":""}
"""

if __name__ == '__main__':

    url = "https://prod-api.devhub.worldpay.io/Form"

    if "Content-Type: application/json" in req:
        print(methods_json.bypass_method_1_json(url, req))
        print(methods_json.bypass_method_2_json(url, req))
        print(methods_json.bypass_method_3_json(url, req))
        print(methods_json.bypass_method_4_json_get(url, req))
        print(methods_json.bypass_method_4_json_put(url, req))

    elif "Content-Type: application/x-www-form-urlencoded" in req:
        print(methods_urlencoded.bypass_method_1_urlencoded(url, req))
        print(methods_urlencoded.bypass_method_2_urlencoded(url, req))
        print(methods_urlencoded.bypass_method_3_urlencoded(url, req))
        print(methods_urlencoded.bypass_method_4_urlencoded_get(url, req))
        print(methods_urlencoded.bypass_method_4_urlencoded_put(url, req))



