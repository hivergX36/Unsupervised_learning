from kmean import *

kmean = Kmean()

kmean.read_data("data.txt")
kmean.rendom_centroid(3)
for i in range(15):
    kmean.get_calculate_assign()
    kmean.update_centroid()
    kmean.display_cluster()
    kmean.calculate_inertia()
    kmean.update_cluster()
    
