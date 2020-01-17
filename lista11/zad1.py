import urllib.request
strona = "https://docs.python.org/3/library/urllib.request.html"
try:    
    print("Strona została znaleziona",urllib.request.urlopen(strona))
except:
    print(strona + "  Error 404 - Strona nie została odnaleziona :(")