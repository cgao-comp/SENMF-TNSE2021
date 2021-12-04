import numpy as np


def getLabelMatrix(data_file):
    l = np.loadtxt(data_file)
    l_int = np.asarray(l, dtype=int, order=None)
    c = l_int.shape
    node_num = c[0]
    origin_cluster = np.empty(node_num, dtype=int)
    for i in range(0, node_num):
        origin_cluster[i] = l_int[i][1]
    return origin_cluster
    return l_int

def getAdjacencyMatrix(edges_matrix):
    edges_matrix = np.asarray(edges_matrix,dtype=int)
    row_num = edges_matrix.shape[0]
    colum_num = edges_matrix.shape[1]
    adjacencyMatrix = np.zeros((edges_matrix.max()+1,edges_matrix.max()+1),dtype=int)
    for i in range(row_num):
        adjacencyMatrix[edges_matrix[i][0]][edges_matrix[i][1]] = 1
        adjacencyMatrix[edges_matrix[i][1]][edges_matrix[i][0]] = 1
    return adjacencyMatrix


