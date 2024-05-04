from utils import argparser
from core import bypass
def result():
    args = argparser.get_arguments()
    req = argparser.get_request(args)
    result_list = [0,0,0,0,0]
    if args.token:
        result_list = bypass.try_bypass(args.url, req, args.token)
    else:
        result_list = bypass.try_bypass(args.url, req)

    if result_list[0] == 1:
        print("Captcha param None method is success.")
    if result_list[1] == 1:
        print("Captcha param Null method is success.")
    if result_list[2] == 1:
        print("Add Header method is success.")
    if result_list[3] == 1:
        print("POST->GET method is potentially success.")
    if result_list[4] == 1:
        print("POST->PUT method is potentially success.")
    if 1 not in result_list:
        print("Bypass isn't success")