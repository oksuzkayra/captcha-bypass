import requests as r
from utils.parser import parse_req_headers, list_to_dict
from core.findtoken import find_token_form_urlencoded

def bypass_method_1_urlencoded(url: str, req: str, token = None):
    # Content-Type'ı urlencoded olan isteklerde captcha parametresini göndermeyerek bypass etmeye çalışır.
    headers = parse_req_headers(req)
    if token == None:
        token = find_token_form_urlencoded(req)
    form_data = list_to_dict(req)
    response = r.post(url, form_data, headers)
    print("Trying method 1..")
    try:
        for key in form_data:
            if key == token:
                del form_data[key]
                break

        new_response = r.post(url, form_data, headers)
        if "40" not in str(response.status_code) and "50" not in str(response.status_code) and response.status_code == new_response.status_code:
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
def bypass_method_2_urlencoded(url: str, req: str, token = None):
    # Content-Type'ı urlencoded olan isteklerde captcha parametresini boş göndererek bypass etmeye çalışır.
    headers = parse_req_headers(req)
    if token == None:
        token = find_token_form_urlencoded(req)
    form_data = list_to_dict(req)
    response = r.post(url, form_data, headers)
    print("Trying method 2..")
    try:
        for key in form_data:
            if key == token:
                form_data[key] = ""
                break

        new_response = r.post(url, form_data, headers)
        if "40" not in str(response.status_code) and "50" not in str(response.status_code) and response.status_code == new_response.status_code:
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
def bypass_method_3_urlencoded(url: str, req: str, token = None):
    # Content-Type'ı urlencoded olan isteklerde Headerlar kullanılarak bypass etmeye çalışır.
    headers = parse_req_headers(req)
    if token == None:
        token = find_token_form_urlencoded(req)
    form_data = list_to_dict(req)
    response = r.post(url, form_data, headers)

    headers["X-Forwarded-Host"] = "127.0.0.1"
    headers["X-Forwarded-For"] = "127.0.0.1"
    headers["X-Originating-IP"] = "127.0.0.1"
    headers["X-Remote-IP"] = "127.0.0.1"
    headers["X-Remote-Addr"] = "127.0.0.1"
    headers["X-Client-IP"] = "127.0.0.1"
    headers["X-Host"] = "127.0.0.1"

    print("Trying method 3..")
    try:
        new_response = r.post(url, form_data, headers)
        if "40" not in str(response.status_code) and "50" not in str(response.status_code) and response.status_code == new_response.status_code:
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
def bypass_method_4_urlencoded_get(url: str, req: str, token = None):
    # Content-Type'ı urlencoded olan isteklerde POST -> GET ile bypass etmeye çalışır.
    headers = parse_req_headers(req)
    if token == None:
        token = find_token_form_urlencoded(req)
    form_data = list_to_dict(req)
    response = r.post(url, form_data, headers)
    del headers["Content-Type"]

    print("Trying method 4.1..")
    try:
        new_response = r.get(url, params=form_data, headers=headers)
        if "40" not in str(response.status_code) and "50" not in str(response.status_code) and response.status_code == new_response.status_code:
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
def bypass_method_4_urlencoded_put(url: str, req: str, token = None):
    # Content-Type'ı urlencoded olan isteklerde POST -> PUT ile bypass etmeye çalışır.
    headers = parse_req_headers(req)
    if token == None:
        token = find_token_form_urlencoded(req)
    form_data = list_to_dict(req)
    response = r.post(url, form_data, headers)

    print("Trying method 4.2..")
    try:
        new_response = r.put(url, data=form_data, headers=headers)
        if "40" not in str(response.status_code) and "50" not in str(response.status_code) and response.status_code == new_response.status_code:
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