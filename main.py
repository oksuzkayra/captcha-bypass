from core import bypass
import argparse

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="URL")
    parser.add_argument("-u", "--url", help="URL", required=True)
    parser.add_argument("-r", "--request", help="Raw Request", required=True)
    args = parser.parse_args()

    url = args.url

    if args.request:
        # Dosyayı aç ve içeriğini oku
        try:
            with open(args.request, 'r') as dosya:
                req = dosya.read()
        except FileNotFoundError:
            print("Error: HTTP Request file not found!")
    else:
        print("Error: -r argument not found!")

    bypass.try_bypass(url,req)



