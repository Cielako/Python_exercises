import re
tekst = 'Już niedługo sesja ametystowy ametyst nowy semestr'
slowa = re.findall(r'\b[an]\w+', tekst)
print(slowa)