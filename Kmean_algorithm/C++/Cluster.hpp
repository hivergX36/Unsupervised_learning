#include<vector> 
#include <iostream>
#include <string>
#include <fstream>
#include <cstdlib>
#include <math.h>  
#include <algorithm>


struct Cluster{
    
    int indexCluster;
    int numberBelongingPoint;
    std::vector<float> * belongingPoints; 

   


    Cluster(int numberClusterIndex, int numberFeature){
        indexCluster = numberClusterIndex;
        numberBelongingPoint = 0;
        belongingPoints = new std::vector<float>[numberFeature];
  

    }


    void computeFitessValue(std::vector<int>* Price, int Nb){
        float fitness1 = 0;
        float fitness2 = 0;
        for(int i = 0; i < Nb; i++){
            fitness1+= solution[0][i] * Price[0][i];
            fitness2+= solution[0][i] * Price[1][i];
            }
            
            FitnessValue1 = fitness1;
            FitnessValue2 = fitness2; 
            fitnessCalculated = true;
        


        }


    
    void displayIndividual(int NbVariable, int NbConstraints){

        std::cout << "La solution créée est: "; 
        for(int i = 0; i < NbVariable; i ++){

            std::cout << " " << solution[0][i];

        }

        std::cout << std::endl; 

        std::cout << "Les contraintes sont: "; 
        for (int j = 0; j < NbConstraints; j++){

            std::cout << " " << SumConstraint[0][j]; 

        }
        std::cout << std::endl;
    }


    


      float operator()(Solution ind1, Solution ind2) { return ind1.FitnessValue1 > ind2.FitnessValue1; } 












    ~Solution(){

    }


};



struct compareObjectives2:Solution {
      float operator()(Solution ind1, Solution ind2) { return ind1.FitnessValue2 > ind2.FitnessValue2; } 

}; 

struct RangeRankSolution:Solution {
    int operator()(Solution ind1, Solution ind2){ return ind1.rank < ind2.rank; }
};


struct RangeRankcrowdingMeasure:Solution {
    int operator()(Solution ind1, Solution ind2){ return ind1.crowdingdistance > ind2.crowdingdistance; }
};
