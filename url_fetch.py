import urllib.request
with urllib.request.urlopen("http://google.com") as response:
    html=response.read()
    info=response.info()
    url=response.geturl()
    print(html)
    print("\nThis is info\n%s" % info)
    print("\nThis is real url\n%s" % url)
#geturl()
#info()

