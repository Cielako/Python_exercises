num = int(input("Podaj liczbę z zakresu (1-1999): "))
while num > 1999 or num <= 0:
        print("Podana liczba jest nieprawidłowa, spróbuj ponownie !!!")
        num = int(input("Podaj liczbę z zakresu (1-1999): "))
def num2words(num):
	ponizej_20 = ['','zero','jeden','dwa','trzy','cztery','pięć','sześć','siedem','osiem','dziewięć','dziesięć','jedenaśćie','dwanaście','trzynaście','czternaście','piętnaście','szesnaście','siedemnaście','osiemnaście','dziewietnaście']
	dziesiatki = ['dwadzieścia','trzydzieści','czterdzieśći','pięćdziesiąt','sześćdziesiąt','siedemdziesiąt','osiemdziesiąt','dziewięćdziesiąt']
	powyzej_100 = {100: 'sto',200: 'dwieście',300: 'trzysta',400: 'Czterysta',500: 'pięćset',600: 'sześćset',700: 'siedemset',800: 'osiemset',900: 'dziewięćset',1000:'Tysiąc',}

	if num < 20:
		 return ponizej_20[num+1]
	
	if num < 100:
		return dziesiatki[(int)(num/10)-2] + ('' if num%10==0 else ' ' + ponizej_20[num%10+1])

	# element przestawny
	element = max([key for key in powyzej_100.keys() if key <= num])

	return num2words(int(-1)) + '' + powyzej_100[element] + ('' if num%element==0 else ' ' + num2words(num%element))
print(num2words(num))