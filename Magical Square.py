import numpy as np

A=[[0,1,1,0,0,0,0,0,0,-1],
   [0,0,0,1,1,0,0,0,0,-1],
   [0,0,0,0,0,0,1,1,0,-1],
   [0,0,0,1,0,0,1,0,0,-1],
   [0,1,0,0,1,0,0,1,0,-1],
   [0,0,1,0,0,0,0,0,0,-1],
   [0,0,0,0,1,0,0,0,0,-1],
   [0,0,1,0,1,0,1,0,0,-1],
   [0,0,0,0,3,0,0,0,0,-1]]

C=[-5,-4,-6,-5,0,-10,-11,0,0]

ans=np.dot(np.linalg.pinv(A),C)
print(ans)

# for rij in A:
#     while np.count_nonzero(rij)>2:
#         found_rij=False
#         setter = 0
#         index=0
#         matrix=[]
#         for element in rij:
#             if setter == 1:
#                 if element!=0:
#                     for rij2 in A:
#                         if rij2[index]!=0 and not np.array_equal(rij,rij2):
#                                 matrix=rij2
#                                 factor=element/rij2[index]
#                                 rij=np.subtract(rij,np.multiply(factor,matrix))
#                                 found_rij=True
#                                 break
#                     if found_rij:
#                         found_rij=False
#                         break
#             if element == 1:
#                 setter = 1
#             index += 1
#     print(rij)
#
#
