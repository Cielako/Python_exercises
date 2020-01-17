import re

tekst = '<a href="http://example.com"><a href="http://example2.com">https://google.com a  https://youtube.com bardzo fajna strona http://filmixy.io'
linki = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', tekst)
print("Oto otrzymane linki: ",linki)