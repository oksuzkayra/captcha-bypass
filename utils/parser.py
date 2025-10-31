import json
from json.decoder import JSONDecodeError

params_dict = {}
def parse_req_headers(req: str):
    # Request headerlarını dictionary olarak döndürür.
    temp = req.split("\n")
    temp = temp[2:len(temp) - 3]
    final_dict = {}
    for i in temp:
        index = i.find(":")
        final_dict[i[:index]] = i[index+2:]
    # Content-Length Header'ını siler.
    if "Content-Length" in final_dict.keys():
        del final_dict["Content-Length"]
    return final_dict
def req_body_to_list(req: str):
    # Request body'i liste olarak döndürür.
    params_all = req[req.find("\n\n")+2:]
    params_list = params_all.split("&")
    return params_list
def req_body_to_list_for_get(req: str):
    # Parametreleri liste olarak döndürür.
    params_all = req[req.find("GET")+4:req.find("HTTP")-1]
    params_list = params_all.split("?")
    if len(params_list) > 1:
        params_list = params_list[1].split("&")
    else:
        params_list = []
    return params_list
def req_body_to_list_chooser(req: str):
    # Request body'i liste olarak döndürür.
    if "GET" in req[0:req.find("\n")]:
        return req_body_to_list_for_get(req)
    else:
        return req_body_to_list(req)
def list_to_dict(req: str):
    # Listeyi dict'e çevirerek döndürür.
    for i in req_body_to_list_chooser(req):
        locations=i.find("=")
        params_dict[i[:locations]] = i[locations+1:]
    return params_dict
def params_to_json(req: str):
    # Request body'i JSON formatına dönüştürür.
    try:
        params_all = req[req.find("\n\n") + 2:]
        params_dict = json.loads(params_all)
        return params_dict
    except JSONDecodeError as e:
        print("JSON Decode Error: ", e)