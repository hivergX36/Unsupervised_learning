from kmean import *

kmean = Kmean()

kmean.read_data("data.txt")
kmean.rendom_centroid(3)
kmean.get_calculate_assign()
