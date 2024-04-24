from core import bypass
from utils import argparser
import argparse

if __name__ == '__main__':

    args = argparser.get_arguments()
    req = argparser.get_request(args)
    if args.token:
        bypass.try_bypass(args.url, req, args.token)
    else:
        bypass.try_bypass(args.url, req)