import argparse

def get_arguments():
    parser = argparse.ArgumentParser(description="URL")
    parser.add_argument("-u", "--url", help="URL", required=True)
    parser.add_argument("-r", "--request", help="Raw Request txt format", required=True)
    parser.add_argument("-t", "--token", help="Captcha Token param", required=False)
    parser.add_argument("-e", "--error", help="Captcha error string", required=False)


    args = parser.parse_args()
    return args

def get_request(args: dict):
    if args.request:
        # Dosyayı aç ve içeriğini oku
        try:
            with open(args.request, 'r') as dosya:
                req = dosya.read()
                return req
        except FileNotFoundError:
            print("Error: HTTP Request file not found!")
    else:
        print("Error: -r argument not found!")