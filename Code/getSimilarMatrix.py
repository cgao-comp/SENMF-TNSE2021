import numpy as np
import networkx as nx

def getOneZeroMatrix(matrix):
    matrix = np.asarray(matrix,dtype=float)
    node_num = matrix.shape[0]
    for i in range(node_num):
        for j in range(node_num):
            if(matrix[i][j])!=0:
                matrix[i][j] = 1
    return matrix


def getGraph(matrix):
    """
    Function to convert a matrix to a networkx graph object.
    :param matrix: the matrix which to convert.
    :return graph: NetworkX grapg object.
    """
    matrix = np.asarray(matrix,dtype=float)
    matrix = getOneZeroMatrix(matrix)
    G = nx.Graph()
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == 1:
                G.add_edge(i,j)
    return G


def getSimilariy(OneZeromatrix):
    node_num = len(OneZeromatrix)
    similar_matrix = np.zeros((node_num,node_num),dtype=float)
    graph = getGraph(OneZeromatrix)
    for i in range(node_num):
        neibor_i_list = list(graph.neighbors(i))
        neibor_i_num = len(neibor_i_list)
        for j in range(node_num):
            neibor_j_list = list(graph.neighbors(j))
            neibor_j_num = len(neibor_j_list)
            commonNeighbor_list = [x for x in neibor_i_list if x in neibor_j_list]
            commonNeighbor_num = len(commonNeighbor_list)
            similar_matrix[i][j] = (2*commonNeighbor_num)/(neibor_j_num + neibor_i_num)
    return similar_matrix

def getSimilariy_2 (OneZeromatrix):
    node_num = len(OneZeromatrix)
    similar_matrix = np.zeros((node_num, node_num), dtype=float)
    graph = getGraph(OneZeromatrix)
    print("Got graph done!")
    node_list = list(graph.node())
    for i, node in enumerate(node_list):
        neibor_i_list = list(graph.neighbors(node))
        first_neighbor = neibor_i_list
        for k, second_nighbor in enumerate(first_neighbor):
            second_list = list(graph.neighbors(second_nighbor))
            neibor_i_list = list(set(neibor_i_list).union(set(second_list)))
        neibor_i_num = len(first_neighbor)
        for j, node_j in enumerate(neibor_i_list):
            neibor_j_list = list(graph.neighbors(node_j))
            neibor_j_num = len(neibor_j_list)
            commonNeighbor_list = [x for x in first_neighbor if x in neibor_j_list]
            commonNeighbor_num = len(commonNeighbor_list)
            similar_matrix[node, node_j] = (2*commonNeighbor_num)/(neibor_j_num + neibor_i_num)
    return similar_matrix