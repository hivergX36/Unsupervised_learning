import re 
import random as rand
import math as mp


class Cluster_assignment:
    
    def __init__(self,index:int):
        cluster = index 
        centroid_coordinate = []
        belonging_vector = []
        indice_vector = []
        


class Kmean:
    
    def __init__(self):
        centroid = []
        predictor = []
        cluster= []
        nbgroup = 0  
        
   
    def checknumber(self,lignes,indice):
        ParsedList = []
        compteur1 = 0
        compteur2 = 0
        while(lignes[indice][compteur1] != "," and lignes[indice][compteur2] != ","):
              while(lignes[indice][compteur2] != ","):
                    compteur2 += 1
              print(lignes[indice][compteur1:compteur2])
              ParsedList.append(int(lignes[indice][compteur1:compteur2]))
              compteur1 = compteur2 + 1
              compteur2 = compteur1

   
              if compteur1 > len(lignes[indice]) - 1:
                    break
        return ParsedList
        
    def read_data(self,text):
        fichier = open(text, "r",encoding="utf8")
        lines = fichier.readlines()
        lines = [lines[i] for i in range(len(lines)) if lines[i] != "\n"]
        lines = [ re.sub("\n", "", lines[i]) for i in range(len(lines))]
        print("lines: ", lines)
        self.predictor = [self.checknumber(lines,k) for k in range(1,len(lines))]
        print("predictor: ", self.predictor)
        
    def rendom_centroid(self, nb_groups):
        self.nbgroup = nb_groups
        number_features = len(self.predictor)
        self.centroids = [[rand.random() for k in range(number_features)] for i in range(nb_groups)]
        self.cluster = [Cluster_assignment(k) for k in range(nb_groups)]
        for(k) in range(nb_groups):
            self.cluster[k].centroid_coordinate = self.centroids[k]
        
    
    def run_kmeans(self, nb_groups, MAX_ITERATION):
        number_iteration = 0 
        self.random_centroid(nb_groups)
        
    def get_calculate_assign(self):
        min_index = 0 
        min_dist = 0 
        predictor_group_vector = [[] for i in range(self.nbgroup)]
        predictor_group_index = [[] for i in range(self.nbgroup)]
        number_features = len(self.predictor)
        for k in range(number_features):
            distance = [0 for j in range(self.nbgroup)]
            for j in range(self.nbgroup): 
                distance[j] = sum([self.predictor[k][i] - self.centroids[j][i] for i in range(len(self.predictor[k]))])
                distance[j] = mp.sqrt(distance[j])
                print("feature: ", k , " centroid: ", j  ," distance: " , distance[j])
            min_dist = min(distance)
            min_index = distance.index(min_dist)
            predictor_group_vector[min_index].append(self.predictor[k])
            predictor_group_index[min_index].append(k)
        print(predictor_group_vector)
        print(predictor_group_index)
        for i in range(self.nbgroup):
            self.cluster[i].belonging_vector = predictor_group_vector[i]
            self.cluster[i].indice_vector = predictor_group_index[i]
            
            
    def update_cluster(self):
        a = 10 
            
            
        
        
        
        
        
        
        
    
