import numpy as np
import math
from scipy import linalg

new_array = np.array([[4,5,6],[7,8,9],[2,5,8]])
determinant = linalg.det(new_array)
inverse = linalg.inv(new_array)
#c = new_array @ inverse
#c = np.multiply(determinant,inverse)
#c = new_array.dot(inverse)
c = new_array * inverse
print(new_array)
print("                            ")
print(determinant)
print("                            ")
print(inverse)
print("                            ")
print(c)
