import string
alfabet = set(string.ascii_lowercase)#pozwala wczytać alfabet ascii do zmiennej alfabet

def czyPangram(string):
    return set(string.lower()) >= alfabet #sprawdzenie czy cały string zawiera choć po 1 literce z całego alfabetu

string = "The quick brown fox jumps over the lazy dog. False, I see false, this exam I may pass"

if(czyPangram(string) == True):
    print("yes")
else:
    print("no")

