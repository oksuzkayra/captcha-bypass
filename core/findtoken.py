import re
from utils.parser import params_to_json, list_to_dict

def find_token_json(req: str):
    # JSON parametreleri arasından içerisinde 'captcha' kelimesi geçen token'i döndürür.
    for key, value in params_to_json(req).items():
        if re.search('captcha', key, re.IGNORECASE):
            return key
        if isinstance(value, dict):
            for nested_key in value.keys():
                if re.search('captcha', nested_key, re.IGNORECASE):
                    return nested_key

def find_token_form_urlencoded(req: str):
    # Parametreler arasından içerisinde 'captcha' kelimesi geçen token'i döndürür.
    for key in list_to_dict(req).keys():
        if re.search('captcha', key, re.IGNORECASE):
            return key