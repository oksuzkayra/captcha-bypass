import re
from utils.parser import params_to_json, list_to_dict

captcha_parameters = [
    "captcha",
    "recaptcha",
    "g-recaptcha-response",
    "captcha_response",
    "security_code",
    "verification_code",
    "human_verification",
    "challenge_response",
    "user_captcha",
    "form_captcha",
    "verification_token",
    "auth_captcha",
    "captcha_input",
    "captcha_text",
    "validation_code",
    "anti_spam_token",
    "bot_protection",
    "image_verification",
    "challenge_answer"
]

def find_token_json(req: str):
    # JSON parametreleri arasından içerisinde 'captcha' kelimesi geçen token'i döndürür.
    for key, value in params_to_json(req).items():
        for captcha_param in captcha_parameters:
            if re.search(captcha_param, key, re.IGNORECASE):
                return key
        if isinstance(value, dict):
            for nested_key in value.keys():
                for captcha_param in captcha_parameters:
                    if re.search(captcha_param, nested_key, re.IGNORECASE):
                        return nested_key

def find_token(req: str):
    # Parametreler arasından içerisinde 'captcha' kelimesi geçen token'i döndürür.
    for key in list_to_dict(req).keys():
        for captcha_param in captcha_parameters:
            if re.search(captcha_param, key, re.IGNORECASE):
                return key