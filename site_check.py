## check the body and the header of the site - similar to curl
import sys
import urllib.request
from pprint import pprint
import json

def main():
    if not len(sys.argv) == 2:
        print("You need to provide HTTP address in CMD line")
        print(f"Example:\n {sys.argv[0]} http://example.com")
        sys.exit()

    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            html=response.read()
            head=response.headers
            url=response.url
            code=response.code
        print(html.decode('utf-8'))
        print("\nThis is HEADER\n%s" % head)
        print("\nThis is real URL\n%s" % url)
        print(code)
    
    except Exception as e:
        print('URL error,',e)
        print('Probably site does not exist.')
if __name__ == '__main__':
    main()
