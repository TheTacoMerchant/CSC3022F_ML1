import math

def distance(point, centroid):
    val = (point[0]-centroid[0])**2 + (point[1] - centroid[1])**2
    return math.sqrt(val)



differentCentroids = True
itt = 0

data = [(1, 2, 10),
(2, 2, 5),
(3, 8, 4),
(4, 5, 8),
(5, 7, 5),
(6, 6, 4),
(7, 1, 2),
(8, 4, 9)]

cluster1 = []
cluster2 = []
cluster3 = []

cent1 = (2,10)
cent2 = (5,8)
cent3 = (1,2)
while differentCentroids:
    itt += 1
    for datum in data:
        if distance((datum[1], datum[2]), cent1) == min(distance((datum[1], datum[2]), cent1),distance((datum[1], datum[2]), cent2),distance((datum[1], datum[2]), cent3)):
            cluster1.append(datum)
        elif distance((datum[1], datum[2]), cent2) == min(distance((datum[1], datum[2]), cent1),distance((datum[1], datum[2]), cent2),distance((datum[1], datum[2]), cent3)):
            cluster2.append(datum)
        else:
            cluster3.append(datum)

    with open('outfile.txt', 'a') as outfile:
        outfile.write(f"Iteration {itt}\n\n")
        points1 = ""
        for point in cluster1:
            points1 += f" {point[0]}"
        outfile.write("Cluster 1:" + points1 + "\n")
        outfile.write(f"Centroid: ({cent1[0]},{cent1[1]})\n\n")

        points2 = ""
        for point in cluster2:
            points2 += f" {point[0]}"
        outfile.write("Cluster 2:" + points2+ "\n")
        outfile.write(f"Centroid: ({cent2[0]},{cent2[1]})\n\n")

        points3 = ""
        for point in cluster3:
            points3 += f" {point[0]}"
        outfile.write("Cluster 3:" + points3+ "\n")
        outfile.write(f"Centroid: ({cent3[0]},{cent3[1]})\n\n")
        

    x1sum = 0
    y1sum = 0
    for datum in cluster1:
        x1sum += datum[1]
        y1sum += datum[2]
    newcent1 = (x1sum/len(cluster1), (y1sum/len(cluster1)))
    cluster1.clear()

    x2sum = 0
    y2sum = 0
    for datum in cluster2:
        x2sum += datum[1]
        y2sum += datum[2]
    newcent2 = (x2sum/len(cluster2), (y2sum/len(cluster2)))
    cluster2.clear()

    x3sum = 0
    y3sum = 0
    for datum in cluster3:
        x3sum += datum[1]
        y3sum += datum[2]
    newcent3 = (x3sum/len(cluster3), (y3sum/len(cluster3)))
    cluster3.clear()

    if (newcent1 == cent1 and newcent2 == cent2 and newcent3 == cent3):
        differentCentroids = False
    
    cent1 = newcent1
    cent2 = newcent2
    cent3 = newcent3
    


