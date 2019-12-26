import numpy

A = numpy.array([[1,2,3,-2,-1],[3,5,5,-3,-9],[2,3,2,0,-8],[2,6,7,-5,1],[1,2,6,-4,-10]])#lewa strona równania
B = numpy.array([6,2,-5,17,12])#prawa strona równania
X = numpy.linalg.solve(A,B)#rozwiązanie układu równań
print("x:"+ str(X[0]) + "\ny:"+ str(X[1]) + "\nz:"+ str(X[2]) + "\nt:"+ str(X[3]) + "\nu:"+ str(X[4]))