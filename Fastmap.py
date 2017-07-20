import numpy as np
import matplotlib.pyplot as plt
datanup = np.loadtxt("fastmap-data.txt",dtype=float)
def fastmap(datanup,k,points):
    if k <= 0 :
        return
    new_datanup = datanup[(-datanup[:, 2]).argsort()]
    row_list = []
    point_x1 = []
    datanup_copy = datanup.copy()
    newdis_list = []
    n = int(np.max(datanup[:,0:2]))
# sort distance
    for row in new_datanup:
        if row[2] == np.max(datanup, axis=0)[2]:
            row_list.append(row)
    row_matrix = np.array(row_list)
# sort point_index
    row_matrix = row_matrix[np.lexsort((row_matrix[:, 0], row_matrix[:, 1]))]
    point1 = row_matrix[0,0]
    point2 = row_matrix[0,1]
    distance = row_matrix[0,2]
# calcuate the index of point
    for i in range(1,n+1):
        if i == point1:
            distance1 = 0
            distance2 = distance
        elif i == point2:
            distance1 = distance
            distance2 = 0
        elif i < point1:
            point = datanup[np.where((datanup[:, 0] == i) & (datanup[:, 1] == point1))]
            point_ = datanup[np.where((datanup[:, 0] == i) & (datanup[:, 1] == point2))]
            distance1 = point[:,2].item()
            distance2 = point_[:,2].item()
        elif i > point1 and i < point2:
            point = datanup[np.where((datanup[:, 0] == point1) & (datanup[:, 1] == i))]
            point_ = datanup[np.where((datanup[:, 0] == i) & (datanup[:, 1] == point2))]
            distance1 = point[:, 2].item()
            distance2 = point_[:, 2].item()
        elif i > point2:
            point = datanup[np.where((datanup[:, 0] == point1) & (datanup[:, 1] == i))]
            point_ = datanup[np.where((datanup[:, 0] == point2) & (datanup[:, 1] == i))]
            distance1 = point[:, 2].item()
            distance2 = point_[:, 2].item()
        value_point = (distance1**2 + distance**2 - distance2**2)/(2*distance)
        point_x1.append(value_point)
    points.append(point_x1)
# dimensional reduction
    for i in range(1,n): # index 1 to n-1
        for j in range(i+1,n+1): # index i+1 to n
            pointt = datanup[np.where((datanup[:, 0] == i) & (datanup[:, 1] == j))]
            old_distance = pointt[:,2].item()
            new_distance = (old_distance**2 - (point_x1[i-1]-point_x1[j-1])**2)**0.5 # list index 0 to n-1
            newdis_list.append(new_distance)
    datanup_copy[:,2] = newdis_list
# recursion
    fastmap(datanup_copy, k-1,points)
points=[]
fastmap(datanup,2,points)
fig, ax = plt.subplots()
ax.scatter(points[0], points[1])
f = open("fastmap-wordlist.txt")
words = f.read().splitlines()
f.close()
for i, txt in enumerate(words):
    ax.annotate(txt, (points[0][i],points[1][i]))
