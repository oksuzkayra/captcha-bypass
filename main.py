from core import methods_json, methods_urlencoded
import argparse

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="URL")
    parser.add_argument("-u", "--url", help="URL", required=True)
    parser.add_argument("-r", "--request", help="Raw Request", required=True)
    args = parser.parse_args()

    url = args.url
    req = args.request

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



