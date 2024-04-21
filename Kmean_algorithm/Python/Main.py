from kmean import *

kmean = Kmean()

kmean.read_data("data.txt")
kmean.rendom_centroid(3)
for i in range(2):
    kmean.get_calculate_assign()
    kmean.update_centroid()
    kmean.display_cluster()
    kmean.update_cluster()   


    
