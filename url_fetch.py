import urllib.request
from pprint import pprint
with urllib.request.urlopen("http://mercury.picoctf.net:47967") as response:
    html=response.read()
    ## geturl - when directed and header info
    info=response.info()
    url=response.geturl()
    pprint(html)
    print("\nThis is info\n%s" % info)
    print("\nThis is real url\n%s" % url)
#    meto=dir(urllib.request.HTTPCookieProcessor.response("https://exmaple.com"))
#    for each in meto:
#       print(f"\n{each}")
