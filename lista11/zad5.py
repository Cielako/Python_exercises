import re
tekst = 'LubieUczyć się CałkiemNowych rzeczy'
spacja =  re.sub(r"(\w)([A-Z])", r"\1 \2", tekst)
print(spacja)