import numpy
import matplotlib.pyplot as plt
jezyki = ["Java", "C", "Python", "C++", "C#", "Visual Basic .NET", "JavaScript", "PHP","SQL", "Swift"]
procentowy_udzial = [17.253, 16.086, 10.309, 6.196, 4.801, 4.743, 2.090, 2.048, 1.843, 1.490]

indeks = numpy.arange(len(jezyki))
plt.bar(indeks,procentowy_udzial, color="orange")
plt.xlabel("Język")
plt.ylabel("%")
plt.xticks(indeks,jezyki, fontsize = 6, rotation = -40)
plt.title('Popularność języków programowania')
plt.show()
