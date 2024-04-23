from kmean import *
from matplotlib import pyplot as plt



kmean = Kmean()

kmean.read_data("data.txt")
kmean.rendom_centroid(3)
print(kmean.predictor)
print(kmean.feature_size)
for i in range(3):
    kmean.get_calculate_assign()
    kmean.update_centroid()
    kmean.display_cluster()





    
