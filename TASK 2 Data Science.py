import numpy as np 

A = np.array([[1, 2, 3], [0, 1, 2], [2, 0, 0]])
B = [[1], [1], [0]]
detA = A[0][0]*A[1][1]*A[2][2]+A[0][1]*A[1][2]*A[2][0]+A[1][0]*A[2][1]*A[0][2]-A[0][2]*A[1][1]*A[2][0]-A[0][0]*A[1][2]*A[2][1]-A[0][1]*A[1][0]*A[2][2]
print (detA)
print (numpy.linalg.det(A))