from core import methods_json, methods_urlencoded, methods_get

def _get_request_method(req: str) -> str:
    """Request-line'den HTTP metodunu güvenli şekilde çıkarır."""
    if not req:
        return ""
    lines = req.splitlines()
    if not lines:
        return ""
    first = lines[0].strip()
    if not first:
        return ""
    parts = first.split()
    if not parts:
        return ""
    return parts[0].upper()

def _get_content_type(req: str) -> str:
    """Req içinde Content-Type header'ını case-insensitive şekilde bulur."""
    if not req:
        return ""
    for line in req.splitlines():
        if ":" not in line:
            continue
        name, val = line.split(":", 1)
        if name.strip().lower() == "content-type":
            return val.strip().lower()
    return ""

def try_bypass(url: str, req: str, token = None):
    bypass_list = [0,0,0,0,0]

    method = _get_request_method(req)
    content_type = _get_content_type(req)

    if method == "GET":
        if "?" in url:
            try:
                url = url.split("?", 1)[0]
            except Exception:
                pass

        try: bypass_list[0] = methods_get.bypass_method_1_get(url, req, token)
        except: pass
        try: bypass_list[1] = methods_get.bypass_method_2_get(url, req, token)
        except: pass
        try: bypass_list[2] = methods_get.bypass_method_3_get(url, req, token)
        except: pass
        try: bypass_list[3] = methods_get.bypass_method_4_post(url, req, token)
        except: pass
        try: bypass_list[4] = methods_get.bypass_method_4_put(url, req, token)
        except: pass

    elif "application/json" in content_type:
        try: bypass_list[0] = methods_json.bypass_method_1_json(url, req, token)
        except: pass
        try: bypass_list[1] = methods_json.bypass_method_2_json(url, req, token)
        except: pass
        try: bypass_list[2] = methods_json.bypass_method_3_json(url, req, token)
        except: pass
        try: bypass_list[3] = methods_json.bypass_method_4_json_get(url, req, token)
        except: pass
        try: bypass_list[4] = methods_json.bypass_method_4_json_put(url, req, token)
        except: pass

    elif "application/x-www-form-urlencoded" in content_type:
        try: bypass_list[0] = methods_urlencoded.bypass_method_1_urlencoded(url, req, token)
        except: pass
        try: bypass_list[1] = methods_urlencoded.bypass_method_2_urlencoded(url, req, token)
        except: pass
        try: bypass_list[2] = methods_urlencoded.bypass_method_3_urlencoded(url, req, token)
        except: pass
        try: bypass_list[3] = methods_urlencoded.bypass_method_4_urlencoded_get(url, req, token)
        except: pass
        try: bypass_list[4] = methods_urlencoded.bypass_method_4_urlencoded_put(url, req, token)
        except: pass

    return bypass_list