import numpy as np
data_type=[('Name','S15'),('Height',float),("Class",int)]
students_detail=[('bill',6.1,10),('jane',5.5,9),('mary',5.7,10),('mark',5.9,11)]
students=np.array(students_detail,dtype=data_type)
print("Original array:")
print(students)
print("Sort By Height")
print(np.sort(students,order='Height'))