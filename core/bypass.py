from core import methods_json, methods_urlencoded

def try_bypass(url: str, req: str):
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
