import numpy as np
import pandas as pd
from sklearn.metrics import pairwise
import equievance
from getSimilarMatrix import getSimilariy, getSimilariy_2
from loadData import getAdjacencyMatrix
from calculation_helper import graph_reader



def getFinal_Matrix(mu,gamma,k,input_path,orbitFile_path,eta,theta,omega):
       """
       Function to get a hybrid matrix (final input matrix).
       :param mu: Weight of currency adjacency matrix.
       :param gamma: Weight of currency community structure.
       :param k: the number of cluster that implement in spectral clustering.
       :param spectralMatrix: result by spectral cluster on original matrix, which formed as n*k, k denote the number of community(by module of spectralClustertest).
       :param edgelist_path: original input edgelist path.
       :param orbitFile_path: orbit file path.
       :param eta: Weight of second proximity  matrix.
       :param theta: Weight of equivalence matrix.

       :return final_A: final input matrix.
       """

       edges = pd.read_csv(input_path)
       G = graph_reader(input_path)
       adj_matrix = getAdjacencyMatrix(edges)
       print("begin to calculate similarities!")
       similar_matrix = getSimilariy_2(adj_matrix)
       print("The calculation of similarities finished!")
       stru_A = adj_matrix + omega*similar_matrix
       second_proximity_matrix = pairwise.cosine_similarity(stru_A)
       print("the seconde is {}".format(np.mat(second_proximity_matrix).shape))
       equivalence_matrix = equievance.getLs(orbitFile_path)
       final_S = stru_A + eta * second_proximity_matrix + theta * equivalence_matrix
       return final_S

def delSelfConnect(matrix):
    """
    function to delete self connected
    :param matrix: n*n matrix
    :return: n*n matrix where matrix[i][i] = 0
    """

    matrix = np.asarray(matrix, dtype=int)
    num = matrix.shape[0]
    matrix = list(matrix)
    for i in range(num):
        matrix[i][i] = 0
    return matrix

