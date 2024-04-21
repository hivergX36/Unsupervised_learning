import re 
import random as rand
import math as mp


class Cluster_assignment:
    
    def __init__(self,index:int):
        cluster = index 
        centroid_coordinate = []
        belonging_vector = []
        indice_vector = []
        number_cluster = 0 
        


class Kmean:
    
    def __init__(self):
        
        data_inertia = []
        centroid = []
        predictor = []
        cluster = []
        feature_size = 0 
        nbgroup = 0
        inertia = 0

        
    
 
        
   
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
        self.data_inertia = [0]

        
    def rendom_centroid(self, nb_groups):
        self.nbgroup = nb_groups
        self.feature_size = len(self.predictor[0])
        self.centroids = [[rand.randint(900,1000) for k in range(self.feature_size)] for i in range(nb_groups)]
        self.cluster = [Cluster_assignment(k) for k in range(nb_groups)]
        for(k) in range(nb_groups):
            self.cluster[k].centroid_coordinate = self.centroids[k]
            print("centroid_: ",  self.cluster[k].centroid_coordinate )
        
    
    def run_kmeans(self, nb_groups, MAX_ITERATION):
        number_iteration = 0 
        self.random_centroid(nb_groups)
        self.get_calculate_assign()
        self.update_cluster()
        
    def get_calculate_assign(self):
        min_index = 0 
        min_dist = 0 
        predictor_group_vector = [[] for i in range(self.nbgroup)]
        predictor_group_index = [[] for i in range(self.nbgroup)]
        for k in range(self.feature_size):
            distance = [0 for j in range(self.nbgroup)]
            for j in range(self.nbgroup): 
                distance[j] = sum([(self.predictor[k][i] - self.centroids[j][i])**2 for i in range(len(self.predictor[k]))])
                distance[j] = mp.sqrt(distance[j])
            min_dist = min(distance)
            min_index = distance.index(min_dist)
            predictor_group_vector[min_index].append(self.predictor[k])
            predictor_group_index[min_index].append(k)
     
        for i in range(self.nbgroup):
            self.cluster[i].belonging_vector = predictor_group_vector[i]
            self.cluster[i].indice_vector = predictor_group_index[i]
            
            
    def update_centroid(self):
        for i in range(self.nbgroup):
            vector = [0 for compteur in range(self.feature_size)]
            for k in range(len(self.cluster[i].belonging_vector)):
                for l in range(self.feature_size):
                    vector[l] += self.cluster[i].belonging_vector[k][l]
            if len(self.cluster[i].belonging_vector) > 0:
                self.cluster[i].centroid_coordinate = [vector[j] / len(self.cluster[i].belonging_vector) for j in range(self.feature_size)]
            
            
    def update_cluster(self):
        for i in range(self.nbgroup):
            self.cluster[i].belonging_vector = []
            self.cluster[i].indice_vector = []
            
            
    def display_cluster(self):
        for i in range(self.nbgroup):
            print("cluster_centroid: ", self.cluster[i].centroid_coordinate)
            print("cluster_vectors: ", self.cluster[i].belonging_vector)
            
            
    def calculate_inertia(self):
        self.inertia = 0 
        for i in range(self.nbgroup):
            distance = [0 for j in range(len(self.cluster[i].belonging_vector))]
            for k in range(len(self.cluster[i].belonging_vector)):
                distance[k] = sum([(self.cluster[i].belonging_vector[k][j] - self.cluster[i].centroid_coordinate[j])**2 for j in range(self.feature_size)])
                distance[k] = mp.sqrt(distance[k])
            self.inertia += sum(distance)
        print("La variance intrasèque est: ", self.inertia)
        self.data_inertia.append(self.inertia)

      
        print("inertia_sequence: ", self.data_inertia)
            
            
            
            
        

            
   

        
        
        
        
        
        
    
